####################
##  VISI210 : Visite de laboratoire
##  La suite de Conway et la classification periodique des "éléments".
##  Yohann THEPAUT - CMI Informatique
####################
##  Objectifs :
##
##  1. Comprendre les enoncés du théoreme "chimique", "arithmetique" et "cosmologique". Comprendre la preuve du premier.
##  2. Programmer la suite de Conway pour retrouver la classification des "atomes". Retrouver leurs numéros et abondance.
##  3. Ecrire un programme pour calculer experimentalement une approximation de la constante "lambda".
##  4. Ecrire un programme pour calculer la suite de Robinson.
####################

import time


## Fonctions qui calculent les suites de Conway et de Robinson ##


def termeSuivant(terme):
    """Fonction qui retourne le terme suivant de la suite de Conway.
    Entrée : Chaîne de caractères ;
    Sortie : Chaîne de caractères ;"""

    nouveauTerme = ""
    c_actuel = terme[0]
    c_compte = 0

    for c in terme:

        if (c != c_actuel):
            nouveauTerme += str(c_compte) + c_actuel
            c_actuel = c
            c_compte = 1
        else:
            c_compte += 1

    nouveauTerme += str(c_compte) + c_actuel
        
    return nouveauTerme



def conway(n,premierTerme = "1",afficher = True):
    """Fonction qui affiche, puis retourne la suite de Conway jusqu'à un rang n.
    Entrée : n: Entier ; premietTerme (option): Chaîne de caractère ; afficher (option): Booléen ;
    Sortie : Tableau de chaînes de caractère"""

    terme = premierTerme
    resultat = [""] * n
    
    for i in range(0,n):

        resultat[i] = terme

        if (afficher):
            print(terme)

        terme = termeSuivant(terme)

    return resultat



def termeSuivantRobinson(terme):
    """Fonction qui retourne le terme suivant de la suite de Robinson.
    Entrée : Chaîne de caractères ;
    Sortie : Chaîne de caractères ;"""

    resultat = ""
    maximum = 0

    for c in terme:

        c = int(c)

        if (c > maximum):

            maximum = c

    for i in range(maximum, -1, -1):

        compte = 0
        
        for c in terme:

            if (int(c) == i):

                compte += 1
        if (compte != 0):
            resultat += str(compte) + str(i)

    return resultat
            
            
    
def robinson(n,premierTerme = "0",afficher = True):
    """Fonction qui affiche, puis retourne la suite de Robinson jusqu'à un rang n.
    Entrée : n: Entier ; premietTerme (option): Chaîne de caractère ; afficher (option): Booléen ;
    Sortie : Tableau de chaînes de caractère"""

    terme = premierTerme
    resultat = [""] * n
    
    for i in range(0,n):

        resultat[i] = terme

        if (afficher):
            print(terme)

        terme = termeSuivantRobinson(terme)

    return resultat



## Fonctions de tests sur les suites ##


def trouverLambda(n, tps = False):
    """Fonction qui "trouve" la constante lambda.
    Entrée : n = Entier ; tps (option) = Booléen ;
    Sortie : Flottant."""

    tpsDepart = time.time()

    suite = conway(n,afficher = False)

    Ln = len(suite[len(suite) - 2])
    Ln1 = len(suite[len(suite) - 1])

    csteLambda = Ln1 / Ln

    if (tps):

        print("Temps de traitement :",time.time()-tpsDepart)
    

    return csteLambda



def trouverBoucle(premierTerme="0"):
    """Fonction qui trouve à quel rang la suite de Robinson boucle.
    Entrée : premierTerme (option): Chaîne de caractères ;
    Sortie : Tuple d'entiers. (prépreiode,periode)"""
    
    robinson = [premierTerme]
    dernierTerme = premierTerme
    
    i = 0   #Rang a partir duquel la suite boucle : préperiode
    j = 0   #Taille de la boucle : periode

    while (chaineDansListe(dernierTerme,robinson[:len(robinson) - 1]) == -1):   #Tant que le dernier terme n'est pas dans la suite
        
        robinson += [termeSuivantRobinson(dernierTerme)]

        dernierTerme = robinson[len(robinson) - 1]

        i += 1

    j = i - chaineDansListe(dernierTerme,robinson[:len(robinson) - 1])
    
    return (i,j + 1)


