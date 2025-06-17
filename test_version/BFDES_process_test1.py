############################################################################################
#This programm is based on the BFDES-opti-test2 who is theoreticaly slower than the next   #
#version but this one is easier to try the use of multiprocess at the place of multiProcess#
############################################################################################


from Crypto.Cipher import DES
import base64
import itertools
import multiprocessing

key = b'uSD-fk83'
texte = b'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor. Cras elementum ultrices diam. Maecenas ligula massa, varius a, semper congue, euismod non, mi. Proin porttitor, orci nec nonummy molestie, enim est eleifend mi, non fermentum diam nisl sit amet erat. Duis semper. Duis arcu massa, scelerisque vitae, consequat in, pretium a, enim. Pellentesque congue. Ut in risus volutpat libero pharetra tempor. Cras vestibulum bibendum augue. Praesent egestas leo in pede. Praesent blandit odio eu enim. Pellentesque sed dui ut augue blandit sodales. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Aliquam nibh. Mauris ac mauris sed pede pellentesque fermentum. Maecenas adipiscing ante non diam sodales hendrerit.Ut velit mauris, egestas sed, gravida nec, ornare ut, mi. Aenean ut orci vel massa suscipit pulvinar. Nulla sollicitudin. Fusce varius, ligula non tempus aliquam, nunc turpis ullamcorper nibh, in tempus sapien eros vitae ligula. Pellentesque rhoncus nunc et augue. Integer id felis. Curabitur aliquet pellentesque diam. Integer quis metus vitae elit lobortis egestas. Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Morbi vel erat non mauris convallis vehicula. Nulla et sapien. Integer tortor tellus, aliquam faucibus, convallis id, congue eu, quam. Mauris ullamcorper felis vitae erat. Proin feugiat, augue non elementum posuere, metus purus iaculis lectus, et tristique ligula justo vitae magna.Aliquam convallis sollicitudin purus. Praesent aliquam, enim at fermentum mollis, ligula massa adipiscing nisl, ac euismod nibh nisl eu lectus. Fusce vulputate sem at sapien. Vivamus leo. Aliquam euismod libero eu enim. Nulla nec felis sed leo placerat imperdiet. Aenean suscipit nulla in justo. Suspendisse cursus rutrum augue. Nulla tincidunt tincidunt mi. Curabitur iaculis, lorem vel rhoncus faucibus, felis magna fermentum augue, et ultricies lacus lorem varius purus. Curabitur eu amet.'

#Chiffrement
enc = DES.new(key, DES.MODE_CFB)
cipher = enc.encrypt(texte)
enc_cipher = base64.b64encode(enc.iv + cipher)

#Déchiffrement
decoded = base64.b64decode(enc_cipher)
iv = decoded[:8]
ciphertext = decoded[8:]

def decrypta1():
    i=0
    for x in map(''.join,itertools.product('abdfhjlnprtvxzABDFHJLNPRTVXZ02468!"$&\'(*,.:<>@[\\^`{|~',repeat=8)):
        if i ==10000 or x[0] != 'a': 
            print(x)
            break
        fkey=x.encode('utf-8')
        #print(fkey,' -a')
        dec = DES.new(fkey, DES.MODE_CFB, iv)
        ptx = dec.decrypt(ciphertext)
        #print(ptx)
        if ptx == texte:
            print("Found Key: ",fkey)
        i+=1

def decryptb1():
    i=0
    for x in map(''.join,itertools.product('badfhjlnprtvxzABDFHJLNPRTVXZ02468!"$&\'(*,.:<>@[\\^`{|~',repeat=8)):
        if i ==10000 or x[0] != 'b': 
            print(x)
            break
        fkey=x.encode('utf-8')
        #print(fkey,' -b')
        dec = DES.new(fkey, DES.MODE_CFB, iv)
        ptx = dec.decrypt(ciphertext)
        #print(ptx)
        if ptx == texte:
            print("Found Key: ",fkey)
        i+=1

def decryptd1():
    i=0
    for x in map(''.join,itertools.product('dabfhjlnprtvxzABDFHJLNPRTVXZ02468!"$&\'(*,.:<>@[\\^`{|~',repeat=8)):
        if i ==10000 or x[0] != 'd': 
            print(x)
            break
        fkey=x.encode('utf-8')
        #print(fkey,' -d')
        dec = DES.new(fkey, DES.MODE_CFB, iv)
        ptx = dec.decrypt(ciphertext)
        #print(ptx)
        if ptx == texte:
            print("Found Key: ",fkey)
        i+=1

def decryptf1():
    i=0
    for x in map(''.join,itertools.product('fabdhjlnprtvxzABDFHJLNPRTVXZ02468!"$&\'(*,.:<>@[\\^`{|~',repeat=8)):
        if i ==10000 or x[0] != 'f': 
            print(x)
            break
        fkey=x.encode('utf-8')
        #print(fkey,' -f')
        dec = DES.new(fkey, DES.MODE_CFB, iv)
        ptx = dec.decrypt(ciphertext)
        #print(ptx)
        if ptx == texte:
            print("Found Key: ",fkey)
        i+=1

