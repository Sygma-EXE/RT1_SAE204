from Crypto.Cipher import DES
import base64
import hashlib
import itertools
import threading

key = b'uSD-fk83'
texte = b'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor. Cras elementum ultrices diam. Maecenas ligula massa, varius a, semper congue, euismod non, mi. Proin porttitor, orci nec nonummy molestie, enim est eleifend mi, non fermentum diam nisl sit amet erat. Duis semper. Duis arcu massa, scelerisque vitae, consequat in, pretium a, enim. Pellentesque congue. Ut in risus volutpat libero pharetra tempor. Cras vestibulum bibendum augue. Praesent egestas leo in pede. Praesent blandit odio eu enim. Pellentesque sed dui ut augue blandit sodales. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Aliquam nibh. Mauris ac mauris sed pede pellentesque fermentum. Maecenas adipiscing ante non diam sodales hendrerit.Ut velit mauris, egestas sed, gravida nec, ornare ut, mi. Aenean ut orci vel massa suscipit pulvinar. Nulla sollicitudin. Fusce varius, ligula non tempus aliquam, nunc turpis ullamcorper nibh, in tempus sapien eros vitae ligula. Pellentesque rhoncus nunc et augue. Integer id felis. Curabitur aliquet pellentesque diam. Integer quis metus vitae elit lobortis egestas. Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Morbi vel erat non mauris convallis vehicula. Nulla et sapien. Integer tortor tellus, aliquam faucibus, convallis id, congue eu, quam. Mauris ullamcorper felis vitae erat. Proin feugiat, augue non elementum posuere, metus purus iaculis lectus, et tristique ligula justo vitae magna.Aliquam convallis sollicitudin purus. Praesent aliquam, enim at fermentum mollis, ligula massa adipiscing nisl, ac euismod nibh nisl eu lectus. Fusce vulputate sem at sapien. Vivamus leo. Aliquam euismod libero eu enim. Nulla nec felis sed leo placerat imperdiet. Aenean suscipit nulla in justo. Suspendisse cursus rutrum augue. Nulla tincidunt tincidunt mi. Curabitur iaculis, lorem vel rhoncus faucibus, felis magna fermentum augue, et ultricies lacus lorem varius purus. Curabitur eu amet.'

#hasinit=(hashlib.md5(texte).hexdigest())

#Chiffrement
enc = DES.new(key, DES.MODE_CFB)
cipher = enc.encrypt(texte)
enc_cipher = base64.b64encode(enc.iv + cipher)
#print(enc_cipher)

#Déchiffrement
decoded = base64.b64decode(enc_cipher)
iv = decoded[:8]
ciphertext = decoded[8:]

##############################################################################################
#we going to generate each key starting by each craracter of the list into a different thread#
#estimated time on the base laptop: 163 years                                                #
##############################################################################################

def decrypta():
    i=0
    for x in map(''.join,itertools.product('abdfhjlnprtvxzABDFHJLNPRTVXZ02468!"$&\'(*,.:<>@[\^`{|~',repeat=8)):
        if i ==1000 or x[0] != 'a': 
            break
        fkey=x.encode('utf-8')
        print(fkey,' -a')
        dec = DES.new(fkey, DES.MODE_CFB, iv)
        ptx = dec.decrypt(ciphertext)
        #print(ptx)
        if ptx == texte:
            print("Found Key: ",fkey)
        i+=1

def decryptb():
    i=0
    for x in map(''.join,itertools.product('badfhjlnprtvxzABDFHJLNPRTVXZ02468!"$&\'(*,.:<>@[\^`{|~',repeat=8)):
        if i ==1000 or x[0] != 'b': 
            break
        fkey=x.encode('utf-8')
        print(fkey,' -b')
        dec = DES.new(fkey, DES.MODE_CFB, iv)
        ptx = dec.decrypt(ciphertext)
        #print(ptx)
        if ptx == texte:
            print("Found Key: ",fkey)
        i+=1

def decryptd():
    i=0
    for x in map(''.join,itertools.product('dabfhjlnprtvxzABDFHJLNPRTVXZ02468!"$&\'(*,.:<>@[\^`{|~',repeat=8)):
        if i ==1000 or x[0] != 'd': 
            break
        fkey=x.encode('utf-8')
        print(fkey,' -d')
        dec = DES.new(fkey, DES.MODE_CFB, iv)
        ptx = dec.decrypt(ciphertext)
        #print(ptx)
        if ptx == texte:
            print("Found Key: ",fkey)
        i+=1

