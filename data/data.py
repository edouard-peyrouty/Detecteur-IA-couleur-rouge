def lire(file):
    try:       
        with open(f"data/{file}.txt","r") as fichier:
            return eval(fichier.read())
    except:
        return False
    
def ecrire(file, contenu):
    with open(f"data/{file}.txt", "w") as fichier:
        fichier.write(str(contenu))