def decrypth1():
    i=0
    for x in map(''.join,itertools.product('habdfjlnprtvxzABDFHJLNPRTVXZ02468!"$&\'(*,.:<>@[\\^`{|~',repeat=8)):
        if i ==10000 or x[0] != 'h': 
            print(x)
            break
        fkey=x.encode('utf-8')
        #print(fkey,' -h')
        dec = DES.new(fkey, DES.MODE_CFB, iv)
        ptx = dec.decrypt(ciphertext)
        #print(ptx)
        if ptx == texte:
            print("Found Key: ",fkey)
        i+=1

def decryptj1():
    i=0
    for x in map(''.join,itertools.product('jabdfhlnprtvxzABDFHJLNPRTVXZ02468!"$&\'(*,.:<>@[\\^`{|~',repeat=8)):
        if i ==10000 or x[0] != 'j': 
            print(x)
            break
        fkey=x.encode('utf-8')
        #print(fkey,' -j')
        dec = DES.new(fkey, DES.MODE_CFB, iv)
        ptx = dec.decrypt(ciphertext)
        #print(ptx)
        if ptx == texte:
            print("Found Key: ",fkey)
        i+=1

def decryptl1():
    i=0
    for x in map(''.join,itertools.product('labdfhjnprtvxzABDFHJLNPRTVXZ02468!"$&\'(*,.:<>@[\\^`{|~',repeat=8)):
        if i ==10000 or x[0] != 'l': 
            print(x)
            break
        fkey=x.encode('utf-8')
        #print(fkey,' -l')
        dec = DES.new(fkey, DES.MODE_CFB, iv)
        ptx = dec.decrypt(ciphertext)
        #print(ptx)
        if ptx == texte:
            print("Found Key: ",fkey)
        i+=1

def decryptn1():
    i=0
    for x in map(''.join,itertools.product('nabdfhjlprtvxzABDFHJLNPRTVXZ02468!"$&\'(*,.:<>@[\\^`{|~',repeat=8)):
        if i ==10000 or x[0] != 'n': 
            print(x)
            break
        fkey=x.encode('utf-8')
        #print(fkey,' -n')
        dec = DES.new(fkey, DES.MODE_CFB, iv)
        ptx = dec.decrypt(ciphertext)
        #print(ptx)
        if ptx == texte:
            print("Found Key: ",fkey)
        i+=1

def decryptp1():
    i=0
    for x in map(''.join,itertools.product('pabdfhjlnrtvxzABDFHJLNPRTVXZ02468!"$&\'(*,.:<>@[\\^`{|~',repeat=8)):
        if i ==10000 or x[0] != 'p': 
            print(x)
            break
        fkey=x.encode('utf-8')
        #print(fkey,' -p')
        dec = DES.new(fkey, DES.MODE_CFB, iv)
        ptx = dec.decrypt(ciphertext)
        #print(ptx)
        if ptx == texte:
            print("Found Key: ",fkey)
        i+=1

def decryptr1():
    i=0
    for x in map(''.join,itertools.product('rabdfhjlnptvxzABDFHJLNPRTVXZ02468!"$&\'(*,.:<>@[\\^`{|~',repeat=8)):
        if i ==10000 or x[0] != 'r':
            print(x)
            break
        fkey=x.encode('utf-8')
        #print(fkey,' -r')
        dec = DES.new(fkey, DES.MODE_CFB, iv)
        ptx = dec.decrypt(ciphertext)
        #print(ptx)
        if ptx == texte:
            print("Found Key: ",fkey)
        i+=1

def decryptt1():
    i=0
    for x in map(''.join,itertools.product('tabdfhjlnprvxzABDFHJLNPRTVXZ02468!"$&\'(*,.:<>@[\\^`{|~',repeat=8)):
        if i ==10000 or x[0] != 't': 
            print(x)
            break
        fkey=x.encode('utf-8')
        #print(fkey,' -t')
        dec = DES.new(fkey, DES.MODE_CFB, iv)
        ptx = dec.decrypt(ciphertext)
        #print(ptx)
        if ptx == texte:
            print("Found Key: ",fkey)
        i+=1

def decryptv1():
    i=0
    for x in map(''.join,itertools.product('vabdfhjlnprtxzABDFHJLNPRTVXZ02468!"$&\'(*,.:<>@[\\^`{|~',repeat=8)):
        if i ==10000 or x[0] != 'v': 
            print(x)
            break
        fkey=x.encode('utf-8')
        #print(fkey,' -v')
        dec = DES.new(fkey, DES.MODE_CFB, iv)
        ptx = dec.decrypt(ciphertext)
        #print(ptx)
        if ptx == texte:
            print("Found Key: ",fkey)
        i+=1

