# Utilisation de l'image officielle Python comme base
FROM python:3.9-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers du projet dans le conteneur
COPY . /app

# Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Donner les permissions d'exécution aux scripts shell
RUN chmod +x collect/collect_data.sh process/process_data.sh main.sh

# Installer gdown (nécessaire pour collect_data.sh si utilisé)
RUN pip install gdown

# Commande pour lancer uniquement le pipeline via main.sh
CMD ["bash", "./main.sh"]
