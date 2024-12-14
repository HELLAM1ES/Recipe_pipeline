#!/bin/bash

echo "=== Démarrage complet du pipeline ==="

# Étape 1 : Collecte des données
echo "Étape 1 : Collecte des données avec collect_data.sh..."
if bash /app/collect_data.sh; then
    echo "Données collectées avec succès."
else
    echo "Erreur : Échec de la collecte des données."
    exit 1
fi

# Étape 2 : Nettoyage des données
echo "Étape 2 : Nettoyage des données avec process_data.sh..."
if bash /app/process_data.sh; then
    echo "Données nettoyées avec succès."
else
    echo "Erreur : Échec du nettoyage des données."
    exit 1
fi

# Étape 3 : Lancement de Streamlit
echo "Étape 3 : Lancement de l'application Streamlit..."
if streamlit run /app/app_streamlit.py; then
    echo "Application Streamlit lancée avec succès."
else
    echo "Erreur : Échec du lancement de Streamlit."
    exit 1
fi