def decryptx1():
    i=0
    for x in map(''.join,itertools.product('xabdfhjlnprtvzABDFHJLNPRTVXZ02468!"$&\'(*,.:<>@[\\^`{|~',repeat=8)):
        if i ==10000 or x[0] != 'x': 
            print(x)
            break
        fkey=x.encode('utf-8')
        #print(fkey,' -x')
        dec = DES.new(fkey, DES.MODE_CFB, iv)
        ptx = dec.decrypt(ciphertext)
        #print(ptx)
        if ptx == texte:
            print("Found Key: ",fkey)
        i+=1

def decryptz1():
    i=0
    for x in map(''.join,itertools.product('zabdfhjlnprtvxABDFHJLNPRTVXZ02468!"$&\'(*,.:<>@[\\^`{|~',repeat=8)):
        if i ==10000 or x[0] != 'z': 
            print(x)
            break
        fkey=x.encode('utf-8')
        #print(fkey,' -z')
        dec = DES.new(fkey, DES.MODE_CFB, iv)
        ptx = dec.decrypt(ciphertext)
        #print(ptx)
        if ptx == texte:
            print("Found Key: ",fkey)
        i+=1

def decryptGA1():
    i=0
    for x in map(''.join,itertools.product('AabdfhjlnprtvxzBDFHJLNPRTVXZ02468!"$&\'(*,.:<>@[\\^`{|~',repeat=8)):
        if i ==10000 or x[0] != 'A': 
            print(x)
            break
        fkey=x.encode('utf-8')
        ##print(fkey,' -a')
        dec = DES.new(fkey, DES.MODE_CFB, iv)
        ptx = dec.decrypt(ciphertext)
        #print(ptx)
        if ptx == texte:
            print("Found Key: ",fkey)
        i+=1

def decryptGB1():
    i=0
    for x in map(''.join,itertools.product('BabdfhjlnprtvxzADFHJLNPRTVXZ02468!"$&\'(*,.:<>@[\\^`{|~',repeat=8)):
        if i ==10000 or x[0] != 'B': 
            print(x)
            break
        fkey=x.encode('utf-8')
        #print(fkey,' -B')
        dec = DES.new(fkey, DES.MODE_CFB, iv)
        ptx = dec.decrypt(ciphertext)
        #print(ptx)
        if ptx == texte:
            print("Found Key: ",fkey)
        i+=1

def decryptGD1():
    i=0
    for x in map(''.join,itertools.product('DabdfhjlnprtvxzABFHJLNPRTVXZ02468!"$&\'(*,.:<>@[\\^`{|~',repeat=8)):
        if i ==10000 or x[0] != 'D': 
            print(x)
            break
        fkey=x.encode('utf-8')
        #print(fkey,' -D')
        dec = DES.new(fkey, DES.MODE_CFB, iv)
        ptx = dec.decrypt(ciphertext)
        #print(ptx)
        if ptx == texte:
            print("Found Key: ",fkey)
        i+=1

def decryptGF1():
    i=0
    for x in map(''.join,itertools.product('FabdfhjlnprtvxzABDHJLNPRTVXZ02468!"$&\'(*,.:<>@[\\^`{|~',repeat=8)):
        if i ==10000 or x[0] != 'F': 
            print(x)
            break
        fkey=x.encode('utf-8')
        #print(fkey,' -F')
        dec = DES.new(fkey, DES.MODE_CFB, iv)
        ptx = dec.decrypt(ciphertext)
        #print(ptx)
        if ptx == texte:
            print("Found Key: ",fkey)
        i+=1

def decryptGH1():
    i=0
    for x in map(''.join,itertools.product('HabdfhjlnprtvxzABDFJLNPRTVXZ02468!"$&\'(*,.:<>@[\\^`{|~',repeat=8)):
        if i ==10000 or x[0] != 'H': 
            print(x)
            break
        fkey=x.encode('utf-8')
        #print(fkey,' -H')
        dec = DES.new(fkey, DES.MODE_CFB, iv)
        ptx = dec.decrypt(ciphertext)
        #print(ptx)
        if ptx == texte:
            print("Found Key: ",fkey)
        i+=1

def decryptGJ1():
    i=0
    for x in map(''.join,itertools.product('JabdfhjlnprtvxzABDFHLNPRTVXZ02468!"$&\'(*,.:<>@[\\^`{|~',repeat=8)):
        if i ==10000 or x[0] != 'J': 
            print(x)
            break
        fkey=x.encode('utf-8')
        #print(fkey,' -J')
        dec = DES.new(fkey, DES.MODE_CFB, iv)
        ptx = dec.decrypt(ciphertext)
        #print(ptx)
        if ptx == texte:
            print("Found Key: ",fkey)
        i+=1