def decryptf():
    i=0
    for x in map(''.join,itertools.product('fabdhjlnprtvxzABDFHJLNPRTVXZ02468!"$&\'(*,.:<>@[\^`{|~',repeat=8)):
        if i ==1000 or x[0] != 'f': 
            break
        fkey=x.encode('utf-8')
        print(fkey,' -f')
        dec = DES.new(fkey, DES.MODE_CFB, iv)
        ptx = dec.decrypt(ciphertext)
        #print(ptx)
        if ptx == texte:
            print("Found Key: ",fkey)
        i+=1

def decrypth():
    i=0
    for x in map(''.join,itertools.product('habdfjlnprtvxzABDFHJLNPRTVXZ02468!"$&\'(*,.:<>@[\^`{|~',repeat=8)):
        if i ==1000 or x[0] != 'h': 
            break
        fkey=x.encode('utf-8')
        print(fkey,' -h')
        dec = DES.new(fkey, DES.MODE_CFB, iv)
        ptx = dec.decrypt(ciphertext)
        #print(ptx)
        if ptx == texte:
            print("Found Key: ",fkey)
        i+=1

def decryptj():
    i=0
    for x in map(''.join,itertools.product('jabdfhlnprtvxzABDFHJLNPRTVXZ02468!"$&\'(*,.:<>@[\^`{|~',repeat=8)):
        if i ==1000 or x[0] != 'j': 
            break
        fkey=x.encode('utf-8')
        print(fkey,' -j')
        dec = DES.new(fkey, DES.MODE_CFB, iv)
        ptx = dec.decrypt(ciphertext)
        #print(ptx)
        if ptx == texte:
            print("Found Key: ",fkey)
        i+=1

def decryptl():
    i=0
    for x in map(''.join,itertools.product('labdfhjnprtvxzABDFHJLNPRTVXZ02468!"$&\'(*,.:<>@[\^`{|~',repeat=8)):
        if i ==1000 or x[0] != 'l': 
            break
        fkey=x.encode('utf-8')
        print(fkey,' -l')
        dec = DES.new(fkey, DES.MODE_CFB, iv)
        ptx = dec.decrypt(ciphertext)
        #print(ptx)
        if ptx == texte:
            print("Found Key: ",fkey)
        i+=1

def decryptn():
    i=0
    for x in map(''.join,itertools.product('nabdfhjlprtvxzABDFHJLNPRTVXZ02468!"$&\'(*,.:<>@[\^`{|~',repeat=8)):
        if i ==1000 or x[0] != 'n': 
            break
        fkey=x.encode('utf-8')
        print(fkey,' -n')
        dec = DES.new(fkey, DES.MODE_CFB, iv)
        ptx = dec.decrypt(ciphertext)
        #print(ptx)
        if ptx == texte:
            print("Found Key: ",fkey)
        i+=1

def decryptp():
    i=0
    for x in map(''.join,itertools.product('pabdfhjlnrtvxzABDFHJLNPRTVXZ02468!"$&\'(*,.:<>@[\^`{|~',repeat=8)):
        if i ==1000 or x[0] != 'p': 
            break
        fkey=x.encode('utf-8')
        print(fkey,' -p')
        dec = DES.new(fkey, DES.MODE_CFB, iv)
        ptx = dec.decrypt(ciphertext)
        #print(ptx)
        if ptx == texte:
            print("Found Key: ",fkey)
        i+=1

def decryptr():
    i=0
    for x in map(''.join,itertools.product('rabdfhjlnptvxzABDFHJLNPRTVXZ02468!"$&\'(*,.:<>@[\^`{|~',repeat=8)):
        if i ==1000 or x[0] != 'r':
            break
        fkey=x.encode('utf-8')
        print(fkey,' -r')
        dec = DES.new(fkey, DES.MODE_CFB, iv)
        ptx = dec.decrypt(ciphertext)
        #print(ptx)
        if ptx == texte:
            print("Found Key: ",fkey)
        i+=1

def decryptt():
    i=0
    for x in map(''.join,itertools.product('tabdfhjlnprvxzABDFHJLNPRTVXZ02468!"$&\'(*,.:<>@[\^`{|~',repeat=8)):
        if i ==1000 or x[0] != 't': 
            break
        fkey=x.encode('utf-8')
        print(fkey,' -t')
        dec = DES.new(fkey, DES.MODE_CFB, iv)
        ptx = dec.decrypt(ciphertext)
        #print(ptx)
        if ptx == texte:
            print("Found Key: ",fkey)
        i+=1

