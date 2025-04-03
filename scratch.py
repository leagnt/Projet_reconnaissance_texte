#!/usr/bin/env python3
import os
import shutil

# Chemin du dossier principal qui contient les sous-dossiers à traiter
main_dir = '/Users/bramouk/Documents/GitHub/Projet_reconnaissance_texte/DataSetCreator/handwritting/curated_data/curated'  # <-- Modifie ce chemin

# Chemin du dossier unique de destination
destination_dir = '/Users/bramouk/Documents/GitHub/Projet_reconnaissance_texte/DataSetCreator/handwritting/curated_data/curated2'  # <-- Modifie ce chemin
os.makedirs(destination_dir, exist_ok=True)

# Liste des extensions d'image autorisées (en minuscule)
allowed_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'}

# Parcours des sous-dossiers du dossier principal
for item in os.listdir(main_dir):
    subfolder_path = os.path.join(main_dir, item)
    if os.path.isdir(subfolder_path):
        try:
            # Conversion du nom de dossier en entier et soustraction de 33
            folder_num = int(item)
            new_prefix = str(folder_num - 33)
        except ValueError:
            # Si le nom du dossier n'est pas un chiffre, on passe
            print(f"Le dossier {item} n'est pas un chiffre, il est ignoré.")
            continue

        # Parcours des fichiers dans le sous-dossier
        for file_name in os.listdir(subfolder_path):
            # Vérifie que c'est un fichier et qu'il a une extension d'image
            file_path = os.path.join(subfolder_path, file_name)
            if os.path.isfile(file_path) and os.path.splitext(file_name)[1].lower() in allowed_extensions:
                # Création du nouveau nom avec le préfixe
                new_name = f"{new_prefix}_{file_name}"
                dest_path = os.path.join(destination_dir, new_name)

                # En cas de conflit (fichier déjà existant), on ajoute un compteur
                counter = 1
                while os.path.exists(dest_path):
                    new_name = f"{new_prefix}_{counter}_{file_name}"
                    dest_path = os.path.join(destination_dir, new_name)
                    counter += 1

                # Déplace le fichier vers le dossier de destination
                shutil.move(file_path, dest_path)
                print(f"Déplacé: {file_path} -> {dest_path}")

print("Opération terminée.")