def decryptGL1():
    i=0
    for x in map(''.join,itertools.product('LabdfhjlnprtvxzABDFHJNPRTVXZ02468!"$&\'(*,.:<>@[\\^`{|~',repeat=8)):
        if i ==10000 or x[0] != 'L': 
            print(x)
            break
        fkey=x.encode('utf-8')
        #print(fkey,' -L')
        dec = DES.new(fkey, DES.MODE_CFB, iv)
        ptx = dec.decrypt(ciphertext)
        #print(ptx)
        if ptx == texte:
            print("Found Key: ",fkey)
        i+=1

def decryptGN1():
    i=0
    for x in map(''.join,itertools.product('NabdfhjlnprtvxzABDFHJLPRTVXZ02468!"$&\'(*,.:<>@[\\^`{|~',repeat=8)):
        if i ==10000 or x[0] != 'N': 
            print(x)
            break
        fkey=x.encode('utf-8')
        #print(fkey,' -N')
        dec = DES.new(fkey, DES.MODE_CFB, iv)
        ptx = dec.decrypt(ciphertext)
        #print(ptx)
        if ptx == texte:
            print("Found Key: ",fkey)
        i+=1

def decryptGP1():
    i=0
    for x in map(''.join,itertools.product('PabdfhjlnprtvxzABDFHJLNRTVXZ02468!"$&\'(*,.:<>@[\\^`{|~',repeat=8)):
        if i ==10000 or x[0] != 'P': 
            print(x)
            break
        fkey=x.encode('utf-8')
        #print(fkey,' -P')
        dec = DES.new(fkey, DES.MODE_CFB, iv)
        ptx = dec.decrypt(ciphertext)
        #print(ptx)
        if ptx == texte:
            print("Found Key: ",fkey)
        i+=1

def decryptGR1():
    i=0
    for x in map(''.join,itertools.product('RabdfhjlnprtvxzABDFHJLNPTVXZ02468!"$&\'(*,.:<>@[\\^`{|~',repeat=8)):
        if i ==10000 or x[0] != 'R': 
            print(x)
            break
        fkey=x.encode('utf-8')
        #print(fkey,' -R')
        dec = DES.new(fkey, DES.MODE_CFB, iv)
        ptx = dec.decrypt(ciphertext)
        #print(ptx)
        if ptx == texte:
            print("Found Key: ",fkey)
        i+=1

def decryptGT1():
    i=0
    for x in map(''.join,itertools.product('TabdfhjlnprtvxzABDFHJLNPRVXZ02468!"$&\'(*,.:<>@[\\^`{|~',repeat=8)):
        if i ==10000 or x[0] != 'T': 
            print(x)
            break
        fkey=x.encode('utf-8')
        #print(fkey,' -T')
        dec = DES.new(fkey, DES.MODE_CFB, iv)
        ptx = dec.decrypt(ciphertext)
        #print(ptx)
        if ptx == texte:
            print("Found Key: ",fkey)
        i+=1

def decryptGV1():
    i=0
    for x in map(''.join,itertools.product('VabdfhjlnprtvxzABDFHJLNPRTXZ02468!"$&\'(*,.:<>@[\\^`{|~',repeat=8)):
        if i ==10000 or x[0] != 'V': 
            print(x)
            break
        fkey=x.encode('utf-8')
        #print(fkey,' -V')
        dec = DES.new(fkey, DES.MODE_CFB, iv)
        ptx = dec.decrypt(ciphertext)
        #print(ptx)
        if ptx == texte:
            print("Found Key: ",fkey)
        i+=1

def decryptGX1():
    i=0
    for x in map(''.join,itertools.product('XabdfhjlnprtvxzABDFHJLNPRTVZ02468!"$&\'(*,.:<>@[\\^`{|~',repeat=8)):
        if i ==10000 or x[0] != 'X': 
            print(x)
            break
        fkey=x.encode('utf-8')
        #print(fkey,' -x')
        dec = DES.new(fkey, DES.MODE_CFB, iv)
        ptx = dec.decrypt(ciphertext)
        #print(ptx)
        if ptx == texte:
            print("Found Key: ",fkey)
        i+=1

def decryptGZ1():
    i=0
    for x in map(''.join,itertools.product('ZabdfhjlnprtvxzABDFHJLNPRTVX02468!"$&\'(*,.:<>@[\\^`{|~',repeat=8)):
        if i ==10000 or x[0] != 'Z': 
            print(x)
            break
        fkey=x.encode('utf-8')
        #print(fkey,' -Z')
        dec = DES.new(fkey, DES.MODE_CFB, iv)
        ptx = dec.decrypt(ciphertext)
        #print(ptx)
        if ptx == texte:
            print("Found Key: ",fkey)
        i+=1