def decryptv():
    i=0
    for x in map(''.join,itertools.product('vabdfhjlnprtxzABDFHJLNPRTVXZ02468!"$&\'(*,.:<>@[\^`{|~',repeat=8)):
        if i ==1000 or x[0] != 'v': 
            break
        fkey=x.encode('utf-8')
        print(fkey,' -v')
        dec = DES.new(fkey, DES.MODE_CFB, iv)
        ptx = dec.decrypt(ciphertext)
        #print(ptx)
        if ptx == texte:
            print("Found Key: ",fkey)
        i+=1

def decryptx():
    i=0
    for x in map(''.join,itertools.product('xabdfhjlnprtvzABDFHJLNPRTVXZ02468!"$&\'(*,.:<>@[\^`{|~',repeat=8)):
        if i ==1000 or x[0] != 'x': 
            break
        fkey=x.encode('utf-8')
        print(fkey,' -x')
        dec = DES.new(fkey, DES.MODE_CFB, iv)
        ptx = dec.decrypt(ciphertext)
        #print(ptx)
        if ptx == texte:
            print("Found Key: ",fkey)
        i+=1

def decryptz():
    i=0
    for x in map(''.join,itertools.product('zabdfhjlnprtvxABDFHJLNPRTVXZ02468!"$&\'(*,.:<>@[\^`{|~',repeat=8)):
        if i ==1000 or x[0] != 'z': 
            break
        fkey=x.encode('utf-8')
        print(fkey,' -z')
        dec = DES.new(fkey, DES.MODE_CFB, iv)
        ptx = dec.decrypt(ciphertext)
        #print(ptx)
        if ptx == texte:
            print("Found Key: ",fkey)
        i+=1

def decryptGA():
    i=0
    for x in map(''.join,itertools.product('AabdfhjlnprtvxzBDFHJLNPRTVXZ02468!"$&\'(*,.:<>@[\^`{|~',repeat=8)):
        if i ==1000 or x[0] != 'A': 
            break
        fkey=x.encode('utf-8')
        print(fkey,' -A')
        dec = DES.new(fkey, DES.MODE_CFB, iv)
        ptx = dec.decrypt(ciphertext)
        #print(ptx)
        if ptx == texte:
            print("Found Key: ",fkey)
        i+=1

def decryptGB():
    i=0
    for x in map(''.join,itertools.product('BabdfhjlnprtvxzADFHJLNPRTVXZ02468!"$&\'(*,.:<>@[\^`{|~',repeat=8)):
        if i ==1000 or x[0] != 'B': 
            break
        fkey=x.encode('utf-8')
        print(fkey,' -B')
        dec = DES.new(fkey, DES.MODE_CFB, iv)
        ptx = dec.decrypt(ciphertext)
        #print(ptx)
        if ptx == texte:
            print("Found Key: ",fkey)
        i+=1

def decryptGD():
    i=0
    for x in map(''.join,itertools.product('DabdfhjlnprtvxzABFHJLNPRTVXZ02468!"$&\'(*,.:<>@[\^`{|~',repeat=8)):
        if i ==1000 or x[0] != 'D': 
            break
        fkey=x.encode('utf-8')
        print(fkey,' -D')
        dec = DES.new(fkey, DES.MODE_CFB, iv)
        ptx = dec.decrypt(ciphertext)
        #print(ptx)
        if ptx == texte:
            print("Found Key: ",fkey)
        i+=1

def decryptGF():
    i=0
    for x in map(''.join,itertools.product('FabdfhjlnprtvxzABDHJLNPRTVXZ02468!"$&\'(*,.:<>@[\^`{|~',repeat=8)):
        if i ==1000 or x[0] != 'F': 
            break
        fkey=x.encode('utf-8')
        print(fkey,' -F')
        dec = DES.new(fkey, DES.MODE_CFB, iv)
        ptx = dec.decrypt(ciphertext)
        #print(ptx)
        if ptx == texte:
            print("Found Key: ",fkey)
        i+=1

def decryptGH():
    i=0
    for x in map(''.join,itertools.product('HabdfhjlnprtvxzABDFJLNPRTVXZ02468!"$&\'(*,.:<>@[\^`{|~',repeat=8)):
        if i ==1000 or x[0] != 'H': 
            break
        fkey=x.encode('utf-8')
        print(fkey,' -H')
        dec = DES.new(fkey, DES.MODE_CFB, iv)
        ptx = dec.decrypt(ciphertext)
        #print(ptx)
        if ptx == texte:
            print("Found Key: ",fkey)
        i+=1

