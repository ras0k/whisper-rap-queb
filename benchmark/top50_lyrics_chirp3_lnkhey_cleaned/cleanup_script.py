import re
from pathlib import Path

def nettoyer_fichiers_txt():
    # Définir le dossier courant (là où le script est exécuté)
    dossier_courant = Path('.')

    # Expression régulière pour trouver tout ce qui est entre [ et ]
    # Le '?' rend la recherche non-gourmande pour éviter de tout supprimer s'il y a plusieurs crochets sur une ligne
    pattern_crochets = re.compile(r'\[.*?\]')

    compteur_fichiers = 0

    # Parcourir tous les fichiers .txt du dossier
    for chemin_fichier in dossier_courant.glob('*.txt'):
        # Lire le contenu du fichier
        with open(chemin_fichier, 'r', encoding='utf-8') as fichier:
            lignes = fichier.readlines()

        lignes_nettoyees = []
        for ligne in lignes:
            # 1. Supprimer les crochets et leur contenu
            ligne_sans_crochets = pattern_crochets.sub('', ligne)

            # 2. Vérifier si la ligne n'est pas vide (strip enlève les espaces et sauts de ligne invisibles)
            if ligne_sans_crochets.strip():
                # Ajouter la ligne nettoyée avec un saut de ligne propre
                lignes_nettoyees.append(ligne_sans_crochets.strip() + '\n')

        # Écraser l'ancien fichier avec le nouveau contenu
        with open(chemin_fichier, 'w', encoding='utf-8') as fichier:
            fichier.writelines(lignes_nettoyees)

        compteur_fichiers += 1
        print(f"Nettoyé : {chemin_fichier.name}")

    print(f"\nTerminé ! {compteur_fichiers} fichier(s) traité(s).")

if __name__ == '__main__':
    # AVERTISSEMENT : Ce script modifie les fichiers de manière permanente.
    # Assurez-vous d'avoir une copie de sauvegarde de vos fichiers .txt avant de l'exécuter.
    nettoyer_fichiers_txt()