def decrypt01():
    i=0
    for x in map(''.join,itertools.product('0abdfhjlnprtvxzABDFHJLNPRTVXZ2468!"$&\'(*,.:<>@[\\^`{|~',repeat=8)):
        if i ==10000 or x[0] != '0': 
            print(x)
            break
        fkey=x.encode('utf-8')
        #print(fkey,' -0')
        dec = DES.new(fkey, DES.MODE_CFB, iv)
        ptx = dec.decrypt(ciphertext)
        #print(ptx)
        if ptx == texte:
            print("Found Key: ",fkey)
        i+=1

def decrypt21():
    i=0
    for x in map(''.join,itertools.product('2abdfhjlnprtvxzABDFHJLNPRTVXZ0468!"$&\'(*,.:<>@[\\^`{|~',repeat=8)):
        if i ==10000 or x[0] != '2': 
            print(x)
            break
        fkey=x.encode('utf-8')
        #print(fkey,' -2')
        dec = DES.new(fkey, DES.MODE_CFB, iv)
        ptx = dec.decrypt(ciphertext)
        #print(ptx)
        if ptx == texte:
            print("Found Key: ",fkey)
        i+=1

def decrypt41():
    i=0
    for x in map(''.join,itertools.product('4abdfhjlnprtvxzABDFHJLNPRTVXZ0268!"$&\'(*,.:<>@[\\^`{|~',repeat=8)):
        if i ==10000 or x[0] != '4': 
            print(x)
            break
        fkey=x.encode('utf-8')
        #print(fkey,' -4')
        dec = DES.new(fkey, DES.MODE_CFB, iv)
        ptx = dec.decrypt(ciphertext)
        #print(ptx)
        if ptx == texte:
            print("Found Key: ",fkey)
        i+=1

def decrypt61():
    i=0
    for x in map(''.join,itertools.product('6abdfhjlnprtvxzABDFHJLNPRTVXZ0248!"$&\'(*,.:<>@[\\^`{|~',repeat=8)):
        if i ==10000 or x[0] != '6': 
            print(x)
            break
        fkey=x.encode('utf-8')
        #print(fkey,' -6')
        dec = DES.new(fkey, DES.MODE_CFB, iv)
        ptx = dec.decrypt(ciphertext)
        #print(ptx)
        if ptx == texte:
            print("Found Key: ",fkey)
        i+=1

def decrypt81():
    i=0
    for x in map(''.join,itertools.product('8abdfhjlnprtvxzABDFHJLNPRTVXZ0246!"$&\'(*,.:<>@[\\^`{|~',repeat=8)):
        if i ==10000 or x[0] != '8': 
            print(x)
            break
        fkey=x.encode('utf-8')
        #print(fkey,' -8')
        dec = DES.new(fkey, DES.MODE_CFB, iv)
        ptx = dec.decrypt(ciphertext)
        #print(ptx)
        if ptx == texte:
            print("Found Key: ",fkey)
        i+=1

def decryptex1(): #!
    i=0
    for x in map(''.join,itertools.product('!abdfhjlnprtvxzABDFHJLNPRTVXZ02468"$&\'(*,.:<>@[\\^`{|~',repeat=8)):
        if i ==10000 or x[0] != '!': 
            print(x)
            break
        fkey=x.encode('utf-8')
        #print(fkey,' -!')
        dec = DES.new(fkey, DES.MODE_CFB, iv)
        ptx = dec.decrypt(ciphertext)
        #print(ptx)
        if ptx == texte:
            print("Found Key: ",fkey)
        i+=1

def decryptdq1(): #"
    i=0
    for x in map(''.join,itertools.product('"abdfhjlnprtvxzABDFHJLNPRTVXZ02468!$&\'(*,.:<>@[\\^`{|~',repeat=8)):
        if i ==10000 or x[0] != '"': 
            print(x)
            break
        fkey=x.encode('utf-8')
        #print(fkey,' -"')
        dec = DES.new(fkey, DES.MODE_CFB, iv)
        ptx = dec.decrypt(ciphertext)
        #print(ptx)
        if ptx == texte:
            print("Found Key: ",fkey)
        i+=1

def decryptdol1(): #$
    i=0
    for x in map(''.join,itertools.product('$abdfhjlnprtvxzABDFHJLNPRTVXZ02468!"&\'(*,.:<>@[\\^`{|~',repeat=8)):
        if i ==10000 or x[0] != '$': 
            print(x)
            break
        fkey=x.encode('utf-8')
        #print(fkey,' -$')
        dec = DES.new(fkey, DES.MODE_CFB, iv)
        ptx = dec.decrypt(ciphertext)
        #print(ptx)
        if ptx == texte:
            print("Found Key: ",fkey)
        i+=1