def decryptGJ():
    i=0
    for x in map(''.join,itertools.product('JabdfhjlnprtvxzABDFHLNPRTVXZ02468!"$&\'(*,.:<>@[\^`{|~',repeat=8)):
        if i ==1000 or x[0] != 'J': 
            break
        fkey=x.encode('utf-8')
        print(fkey,' -J')
        dec = DES.new(fkey, DES.MODE_CFB, iv)
        ptx = dec.decrypt(ciphertext)
        #print(ptx)
        if ptx == texte:
            print("Found Key: ",fkey)
        i+=1

def decryptGL():
    i=0
    for x in map(''.join,itertools.product('LabdfhjlnprtvxzABDFHJNPRTVXZ02468!"$&\'(*,.:<>@[\^`{|~',repeat=8)):
        if i ==1000 or x[0] != 'L': 
            break
        fkey=x.encode('utf-8')
        print(fkey,' -L')
        dec = DES.new(fkey, DES.MODE_CFB, iv)
        ptx = dec.decrypt(ciphertext)
        #print(ptx)
        if ptx == texte:
            print("Found Key: ",fkey)
        i+=1

def decryptGN():
    i=0
    for x in map(''.join,itertools.product('NabdfhjlnprtvxzABDFHJLPRTVXZ02468!"$&\'(*,.:<>@[\^`{|~',repeat=8)):
        if i ==1000 or x[0] != 'N': 
            break
        fkey=x.encode('utf-8')
        print(fkey,' -N')
        dec = DES.new(fkey, DES.MODE_CFB, iv)
        ptx = dec.decrypt(ciphertext)
        #print(ptx)
        if ptx == texte:
            print("Found Key: ",fkey)
        i+=1

def decryptGP():
    i=0
    for x in map(''.join,itertools.product('PabdfhjlnprtvxzABDFHJLNRTVXZ02468!"$&\'(*,.:<>@[\^`{|~',repeat=8)):
        if i ==1000 or x[0] != 'P': 
            break
        fkey=x.encode('utf-8')
        print(fkey,' -P')
        dec = DES.new(fkey, DES.MODE_CFB, iv)
        ptx = dec.decrypt(ciphertext)
        #print(ptx)
        if ptx == texte:
            print("Found Key: ",fkey)
        i+=1

def decryptGR():
    i=0
    for x in map(''.join,itertools.product('RabdfhjlnprtvxzABDFHJLNPTVXZ02468!"$&\'(*,.:<>@[\^`{|~',repeat=8)):
        if i ==1000 or x[0] != 'R': 
            break
        fkey=x.encode('utf-8')
        print(fkey,' -R')
        dec = DES.new(fkey, DES.MODE_CFB, iv)
        ptx = dec.decrypt(ciphertext)
        #print(ptx)
        if ptx == texte:
            print("Found Key: ",fkey)
        i+=1

def decryptGT():
    i=0
    for x in map(''.join,itertools.product('TabdfhjlnprtvxzABDFHJLNPRVXZ02468!"$&\'(*,.:<>@[\^`{|~',repeat=8)):
        if i ==1000 or x[0] != 'T': 
            break
        fkey=x.encode('utf-8')
        print(fkey,' -T')
        dec = DES.new(fkey, DES.MODE_CFB, iv)
        ptx = dec.decrypt(ciphertext)
        #print(ptx)
        if ptx == texte:
            print("Found Key: ",fkey)
        i+=1

def decryptGV():
    i=0
    for x in map(''.join,itertools.product('VabdfhjlnprtvxzABDFHJLNPRTXZ02468!"$&\'(*,.:<>@[\^`{|~',repeat=8)):
        if i ==1000 or x[0] != 'V': 
            break
        fkey=x.encode('utf-8')
        print(fkey,' -V')
        dec = DES.new(fkey, DES.MODE_CFB, iv)
        ptx = dec.decrypt(ciphertext)
        #print(ptx)
        if ptx == texte:
            print("Found Key: ",fkey)
        i+=1

def decryptGX():
    i=0
    for x in map(''.join,itertools.product('XabdfhjlnprtvxzABDFHJLNPRTVZ02468!"$&\'(*,.:<>@[\^`{|~',repeat=8)):
        if i ==1000 or x[0] != 'x': 
            break
        fkey=x.encode('utf-8')
        print(fkey,' -x')
        dec = DES.new(fkey, DES.MODE_CFB, iv)
        ptx = dec.decrypt(ciphertext)
        #print(ptx)
        if ptx == texte:
            print("Found Key: ",fkey)
        i+=1

