#!/bin/bash

# Définir les chemins des fichiers
INPUT_FILE="data/recipes.csv"
OUTPUT_FILE="data/cleaned_recipes.csv"
SCRIPT_FILE="process/process_data.py"

# Vérifier si le fichier nettoyé existe déjà
if [ -f "$OUTPUT_FILE" ]; then
    echo "Le fichier nettoyé $OUTPUT_FILE existe déjà. Nettoyage non nécessaire."
    exit 0
fi

# Vérifier si le script Python existe
if [ ! -f "$SCRIPT_FILE" ]; then
    echo "Erreur : Le script Python $SCRIPT_FILE est introuvable."
    exit 1
fi

# Si le fichier nettoyé n'existe pas, lancer le script Python
echo "Nettoyage des données en cours..."
python3 "$SCRIPT_FILE"

# Vérification de la réussite du nettoyage
if [ $? -eq 0 ]; then
    echo "Les données ont été nettoyées avec succès."
else
    echo "Erreur : Échec du nettoyage des données."
    exit 1
fi
