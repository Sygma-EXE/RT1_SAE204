from Crypto.Cipher import DES
import base64
import hashlib

key = b'ef5cg8-6'
texte = b'text la ouais con'

hasinit=(hashlib.md5(texte).hexdigest())

#Chiffrement
enc = DES.new(key, DES.MODE_CFB)
cipher = enc.encrypt(texte)
enc_cipher = base64.b64encode(enc.iv + cipher)
#print(enc_cipher)

#Déchiffrement
decoded = base64.b64decode(enc_cipher)
iv = decoded[:8]
ciphertext = decoded[8:]

found=0
while found==0:
    fkey=0
    dec = DES.new(fkey, DES.MODE_CFB, iv)
    ptx = dec.decrypt(ciphertext)
    #print(ptx)
    fhash=(hashlib.md5(ptx).hexdigest())
    if fhash == hasinit:
        found=1
        print(fkey)