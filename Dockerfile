# Utilisation de l'image officielle Python comme base
FROM python:3.9-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers du projet dans le conteneur
COPY . /app

# Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Donner les permissions d'exécution aux scripts shell
RUN chmod +x collect/collect_data.sh process/process_data.sh

# Installer gdown (nécessaire pour collect_data.sh si utilisé)
RUN pip install gdown

# Exposer le port de Streamlit
EXPOSE 8501

# Commande par défaut pour exécuter le pipeline et Streamlit
CMD bash -c "./collect/collect_data.sh && ./process/process_data.sh && streamlit run application/app_streamlit.py"