def decryptes1(): #&
    i=0
    for x in map(''.join,itertools.product('&abdfhjlnprtvxzABDFHJLNPRTVXZ02468!"$\'(*,.:<>@[\\^`{|~',repeat=8)):
        if i ==10000 or x[0] != '&': 
            print(x)
            break
        fkey=x.encode('utf-8')
        #print(fkey,' -&')
        dec = DES.new(fkey, DES.MODE_CFB, iv)
        ptx = dec.decrypt(ciphertext)
        #print(ptx)
        if ptx == texte:
            print("Found Key: ",fkey)
        i+=1

def decryptasq1(): #'
    i=0
    for x in map(''.join,itertools.product('\'abdfhjlnprtvxzABDFHJLNPRTVXZ02468!"$&(*,.:<>@[\\^`{|~',repeat=8)):
        if i ==10000 or x[0] != '\'': 
            print(x)
            break
        fkey=x.encode('utf-8')
        #print(fkey,' -\'')
        dec = DES.new(fkey, DES.MODE_CFB, iv)
        ptx = dec.decrypt(ciphertext)
        #print(ptx)
        if ptx == texte:
            print("Found Key: ",fkey)
        i+=1

def decryptpo1(): #(
    i=0
    for x in map(''.join,itertools.product('(abdfhjlnprtvxzABDFHJLNPRTVXZ02468!"$&\'*,.:<>@[\\^`{|~',repeat=8)):
        if i ==10000 or x[0] != '(': 
            print(x)
            break
        fkey=x.encode('utf-8')
        #print(fkey,' -(')
        dec = DES.new(fkey, DES.MODE_CFB, iv)
        ptx = dec.decrypt(ciphertext)
        #print(ptx)
        if ptx == texte:
            print("Found Key: ",fkey)
        i+=1

def decryptast1(): #*
    i=0
    for x in map(''.join,itertools.product('*abdfhjlnprtvxzABDFHJLNPRTVXZ02468!"$&\'(,.:<>@[\\^`{|~',repeat=8)):
        if i ==10000 or x[0] != '*': 
            print(x)
            break
        fkey=x.encode('utf-8')
        #print(fkey,' -*')
        dec = DES.new(fkey, DES.MODE_CFB, iv)
        ptx = dec.decrypt(ciphertext)
        #print(ptx)
        if ptx == texte:
            print("Found Key: ",fkey)
        i+=1

def decryptcom1(): #,
    i=0
    for x in map(''.join,itertools.product(',abdfhjlnprtvxzABDFHJLNPRTVXZ02468!"$&\'(*.:<>@[\\^`{|~',repeat=8)):
        if i ==10000 or x[0] != ',': 
            print(x)
            break
        fkey=x.encode('utf-8')
        #print(fkey,' -,')
        dec = DES.new(fkey, DES.MODE_CFB, iv)
        ptx = dec.decrypt(ciphertext)
        #print(ptx)
        if ptx == texte:
            print("Found Key: ",fkey)
        i+=1

def decryptpoin1(): #.
    i=0
    for x in map(''.join,itertools.product('.abdfhjlnprtvxzABDFHJLNPRTVXZ02468!"$&\'(*,:<>@[\\^`{|~',repeat=8)):
        if i ==10000 or x[0] != '.': 
            print(x)
            break
        fkey=x.encode('utf-8')
        #print(fkey,' -.')
        dec = DES.new(fkey, DES.MODE_CFB, iv)
        ptx = dec.decrypt(ciphertext)
        #print(ptx)
        if ptx == texte:
            print("Found Key: ",fkey)
        i+=1

def decryptdpoi1(): #:
    i=0
    for x in map(''.join,itertools.product(':abdfhjlnprtvxzABDFHJLNPRTVXZ02468!"$&\'(*,.<>@[\\^`{|~',repeat=8)):
        if i ==10000 or x[0] != ':': 
            print(x)
            break
        fkey=x.encode('utf-8')
        #print(fkey,' -:')
        dec = DES.new(fkey, DES.MODE_CFB, iv)
        ptx = dec.decrypt(ciphertext)
        #print(ptx)
        if ptx == texte:
            print("Found Key: ",fkey)
        i+=1

def decryptmo1(): #<
    i=0
    for x in map(''.join,itertools.product('<abdfhjlnprtvxzABDFHJLNPRTVXZ02468!"$&\'(*,.:>@[\\^`{|~',repeat=8)):
        if i ==10000 or x[0] != '<': 
            print(x)
            break
        fkey=x.encode('utf-8')
        #print(fkey,' -<')
        dec = DES.new(fkey, DES.MODE_CFB, iv)
        ptx = dec.decrypt(ciphertext)
        #print(ptx)
        if ptx == texte:
            print("Found Key: ",fkey)
        i+=1

def decryptmi1(): #>
    i=0
    for x in map(''.join,itertools.product('>abdfhjlnprtvxzABDFHJLNPRTVXZ02468!"$&\'(*,.:<@[\\^`{|~',repeat=8)):
        if i ==10000 or x[0] != '>': 
            print(x)
            break
        fkey=x.encode('utf-8')
        #print(fkey,' ->')
        dec = DES.new(fkey, DES.MODE_CFB, iv)
        ptx = dec.decrypt(ciphertext)
        #print(ptx)
        if ptx == texte:
            print("Found Key: ",fkey)
        i+=1