def chaineDansListe(chaine,liste):
    """Fonction qui retourne si une chaine de caractères se trouve dans une liste de chaîne de caractères.
    Entrée : chaine: Chaîne de caractères; liste: Liste de chaînes de caractères ;
    Sortie : Eniter (Rang trouvé)."""

    trouve = False
    i = 0

    while (not trouve and i < len(liste)):

        elt = liste[i]
        if (chaine == elt):
            trouve = True

        i += 1

    if (not trouve):
        i = -1

    return i



## Fonctions en cours de developpement pour retrouver la classification periodique des elements. ##



#def chaineCompriseDansListe(chaine,liste):
#    """Fonction qui retourne si une chaine de caractères se trouve dans un element d'une liste.
#    Entrée : chaine: Chaîne de caractères; liste: Liste de chaînes de caractères ;
#    Sortie : Booléen."""
#
#    trouve = False
#    i = 0
#
#    while (not trouve and i < len(liste)):
#
#        elt = liste[i]
#        if (chaine in elt):
#            trouve = True
#
#        i += 1
#
#    if (not trouve):
#        res = False
#    else:
#        res = True
#
#    return res




noms_atomes = ['U','Pa','Th','Ac','Ra','Fr','Rn','At','Po','Bi','Pb','Tl','Hg','Au','Pt','Ir','Os','Re','W','Ta','Hf','Lu','Yb','Tm','Er','Ho','Dy','Tb','Gd','Eu','Sm','Pm','Nd','Pr','Ce','La','Ba','Cs','Xe','I','Te','Sb','Sn','In','Cd','Ag','Pd','Rh','Ru','Tc','Mo','Nb','Zr','Y','Sr','Rb','Kr','Br','Se','As','Ge','Ga','Zn','Cu','Ni','Co','Fe','Mn','Cr','V','Ti','Sc','Ca','K','Ar','Cl','S','P','Si','Al','Mg','Na','Ne','F','O','N','C','B','Be','Li','He','H']

def traduction():
    """Fonction qui va traduire un terme de la suite vers des elements du tableau periodique.
    Entrée : Vide ;
    Sortie : Dictionnaire."""

    
    dico = construireDico()
    
    fichier = open('Elementsconway50.txt', 'r')
    suite = fichier.readlines()
    fichier.close()

    fichier = open('Traduction50.txt','a')
    
    for i in range(0,len(suite)):
        elt = suite[i][:len(suite[i])-1]

        for k,v in dico.items():
            elt = elt.replace(v,noms_atomes[k])  #Replacer par les elements du tableau periodique
            
        fichier.write(elt + '\n')

    fichier.close()



def couper(chaine,i,afficher = False):
    """Fonction qui retourne si l'on peut couper la chaîne en i. (cf. Splitting Theorem)
    Entrée : chaine: chaîne de caractères ; i: entier ; afficher (option): Booléen
    Sortie : Booléen."""

    #On peut couper chaine en L et R si :
    #   L ou R vide (on ne traitera pas ce cas).
    #   ou
    #   L       R
    #   n]      [m
    #   2]      [1X     ou      [111    ou      [3X^n, n!=3      ou      [n^1
    #   !=2]    [221X   ou      [22111  ou      [223X^n, n!=3    ou      [22n^(0 ou 1)
    #
    #   n >= 4 et m <= 3

    resultat = False

    L = chaine[i-1]     #Dernier chiffre de L
    R = chaine[i:]

    R += 'NNNNNNNN'     #Eviter les erreurs si R[j] n'existe pas.

    if (int(L) >= 4 and int(R[0]) <= 3):    #Cas 1 : n] [m
        resultat = True
        debug = '[DEBUG] Split = 1'
        
    elif (L == '2' and (R[1] != 'N' and R[0] == '1' and R[1] != R[0] and R[2] != R[1])):    #Cas 2a : 2] [1X
        resultat = True
        debug = '[DEBUG] Split = 2a'
        
    elif (L == '2' and (R[0:3] == '111' and R[3] != '1')):   #Cas 2b : 2] [111
        resultat = True
        debug = '[DEBUG] Split = 2b'
        
    elif (L == '2' and (R[0] == '3' and R[1] != '3')):      #Cas 2c : 2] [3X^n, n!=3
        X = R[1]
        j = 1
        while (R[j] == X and j < 5):
            j+=1
            
        if (j-1 != 3):
            resultat = True
            debug = '[DEBUG] Split = 2c'
        else:
            debug = '[DEBUG] Split = None'

    elif (L == '2' and (R[0] != 'N' and R[0] != R[1] and int(R[0]) >= 4)):      #Cas 2d : 2] [n^1
        resultat = True
        debug = '[DEBUG] Split = 2d'

    elif (L != '2' and (R[0:3] == '221' and R[3] != 'N' and R[2] != '1' and R[3] != R[4])):      #Cas 3a : !=2] [221X
        resultat = True
        debug = '[DEBUG] Split = 3a'

    elif (L != '2' and (R[0:5] == '22111' and R[5] != '1')):        #Cas 3b : !=2] [22111
        resultat = True
        debug = '[DEBUG] Split = 3b'

    elif (L != '2' and (R[0:3] == '223' and R[3] != '3')):          #Cas 3c : !=2] [223X^n, n!=3, X!=3
        X = R[3]
        j = 3
        while (R[j] == X and j < 8):
            j+=1
            
        if (j-3 != 3):
            resultat = True
            debug = '[DEBUG] Split = 3c'
        else:
            debug = '[DEBUG] Split = None'

    elif (L != '2' and (R[0:2] == '22' and R[2] != '2' and (R[2] == 'N' or R[2] != R[3] and int(R[2]) >= 4))):   #Cas 3d : !=2] [22n^(0 ou 1)
        resultat = True
        debug = '[DEBUG] Split = 3d'
        
    else:
        debug = '[DEBUG] Split = None'

    if (afficher):
        print(debug)

    return resultat


