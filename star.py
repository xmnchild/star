taille = input("Veuillez saisir une taille : ")
try:
    taille = int(taille)
    if taille < 0:
        print("La valeur doit être positive")
    elif taille == 0:
        print()
    else:
        longueurBrancheHaut = taille * 2 - 1
        longueurBrancheCote = taille * 2 + 1
        longueurLigne = longueurBrancheCote * 2 + longueurBrancheHaut
        marqueEtoile = (longueurBrancheHaut - 1) / 2

        def afficherLigneIntermediaire():
            output = ""
            for colonne in range(0, longueurLigne):
                if ((colonne < (longueurBrancheCote)) or (colonne >= (longueurBrancheCote + longueurBrancheHaut))):
                    output = output + "*"
                else:
                    output = output + " "
            print(output)
        modificateur = 0
        for ligne in range(0, taille):
            output = ""
            for espace in range(0, longueurBrancheCote):
                output = output + " "
            for colonne in range(0, longueurBrancheHaut):
                if ((colonne == marqueEtoile - modificateur) or (colonne == marqueEtoile + modificateur)):
                    output = output + "*"
                else:
                    output = output + " "
            modificateur = modificateur + 1
            print(output)
        afficherLigneIntermediaire()
        modificateur = 1
        for ligne in range(0, taille):
            output = ""
            for colonne in range(0, longueurLigne):
                if ((colonne == modificateur) or (colonne == (longueurLigne - modificateur - 1))):
                    output = output + "*"
                else:
                    output = output + " "
            modificateur = modificateur + 1
            print(output)
        modificateur = marqueEtoile
        for ligne in range(0, taille-1):
            output = ""
            for colonne in range(0, longueurLigne):
                if ((colonne == modificateur) or (colonne == (longueurLigne - modificateur - 1))):
                    output = output + "*"
                else:
                    output = output + " "
            modificateur = modificateur - 1
            print(output)
        afficherLigneIntermediaire()
        modificateur = marqueEtoile
        for ligne in range(0, taille):
            output = ""
            for espace in range(0, longueurBrancheCote):
                output = output + " "
            for colonne in range(0, longueurBrancheHaut):
                if ((colonne == marqueEtoile - modificateur) or (colonne == marqueEtoile + modificateur)):
                    output = output + "*"
                else:
                    output = output + " "
            modificateur = modificateur - 1
            print(output)
except ValueError:
    print("Veuillez saisir un entier positif")