def decryptat1(): #@
    i=0
    for x in map(''.join,itertools.product('@abdfhjlnprtvxzABDFHJLNPRTVXZ02468!"$&\'(*,.:<>[\\^`{|~',repeat=8)):
        if i ==10000 or x[0] != '@': 
            print(x)
            break
        fkey=x.encode('utf-8')
        #print(fkey,' -@')
        dec = DES.new(fkey, DES.MODE_CFB, iv)
        ptx = dec.decrypt(ciphertext)
        #print(ptx)
        if ptx == texte:
            print("Found Key: ",fkey)
        i+=1

def decryptoc1(): #[
    i=0
    for x in map(''.join,itertools.product('[abdfhjlnprtvxzABDFHJLNPRTVXZ02468!"$&\'(*,.:<>@\\^`{|~',repeat=8)):
        if i ==10000 or x[0] != '[': 
            print(x)
            break
        fkey=x.encode('utf-8')
        #print(fkey,' -[')
        dec = DES.new(fkey, DES.MODE_CFB, iv)
        ptx = dec.decrypt(ciphertext)
        #print(ptx)
        if ptx == texte:
            print("Found Key: ",fkey)
        i+=1

def decryptbs1(): #\
    i=0
    for x in map(''.join,itertools.product('\\abdfhjlnprtvxzABDFHJLNPRTVXZ02468!"$&\'(*,.:<>@[^`{|~',repeat=8)):
        if i ==10000 or x[0] != '\\': 
            print(x)
            break
        fkey=x.encode('utf-8')
        #print(fkey,' -\\')
        dec = DES.new(fkey, DES.MODE_CFB, iv)
        ptx = dec.decrypt(ciphertext)
        #print(ptx)
        if ptx == texte:
            print("Found Key: ",fkey)
        i+=1

def decryptcir1(): #^
    i=0
    for x in map(''.join,itertools.product('^abdfhjlnprtvxzABDFHJLNPRTVXZ02468!"$&\'(*,.:<>@[\\{|~',repeat=8)):
        if i ==10000 or x[0] != '^': 
            print(x)
            break
        fkey=x.encode('utf-8')
        #print(fkey,' -^')
        dec = DES.new(fkey, DES.MODE_CFB, iv)
        ptx = dec.decrypt(ciphertext)
        #print(ptx)
        if ptx == texte:
            print("Found Key: ",fkey)
        i+=1

def decryptidk1(): #`
    i=0
    for x in map(''.join,itertools.product('`abdfhjlnprtvxzABDFHJLNPRTVXZ02468!"$&\'(*,.:<>@[\\^`{|~',repeat=8)):
        if i ==10000 or x[0] != '`': 
            print(x)
            break
        fkey=x.encode('utf-8')
        #print(fkey,' -`')
        dec = DES.new(fkey, DES.MODE_CFB, iv)
        ptx = dec.decrypt(ciphertext)
        #print(ptx)
        if ptx == texte:
            print("Found Key: ",fkey)
        i+=1

def decryptosc1(): #{
    i=0
    for x in map(''.join,itertools.product('{abdfhjlnprtvxzABDFHJLNPRTVXZ02468!"$&\'(*,.:<>@[\\^`{|~',repeat=8)):
        if i ==10000 or x[0] != '{': 
            print(x)
            break
        fkey=x.encode('utf-8')
        #print(fkey,' -{')
        dec = DES.new(fkey, DES.MODE_CFB, iv)
        ptx = dec.decrypt(ciphertext)
        #print(ptx)
        if ptx == texte:
            print("Found Key: ",fkey)
        i+=1

def decryptss1(): #|
    i=0
    for x in map(''.join,itertools.product('|abdfhjlnprtvxzABDFHJLNPRTVXZ02468!"$&\'(*,.:<>@[\\^`{~',repeat=8)):
        if i ==10000 or x[0] != '|': 
            print(x)
            break
        fkey=x.encode('utf-8')
        #print(fkey,' -|')
        dec = DES.new(fkey, DES.MODE_CFB, iv)
        ptx = dec.decrypt(ciphertext)
        #print(ptx)
        if ptx == texte:
            print("Found Key: ",fkey)
        i+=1

def decrypttild1(): #~
    i=0
    for x in map(''.join,itertools.product('~abdfhjlnprtvxzABDFHJLNPRTVXZ02468!"$&\'(*,.:<>@[\\^`{|',repeat=8)):
        if i ==10000 or x[0] != '~': 
            print(x)
            break
        fkey=x.encode('utf-8')
        #print(fkey,' -~')
        dec = DES.new(fkey, DES.MODE_CFB, iv)
        ptx = dec.decrypt(ciphertext)
        #print(ptx)
        if ptx == texte:
            print("Found Key: ",fkey)
        i+=1

