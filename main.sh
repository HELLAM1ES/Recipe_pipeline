#!/bin/bash

echo "=== Démarrage complet du pipeline ==="

# Étape 1 : Collecte des données
echo "Étape 1 : Collecte des données avec collect/collect_data.sh..."
bash collect/collect_data.sh
if [ $? -ne 0 ]; then
    echo "Erreur : Échec de la collecte des données."
    exit 1
fi
echo "Données collectées avec succès."

# Étape 2 : Nettoyage des données
echo "Étape 2 : Nettoyage des données avec process/process_data.sh..."
bash process/process_data.sh
if [ $? -ne 0 ]; then
    echo "Erreur : Échec du nettoyage des données."
    exit 1
fi
echo "Données nettoyées avec succès."

# Étape 3 : Lancement de l'application Streamlit
echo "Étape 3 : Lancement de l'application Streamlit..."
streamlit run application/app_streamlit.py

echo "Pipeline terminé avec succès."
