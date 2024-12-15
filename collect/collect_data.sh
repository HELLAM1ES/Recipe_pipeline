#!/bin/bash

# Définir le chemin absolu vers le répertoire parent pour garantir les bonnes références
BASE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

# Chemin du fichier à télécharger
FILE_PATH="$BASE_DIR/data/recipes.csv"

# Créer le dossier pour stocker les données
mkdir -p "$BASE_DIR/data"

# Vérifier si le fichier existe déjà
if [ -f "$FILE_PATH" ]; then
    echo "Le fichier recipes.csv existe déjà dans ./data. Téléchargement non nécessaire."
    exit 0
fi

# Télécharger le fichier depuis Google Drive
echo "Téléchargement du fichier recipes.csv depuis Google Drive..."
gdown --id 1dxNK8ihNTUkWz6YG9W5yoo7xxidGXWUG -O "$FILE_PATH"

# Vérifier si le fichier a été téléchargé avec succès
if [ -f "$FILE_PATH" ]; then
    echo "Les données ont été téléchargées avec succès dans $FILE_PATH."
else
    echo "Erreur : Le fichier recipes.csv n'a pas été téléchargé."
    exit 1
fi

# Vérifier la taille du fichier pour s'assurer qu'il n'est pas vide ou corrompu
if [ ! -s "$FILE_PATH" ]; then
    echo "Erreur : Le fichier recipes.csv est vide ou corrompu."
    exit 1
fi

echo "Téléchargement terminé avec succès."