if __name__ == "__main__":

    Processa = multiprocessing.Process(target=decrypta1)
    Processb = multiprocessing.Process(target=decryptb1)
    Processd = multiprocessing.Process(target=decryptd1)
    Processf = multiprocessing.Process(target=decryptf1)
    Processh = multiprocessing.Process(target=decrypth1)
    Processj = multiprocessing.Process(target=decryptj1)
    Processl = multiprocessing.Process(target=decryptl1)
    Processn = multiprocessing.Process(target=decryptn1)
    Processp = multiprocessing.Process(target=decryptp1)
    Processr = multiprocessing.Process(target=decryptr1)
    Processt = multiprocessing.Process(target=decryptt1)
    Processv = multiprocessing.Process(target=decryptv1)
    Processx = multiprocessing.Process(target=decryptx1)
    Processz = multiprocessing.Process(target=decryptz1)
    ProcessGA = multiprocessing.Process(target=decryptGA1)
    ProcessGB = multiprocessing.Process(target=decryptGB1)
    ProcessGD = multiprocessing.Process(target=decryptGD1)
    ProcessGF = multiprocessing.Process(target=decryptGF1)
    ProcessGH = multiprocessing.Process(target=decryptGH1)
    ProcessGJ = multiprocessing.Process(target=decryptGJ1)
    ProcessGL = multiprocessing.Process(target=decryptGL1)
    ProcessGN = multiprocessing.Process(target=decryptGN1)
    ProcessGP = multiprocessing.Process(target=decryptGP1)
    ProcessGR = multiprocessing.Process(target=decryptGR1)
    ProcessGT = multiprocessing.Process(target=decryptGT1)
    ProcessGV = multiprocessing.Process(target=decryptGV1)
    ProcessGX = multiprocessing.Process(target=decryptGX1)
    ProcessGZ = multiprocessing.Process(target=decryptGZ1)
    Process0 = multiprocessing.Process(target=decrypt01)
    Process2 = multiprocessing.Process(target=decrypt21)
    Process4 = multiprocessing.Process(target=decrypt41)
    Process6 = multiprocessing.Process(target=decrypt61)
    Process8 = multiprocessing.Process(target=decrypt81)
    Processex = multiprocessing.Process(target=decryptex1)
    Processdq = multiprocessing.Process(target=decryptdq1)
    Processdol = multiprocessing.Process(target=decryptdol1)
    Processes = multiprocessing.Process(target=decryptes1)
    Processsq = multiprocessing.Process(target=decryptasq1)
    Processpo = multiprocessing.Process(target=decryptpo1)
    Processast = multiprocessing.Process(target=decryptast1)
    Processcom = multiprocessing.Process(target=decryptcom1)
    Processpoin = multiprocessing.Process(target=decryptpoin1)
    Processdpoi = multiprocessing.Process(target=decryptdpoi1)
    Processmo = multiprocessing.Process(target=decryptmo1)
    Processmi = multiprocessing.Process(target=decryptmi1)
    Processat = multiprocessing.Process(target=decryptat1)
    Processoc = multiprocessing.Process(target=decryptoc1)
    Processbs = multiprocessing.Process(target=decryptbs1)
    Processcir = multiprocessing.Process(target=decryptcir1)
    Processidk = multiprocessing.Process(target=decryptidk1)
    Processosc = multiprocessing.Process(target=decryptosc1)
    Processss = multiprocessing.Process(target=decryptss1)
    Processtild = multiprocessing.Process(target=decrypttild1)

    Processa.start()
    Processb.start()
    Processd.start()
    Processf.start()
    Processh.start()
    Processj.start()
    Processl.start()
    Processn.start()
    Processp.start()
    Processr.start()
    Processt.start()
    Processv.start()
    Processx.start()
    Processz.start()
    ProcessGA.start()
    ProcessGB.start()
    ProcessGD.start()
    ProcessGF.start()
    ProcessGH.start()
    ProcessGJ.start()
    ProcessGL.start()
    ProcessGN.start()
    ProcessGP.start()
    ProcessGR.start()
    ProcessGT.start()
    ProcessGV.start()
    ProcessGX.start()
    ProcessGZ.start()
    Process0.start()
    Process2.start()
    Process4.start()
    Process6.start()
    Process8.start()
    Processex.start()
    Processdq.start()
    Processdol.start()
    Processes.start()
    Processsq.start()
    Processpo.start()
    Processast.start()
    Processcom.start()
    Processpoin.start()
    Processdpoi.start()
    Processmo.start()
    Processmi.start()
    Processat.start()
    Processoc.start()
    Processbs.start()
    Processcir.start()
    Processidk.start()
    Processosc.start()
    Processss.start()
    Processtild.start()