def decryptGZ():
    i=0
    for x in map(''.join,itertools.product('ZabdfhjlnprtvxzABDFHJLNPRTVX02468!"$&\'(*,.:<>@[\^`{|~',repeat=8)):
        if i ==1000 or x[0] != 'Z': 
            break
        fkey=x.encode('utf-8')
        print(fkey,' -Z')
        dec = DES.new(fkey, DES.MODE_CFB, iv)
        ptx = dec.decrypt(ciphertext)
        #print(ptx)
        if ptx == texte:
            print("Found Key: ",fkey)
        i+=1

def decrypt0():
    i=0
    for x in map(''.join,itertools.product('0abdfhjlnprtvxzABDFHJLNPRTVXZ2468!"$&\'(*,.:<>@[\^`{|~',repeat=8)):
        if i ==1000 or x[0] != '0': 
            break
        fkey=x.encode('utf-8')
        print(fkey,' -0')
        dec = DES.new(fkey, DES.MODE_CFB, iv)
        ptx = dec.decrypt(ciphertext)
        #print(ptx)
        if ptx == texte:
            print("Found Key: ",fkey)
        i+=1

def decrypt2():
    i=0
    for x in map(''.join,itertools.product('2abdfhjlnprtvxzABDFHJLNPRTVXZ0468!"$&\'(*,.:<>@[\^`{|~',repeat=8)):
        if i ==1000 or x[0] != '2': 
            break
        fkey=x.encode('utf-8')
        print(fkey,' -2')
        dec = DES.new(fkey, DES.MODE_CFB, iv)
        ptx = dec.decrypt(ciphertext)
        #print(ptx)
        if ptx == texte:
            print("Found Key: ",fkey)
        i+=1

def decrypt4():
    i=0
    for x in map(''.join,itertools.product('4abdfhjlnprtvxzABDFHJLNPRTVXZ0268!"$&\'(*,.:<>@[\^`{|~',repeat=8)):
        if i ==1000 or x[0] != '4': 
            break
        fkey=x.encode('utf-8')
        print(fkey,' -4')
        dec = DES.new(fkey, DES.MODE_CFB, iv)
        ptx = dec.decrypt(ciphertext)
        #print(ptx)
        if ptx == texte:
            print("Found Key: ",fkey)
        i+=1

def decrypt6():
    i=0
    for x in map(''.join,itertools.product('6abdfhjlnprtvxzABDFHJLNPRTVXZ0248!"$&\'(*,.:<>@[\^`{|~',repeat=8)):
        if i ==1000 or x[0] != '6': 
            break
        fkey=x.encode('utf-8')
        print(fkey,' -6')
        dec = DES.new(fkey, DES.MODE_CFB, iv)
        ptx = dec.decrypt(ciphertext)
        #print(ptx)
        if ptx == texte:
            print("Found Key: ",fkey)
        i+=1

def decrypt8():
    i=0
    for x in map(''.join,itertools.product('8abdfhjlnprtvxzABDFHJLNPRTVXZ0246!"$&\'(*,.:<>@[\^`{|~',repeat=8)):
        if i ==1000 or x[0] != '8': 
            break
        fkey=x.encode('utf-8')
        print(fkey,' -8')
        dec = DES.new(fkey, DES.MODE_CFB, iv)
        ptx = dec.decrypt(ciphertext)
        #print(ptx)
        if ptx == texte:
            print("Found Key: ",fkey)
        i+=1

def decryptex(): #!
    i=0
    for x in map(''.join,itertools.product('!abdfhjlnprtvxzABDFHJLNPRTVXZ02468"$&\'(*,.:<>@[\^`{|~',repeat=8)):
        if i ==1000 or x[0] != '!': 
            break
        fkey=x.encode('utf-8')
        print(fkey,' -!')
        dec = DES.new(fkey, DES.MODE_CFB, iv)
        ptx = dec.decrypt(ciphertext)
        #print(ptx)
        if ptx == texte:
            print("Found Key: ",fkey)
        i+=1

def decryptdq(): #"
    i=0
    for x in map(''.join,itertools.product('"abdfhjlnprtvxzABDFHJLNPRTVXZ02468!$&\'(*,.:<>@[\^`{|~',repeat=8)):
        if i ==1000 or x[0] != '"': 
            break
        fkey=x.encode('utf-8')
        print(fkey,' -"')
        dec = DES.new(fkey, DES.MODE_CFB, iv)
        ptx = dec.decrypt(ciphertext)
        #print(ptx)
        if ptx == texte:
            print("Found Key: ",fkey)
        i+=1

def decryptdol(): #$
    i=0
    for x in map(''.join,itertools.product('$abdfhjlnprtvxzABDFHJLNPRTVXZ02468!"&\'(*,.:<>@[\^`{|~',repeat=8)):
        if i ==1000 or x[0] != '$': 
            break
        fkey=x.encode('utf-8')
        print(fkey,' -$')
        dec = DES.new(fkey, DES.MODE_CFB, iv)
        ptx = dec.decrypt(ciphertext)
        #print(ptx)
        if ptx == texte:
            print("Found Key: ",fkey)
        i+=1


