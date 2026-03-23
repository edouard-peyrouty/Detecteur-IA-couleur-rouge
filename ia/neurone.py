epsilon = 0.2

def activation(p,e):
    '''
    Retourne True si le neurone est activé et False sinon.
    p : est l'état du neurone.
    e : contient les composantes de la couleur.
    ---
    Retourne True si le neurone est activé, False sinon
    '''
    return sum([float(p[i]) * float(e[i]) for i in range(3)]) >= 1

def apprentissage(p,e,b):
    '''
    Apprentissage sur une couleur et 1 objectif.
    p : est l'état courant du neurone.
    e : contient les composantes de la couleur.
    b : est l'obectif (1 si rouge, 0 sinon)
    ---
    p : l'état est modifié selon la règle énoncée.
    '''
    # on teste le neurone sur une entrée
    s = activation(p,e)
    # si le resultat n'est pas celui souhaité on change l'état du neurone
    if s != int(b):
        # on change l'état différement en fonction du cas
        if s == 0:
            p = [p[i] + epsilon * e[i] for i in range(3)]
        else:
           p = [p[i] - epsilon * e[i] for i in range(3)]
    # on renvoie le nouvel état
    return p 
        
def epoque_apprentissage(neurone_init,liste_entrees_objectifs):
    '''
    Phase d'apprentissage pour l'ensemble des couleurs.
    neurone_init : contient l'état initial du neurone
    liste_entrees_objectifs : contient la liste des couleurs avec leur objectif
    ---
    Retourne l'état du neurone après l'apprentissage sur toutes les couleurs
    '''
    neurone = neurone_init
    # on apprend le neurone sur chacune des entrées de la liste
    for entree,objectif in liste_entrees_objectifs:
        neurone = apprentissage(neurone,entree,objectif)
    return neurone

def ecart(p1,p2):
    '''
    Retourne l'écart entre deux états successifs du neurones.
    p1 : état précédent du neurone.
    p2 : état courant du neurone.
    ---
    Retourne l'écart quadratique entre p1 et p2
    '''
    return sum([(p1[i] - p2[i])**2 for i in range(3)])