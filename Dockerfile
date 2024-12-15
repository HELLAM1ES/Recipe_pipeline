# Utilisation de l'image officielle Python comme base
FROM python:3.9-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier tous les fichiers et dossiers nécessaires dans le conteneur
COPY . /app

# Donner les permissions d'exécution à tous les scripts dans l'ensemble du projet
RUN chmod -R +x /app

# Installer les dépendances Python nécessaires
RUN pip install --no-cache-dir -r requirements.txt

# Exposer le port pour Streamlit
EXPOSE 8501

# Commande par défaut pour exécuter le pipeline complet
CMD ["bash", "main.sh"]
