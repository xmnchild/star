taille = input("Veuillez saisir une taille : ")

try:
    taille = int(taille)

    if taille < 0:
        print("La valeur doit être positive")
    elif taille == 0 :
        #ne rien afficher
        print()
    else :

        longueurBrancheHaut = taille * 2 - 1 #définit la largeur de la branche en haut (-1) pour gérer le input de 1 par l'utilisateur et pour tomber tjrs sur une largeur impaire pour faire le pic 
        longueurBrancheCote = taille * 2 + 1 #définit la largeur des branches de côté
        longueurLigne = longueurBrancheCote * 2 + longueurBrancheHaut #définit la largeur totale de l'étoile 

        marqueEtoile = (longueurBrancheHaut - 1) / 2 #permet de savoir où placer les pics des branches hautes et basses

        def afficherLigneIntermediaire():
            output = "" #utilisation de outpout a la place de print pour accelerer le processus
            for colonne in range(0, longueurLigne):
                if( (colonne < (longueurBrancheCote)) or (colonne >= (longueurBrancheCote + longueurBrancheHaut)) ):
                    output = output + "*"
                else:
                    output = output + " "
            print(output)

        # branche haute
        modificateur = 0
        for ligne in range(0, taille):
            output = ""
            # ajout espaces à gauche
            for espace in range(0, longueurBrancheCote):
                output = output + " "
            # ajout des *
            for colonne in range(0, longueurBrancheHaut):
                if((colonne == marqueEtoile - modificateur) or (colonne == marqueEtoile + modificateur)):
                    output = output + "*"
                else:
                    output = output + " "
            modificateur = modificateur + 1        
            print(output)

        # ligne intermédiaire haute
        afficherLigneIntermediaire()

        #branches côtés supérieures
        modificateur = 1
        for ligne in range(0, taille):
            output = ""
            for colonne in range (0, longueurLigne):
                if ((colonne==modificateur) or ( colonne ==(longueurLigne - modificateur -1) ) ):
                    output = output + "*"
                else:
                    output = output + " "
            modificateur = modificateur + 1    
            print(output)
            
        #branches côtés inférieures
        modificateur = marqueEtoile
        for ligne in range(0, taille-1):
            output = ""
            for colonne in range (0, longueurLigne):
                if ((colonne==modificateur) or ( colonne ==(longueurLigne - modificateur -1) ) ):
                    output = output + "*"
                else:
                    output = output + " "
            modificateur = modificateur - 1    
            print(output)
            
        # ligne intermédiaire basse
        afficherLigneIntermediaire()

        # branche basse
        modificateur = marqueEtoile
        for ligne in range(0, taille):
            output = ""
            # ajout espaces à gauche
            for espace in range(0, longueurBrancheCote):
                output = output + " "
            # ajout des *
            for colonne in range(0, longueurBrancheHaut):
                if((colonne == marqueEtoile - modificateur) or (colonne == marqueEtoile + modificateur)):
                    output = output + "*"
                else:
                    output = output + " "
            modificateur = modificateur - 1        
            print(output)

    
except ValueError:
    print("Veuillez saisir un entier positif")



    


