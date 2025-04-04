import os
import tarfile
import cv2
import numpy as np
from os.path import join, isfile


# Configuration
archive_path = "curated.tar.gz.01"  # Chemin vers votre archive
extract_dir = "curated_data"  # Dossier d'extraction
character_set = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


# 1. Extraction de l'archive
def extract_archive():
    if not os.path.exists(extract_dir):
        os.makedirs(extract_dir)

    try:
        with tarfile.open(archive_path, "r:gz") as tar:
            tar.extractall(path=extract_dir)
        print("Archive extraite avec succès.")
    except Exception as e:
        print(f"Erreur lors de l'extraction: {e}")
        exit()


# 2. Chargement des images
def load_dataset():
    X, y = [], []

    for char in character_set:
        char_code = ord(char)
        char_dir = join(extract_dir, str(char_code))

        if not os.path.isdir(char_dir):
            print(f"Attention: Dossier {char_dir} introuvable. Ignoré.")
            continue

        for file_name in os.listdir(char_dir):
            file_path = join(char_dir, file_name)

            if isfile(file_path):
                img = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
                if img is not None:
                    # Redimensionnement optionnel
                    img = cv2.resize(img, (32, 32), interpolation=cv2.INTER_AREA)
                    X.append(img)
                    y.append(char_code)
                else:
                    print(f"Erreur: Impossible de lire {file_path}")

    # Conversion en tableaux numpy
    X = np.array(X, dtype=np.uint8)
    y = np.array(y, dtype=np.uint8)

    print(f"\nDataset chargé:")
    print(f"- Images: {X.shape} (nombre, hauteur, largeur)")
    print(f"- Labels: {y.shape}")

    return X, y


# Exécution principale
if __name__ == "__main__":
    # 1. Extraire l'archive
    extract_archive()

    # 2. Charger le dataset
    X, y = load_dataset()

    # 3. Exemple d'affichage
    import matplotlib.pyplot as plt

    plt.figure(figsize=(10, 5))
    for i in range(5):
        plt.subplot(1, 5, i + 1)
        plt.imshow(X[i], cmap='gray')
        plt.title(chr(y[i]))
        plt.axis('off')
    plt.show()