def decryptes(): #&
    i=0
    for x in map(''.join,itertools.product('&abdfhjlnprtvxzABDFHJLNPRTVXZ02468!"$\'(*,.:<>@[\^`{|~',repeat=8)):
        if i ==1000 or x[0] != '&': 
            break
        fkey=x.encode('utf-8')
        print(fkey,' -&')
        dec = DES.new(fkey, DES.MODE_CFB, iv)
        ptx = dec.decrypt(ciphertext)
        #print(ptx)
        if ptx == texte:
            print("Found Key: ",fkey)
        i+=1

def decryptasq(): #'
    i=0
    for x in map(''.join,itertools.product('\'abdfhjlnprtvxzABDFHJLNPRTVXZ02468!"$&(*,.:<>@[\^`{|~',repeat=8)):
        if i ==1000 or x[0] != '\'': 
            break
        fkey=x.encode('utf-8')
        print(fkey,' -\'')
        dec = DES.new(fkey, DES.MODE_CFB, iv)
        ptx = dec.decrypt(ciphertext)
        #print(ptx)
        if ptx == texte:
            print("Found Key: ",fkey)
        i+=1

def decryptpo(): #(
    i=0
    for x in map(''.join,itertools.product('(abdfhjlnprtvxzABDFHJLNPRTVXZ02468!"$&\'*,.:<>@[\^`{|~',repeat=8)):
        if i ==1000 or x[0] != '(': 
            break
        fkey=x.encode('utf-8')
        print(fkey,' -(')
        dec = DES.new(fkey, DES.MODE_CFB, iv)
        ptx = dec.decrypt(ciphertext)
        #print(ptx)
        if ptx == texte:
            print("Found Key: ",fkey)
        i+=1

def decryptast(): #*
    i=0
    for x in map(''.join,itertools.product('*abdfhjlnprtvxzABDFHJLNPRTVXZ02468!"$&\'(,.:<>@[\^`{|~',repeat=8)):
        if i ==1000 or x[0] != '*': 
            break
        fkey=x.encode('utf-8')
        print(fkey,' -*')
        dec = DES.new(fkey, DES.MODE_CFB, iv)
        ptx = dec.decrypt(ciphertext)
        #print(ptx)
        if ptx == texte:
            print("Found Key: ",fkey)
        i+=1

def decryptcom(): #,
    i=0
    for x in map(''.join,itertools.product(',abdfhjlnprtvxzABDFHJLNPRTVXZ02468!"$&\'(*.:<>@[\^`{|~',repeat=8)):
        if i ==1000 or x[0] != ',': 
            break
        fkey=x.encode('utf-8')
        print(fkey,' -,')
        dec = DES.new(fkey, DES.MODE_CFB, iv)
        ptx = dec.decrypt(ciphertext)
        #print(ptx)
        if ptx == texte:
            print("Found Key: ",fkey)
        i+=1

def decryptpoin(): #.
    i=0
    for x in map(''.join,itertools.product('.abdfhjlnprtvxzABDFHJLNPRTVXZ02468!"$&\'(*,:<>@[\^`{|~',repeat=8)):
        if i ==1000 or x[0] != '.': 
            break
        fkey=x.encode('utf-8')
        print(fkey,' -.')
        dec = DES.new(fkey, DES.MODE_CFB, iv)
        ptx = dec.decrypt(ciphertext)
        #print(ptx)
        if ptx == texte:
            print("Found Key: ",fkey)
        i+=1

def decryptdpoi(): #:
    i=0
    for x in map(''.join,itertools.product(':abdfhjlnprtvxzABDFHJLNPRTVXZ02468!"$&\'(*,.<>@[\^`{|~',repeat=8)):
        if i ==1000 or x[0] != ':': 
            break
        fkey=x.encode('utf-8')
        print(fkey,' -:')
        dec = DES.new(fkey, DES.MODE_CFB, iv)
        ptx = dec.decrypt(ciphertext)
        #print(ptx)
        if ptx == texte:
            print("Found Key: ",fkey)
        i+=1

def decryptmo(): #<
    i=0
    for x in map(''.join,itertools.product('<abdfhjlnprtvxzABDFHJLNPRTVXZ02468!"$&\'(*,.:>@[\^`{|~',repeat=8)):
        if i ==1000 or x[0] != '<': 
            break
        fkey=x.encode('utf-8')
        print(fkey,' -<')
        dec = DES.new(fkey, DES.MODE_CFB, iv)
        ptx = dec.decrypt(ciphertext)
        #print(ptx)
        if ptx == texte:
            print("Found Key: ",fkey)
        i+=1

