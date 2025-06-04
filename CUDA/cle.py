import itertools


# Jeu de caractères fourni
charset = "abdfhjlnprtvxzABDFHJLNPRTVXZ02468!\"$&'(*,.:<>@[\\^`{|~"


# Fichier de sortie
with open("cles.txt", "w") as f:
    for combo in itertools.product(charset, repeat=8):
        key = ''.join(combo)
        f.write(key + '\n')
