import numba
from numba import cuda

print("🧪 Vérification de l’environnement CUDA + Numba")
print("➡️ Numba version :", numba.__version__)

try:
    cuda_version = cuda.runtime.get_version()
    print("➡️ Version CUDA Runtime :", f"{cuda_version[0]}.{cuda_version[1]}")

    device = cuda.get_current_device()
    print("➡️ GPU détecté :", device.name.decode())
    print("➡️ Compute Capability :", device.compute_capability)

    # Utilise current_context().get_memory_info() à la place de get_attribute
    mem_free, mem_total = cuda.current_context().get_memory_info()
    print("➡️ Mémoire totale sur GPU :", mem_total // (1024 ** 2), "MB")
    print("➡️ Mémoire libre :", mem_free // (1024 ** 2), "MB")

except cuda.cudadrv.error.CudaSupportError:
    print("❌ Aucun GPU CUDA-compatible détecté ou problème de driver.")
except Exception as e:
    print("❌ Erreur CUDA inattendue :", e)

 
print("CUDA Runtime version :", cuda.runtime.get_version())
print("GPU détecté :", cuda.get_current_device().name.decode())