def decryptmi(): #>
    i=0
    for x in map(''.join,itertools.product('>abdfhjlnprtvxzABDFHJLNPRTVXZ02468!"$&\'(*,.:<@[\^`{|~',repeat=8)):
        if i ==1000 or x[0] != '>': 
            break
        fkey=x.encode('utf-8')
        print(fkey,' ->')
        dec = DES.new(fkey, DES.MODE_CFB, iv)
        ptx = dec.decrypt(ciphertext)
        #print(ptx)
        if ptx == texte:
            print("Found Key: ",fkey)
        i+=1

def decryptat(): #@
    i=0
    for x in map(''.join,itertools.product('@abdfhjlnprtvxzABDFHJLNPRTVXZ02468!"$&\'(*,.:<>[\^`{|~',repeat=8)):
        if i ==1000 or x[0] != '@': 
            break
        fkey=x.encode('utf-8')
        print(fkey,' -@')
        dec = DES.new(fkey, DES.MODE_CFB, iv)
        ptx = dec.decrypt(ciphertext)
        #print(ptx)
        if ptx == texte:
            print("Found Key: ",fkey)
        i+=1

def decryptoc(): #[
    i=0
    for x in map(''.join,itertools.product('[abdfhjlnprtvxzABDFHJLNPRTVXZ02468!"$&\'(*,.:<>@\^`{|~',repeat=8)):
        if i ==1000 or x[0] != '[': 
            break
        fkey=x.encode('utf-8')
        print(fkey,' -[')
        dec = DES.new(fkey, DES.MODE_CFB, iv)
        ptx = dec.decrypt(ciphertext)
        #print(ptx)
        if ptx == texte:
            print("Found Key: ",fkey)
        i+=1

def decryptbs(): #\
    i=0
    for x in map(''.join,itertools.product('\abdfhjlnprtvxzABDFHJLNPRTVXZ02468!"$&\'(*,.:<>@[^`{|~',repeat=8)):
        if i ==1000 or x[0] != '\\': 
            break
        fkey=x.encode('utf-8')
        print(fkey,' -\\')
        dec = DES.new(fkey, DES.MODE_CFB, iv)
        ptx = dec.decrypt(ciphertext)
        #print(ptx)
        if ptx == texte:
            print("Found Key: ",fkey)
        i+=1

def decryptcir(): #^
    i=0
    for x in map(''.join,itertools.product('^abdfhjlnprtvxzABDFHJLNPRTVXZ02468!"$&\'(*,.:<>@[\`{|~',repeat=8)):
        if i ==1000 or x[0] != '^': 
            break
        fkey=x.encode('utf-8')
        print(fkey,' -^')
        dec = DES.new(fkey, DES.MODE_CFB, iv)
        ptx = dec.decrypt(ciphertext)
        #print(ptx)
        if ptx == texte:
            print("Found Key: ",fkey)
        i+=1

def decryptidk(): #`
    i=0
    for x in map(''.join,itertools.product('`abdfhjlnprtvxzABDFHJLNPRTVXZ02468!"$&\'(*,.:<>@[\^`{|~',repeat=8)):
        if i ==1000 or x[0] != '`': 
            break
        fkey=x.encode('utf-8')
        print(fkey,' -`')
        dec = DES.new(fkey, DES.MODE_CFB, iv)
        ptx = dec.decrypt(ciphertext)
        #print(ptx)
        if ptx == texte:
            print("Found Key: ",fkey)
        i+=1

def decryptosc(): #{
    i=0
    for x in map(''.join,itertools.product('{abdfhjlnprtvxzABDFHJLNPRTVXZ02468!"$&\'(*,.:<>@[\^`{|~',repeat=8)):
        if i ==1000 or x[0] != '{': 
            break
        fkey=x.encode('utf-8')
        print(fkey,' -{')
        dec = DES.new(fkey, DES.MODE_CFB, iv)
        ptx = dec.decrypt(ciphertext)
        #print(ptx)
        if ptx == texte:
            print("Found Key: ",fkey)
        i+=1

def decryptss(): #|
    i=0
    for x in map(''.join,itertools.product('|abdfhjlnprtvxzABDFHJLNPRTVXZ02468!"$&\'(*,.:<>@[\^`{~',repeat=8)):
        if i ==1000 or x[0] != '|': 
            break
        fkey=x.encode('utf-8')
        print(fkey,' -|')
        dec = DES.new(fkey, DES.MODE_CFB, iv)
        ptx = dec.decrypt(ciphertext)
        #print(ptx)
        if ptx == texte:
            print("Found Key: ",fkey)
        i+=1