def estAtome(terme):
    """Fonction qui permet de dire si un terme est un atome.
    Entrée : Chaîne de caractères ;
    Sortie : Booléen."""

    
    resultat = True

    i = 1
    while (i < len(terme) and resultat):
        if (couper(terme,i)):
            resultat = False
        i+=1

    return resultat


def decoupage(terme,recursive = True):
    """Fonction qui découpe un terme en plusieurs élements.
    Entrée : terme: Chaîne de caractères ; recursive (option): Booléen ;
    Sortie : Tableau(x) de chaînes de caractères."""

    resultat = []

    dernier_decoupage = 0
    
    for i in range(1,len(terme)):

        if (couper(terme,i)):

            resultat += [terme[dernier_decoupage:i]]
            dernier_decoupage = i

    resultat += [terme[dernier_decoupage:len(terme)]]

    if (recursive):
        resrec = []
        resultat_total = []
        for j in resultat:

            if estAtome(j):
                resrec += [j]
            else:
                resrec += [decoupage(j,True)]

        resultat_total += resrec

        return resultat_total
    else:
        return resultat


def construireDico():
    """Fonction qui va contruire le dictionnaire des atomes avec leur valeur correspondante.
    Entrée : Vide ;
    Sortie : Dictionnaire de listes de chaînes de caractères."""


    dico = {}
    j = 0

    fichier = open('Elementsconway30.txt', 'r')
    suite = fichier.readlines()
    fichier.close()

    for i in range(0,len(suite)):
        elt = suite[i][:len(suite[i])-1]


        if estAtome(elt):
            dico[noms_atomes[i]] = [elt]
        else:
            composes = decoupage(elt,recursive=False)
            dico[noms_atomes[i]] = composes

        print(str(i) + '/' + str(len(suite)-1))
    return dico


def dejaPresent(dico,chaine):
    """Fonction qui retourne si une chaîne d'une liste du dictionnaire est déjà présent 2 fois dans une autre liste du dictionnaire. (Utilisé pour le traitement du dico.)
    Entrée : dico: Dictionnaire de listes de chaînes de caractères ; chaine: Chaîne de caractères.
    Sortie : Booléen."""

    i = 0
    trouve = False
    compte = 0
    liste_cles = list(dico)
    
    while (not trouve and i < len(dico.items())):
        k = liste_cles[i]  #Clé
        v = dico[k]  #Valeur

        j=0
        while (not trouve and j<len(v)):
            if v[j] == chaine:
                compte += 1
            j+=1

        i+=1
        
        if (compte >= 2):
            trouve = True

    return trouve
        

def traitementDico():
    """Fonction qui va créer le dictionnaire des atomes sans les composés.
    Entrée : Vide ;
    Sortie : Dictionnaire de chaînes de caractères."""
    #Ne fonctionne pas

    dico = construireDico()
    resultat = {}

    for k,v in dico.items():
        if (len(v) == 1):
            resultat[k] = v[0]
        else:
            i = 0
            for elt in v:
                if not dejaPresent(dico,elt):
                    resultat[k] = v[i]
                elif (i == len(v)-1):
                    print('pas de correspondance')
                i+=1

    return resultat




















