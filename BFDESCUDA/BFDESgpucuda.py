from numba import cuda
import numpy as np
import math
from des import des  # Assure-toi d’avoir le fichier des.py dans le même dossier

# === CONFIGURATION ===
charset_str = 'abdfhjlnprtvxzABDFHJLNPRTVXZ02468!"$&\'(*,.:<>@[\\^`{|~'
charset = charset_str.encode('utf-8')
charset_len = len(charset)
key_length = 8
plaintext = "Message secret GPU brute-force"
true_key = "aaaaaAz8"

# === Chiffrement du message avec la vraie clé ===
d = des()
ciphertext = d.encrypt(true_key, plaintext, padding=True)

# === GPU kernel : génère les clés à partir d’un index de départ et d’un batch_size ===
@cuda.jit
def generate_keys(start_idx, keys_out, charset, charset_len, key_length):
    idx = cuda.grid(1)
    real_idx = start_idx + idx
    if idx >= keys_out.shape[0]:
        return

    key = cuda.local.array(8, dtype=np.uint8)
    i = real_idx
    for j in range(key_length - 1, -1, -1):
        key[j] = charset[i % charset_len]
        i //= charset_len

    for j in range(key_length):
        keys_out[idx, j] = key[j]


def run_gpu_bruteforce():
    print("🔐 Texte chiffré :", ciphertext)

    total_keys = charset_len ** key_length
    print(f"🔎 Tentatives totales : {total_keys}")

    batch_size = 1_000_000  # 1 million de clés par batch (à ajuster selon ta RAM / GPU)
    threads_per_block = 128
    des_instance = des()

    charset_device = cuda.to_device(np.array(list(charset), dtype=np.uint8))

    for start in range(0, total_keys, batch_size):
        current_batch_size = min(batch_size, total_keys - start)

        # Préparation buffers batch
        keys_gpu = np.zeros((current_batch_size, key_length), dtype=np.uint8)
        keys_device = cuda.to_device(keys_gpu)

        blocks = math.ceil(current_batch_size / threads_per_block)
        generate_keys[blocks, threads_per_block](start, keys_device, charset_device, charset_len, key_length)

        keys_device.copy_to_host(keys_gpu)

        # Test CPU sur ce batch
        for i in range(current_batch_size):
            candidate_key = keys_gpu[i].tobytes().decode(errors='ignore')
            try:
                decrypted = des_instance.decrypt(candidate_key, ciphertext, padding=True)
                if decrypted == plaintext:
                    print("✅ Clé trouvée :", candidate_key)
                    return
            except Exception:
                pass

        print(f"Batch {start // batch_size + 1} / {math.ceil(total_keys / batch_size)} testé...")

    print("❌ Aucune clé correcte trouvée.")


# === Exécution ===
if __name__ == "__main__":
    run_gpu_bruteforce()