def decrypttild(): #~
    i=0
    for x in map(''.join,itertools.product('~abdfhjlnprtvxzABDFHJLNPRTVXZ02468!"$&\'(*,.:<>@[\^`{|',repeat=8)):
        if i ==1000 or x[0] != '~': 
            break
        fkey=x.encode('utf-8')
        print(fkey,' -~')
        dec = DES.new(fkey, DES.MODE_CFB, iv)
        ptx = dec.decrypt(ciphertext)
        #print(ptx)
        if ptx == texte:
            print("Found Key: ",fkey)
        i+=1

threada = threading.Thread(target=decrypta)
threadb = threading.Thread(target=decryptb)
threadd = threading.Thread(target=decryptd)
threadf = threading.Thread(target=decryptf)
threadh = threading.Thread(target=decrypth)
threadj = threading.Thread(target=decryptj)
threadl = threading.Thread(target=decryptl)
threadn = threading.Thread(target=decryptn)
threadp = threading.Thread(target=decryptp)
threadr = threading.Thread(target=decryptr)
threadt = threading.Thread(target=decryptt)
threadv = threading.Thread(target=decryptv)
threadx = threading.Thread(target=decryptx)
threadz = threading.Thread(target=decryptz)
threadGA = threading.Thread(target=decryptGA)
threadGB = threading.Thread(target=decryptGB)
threadGD = threading.Thread(target=decryptGD)
threadGF = threading.Thread(target=decryptGF)
threadGH = threading.Thread(target=decryptGH)
threadGJ = threading.Thread(target=decryptGJ)
threadGL = threading.Thread(target=decryptGL)
threadGN = threading.Thread(target=decryptGN)
threadGP = threading.Thread(target=decryptGP)
threadGR = threading.Thread(target=decryptGR)
threadGT = threading.Thread(target=decryptGT)
threadGV = threading.Thread(target=decryptGV)
threadGX = threading.Thread(target=decryptGX)
threadGZ = threading.Thread(target=decryptGZ)
thread0 = threading.Thread(target=decrypt0)
thread2 = threading.Thread(target=decrypt2)
thread4 = threading.Thread(target=decrypt4)
thread6 = threading.Thread(target=decrypt6)
thread8 = threading.Thread(target=decrypt8)
threadex = threading.Thread(target=decryptex)
threaddq = threading.Thread(target=decryptdq)
threaddol = threading.Thread(target=decryptdol)
threades = threading.Thread(target=decryptes)
threadsq = threading.Thread(target=decryptasq)
threadpo = threading.Thread(target=decryptpo)
threadast = threading.Thread(target=decryptast)
threadcom = threading.Thread(target=decryptcom)
threadpoin = threading.Thread(target=decryptpoin)
threaddpoi = threading.Thread(target=decryptdpoi)
threadmo = threading.Thread(target=decryptmo)
threadmi = threading.Thread(target=decryptmi)
threadat = threading.Thread(target=decryptat)
threadoc = threading.Thread(target=decryptoc)
threadbs = threading.Thread(target=decryptbs)
threadcir = threading.Thread(target=decryptcir)
threadidk = threading.Thread(target=decryptidk)
threadosc = threading.Thread(target=decryptosc)
threadss = threading.Thread(target=decryptss)
threadtild = threading.Thread(target=decrypttild)

threada.start()
threadb.start()
threadd.start()
threadf.start()
threadh.start()
threadj.start()
threadl.start()
threadn.start()
threadp.start()
threadr.start()
threadt.start()
threadv.start()
threadx.start()
threadz.start()
threadGA.start()
threadGB.start()
threadGD.start()
threadGF.start()
threadGH.start()
threadGJ.start()
threadGL.start()
threadGN.start()
threadGP.start()
threadGR.start()
threadGT.start()
threadGV.start()
threadGX.start()
threadGZ.start()
thread0.start()
thread2.start()
thread4.start()
thread6.start()
thread8.start()
threadex.start()
threaddq.start()
threaddol.start()
threades.start()
threadsq.start()
threadpo.start()
threadast.start()
threadcom.start()
threadpoin.start()
threaddpoi.start()
threadmo.start()
threadmi.start()
threadat.start()
threadoc.start()
threadbs.start()
threadcir.start()
threadidk.start()
threadosc.start()
threadss.start()
threadtild.start()