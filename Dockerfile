# Utiliser une image légère basée sur Python
FROM python:3.9-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier tous les fichiers dans le conteneur
COPY . /app

# Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Donner les permissions d'exécution aux scripts shell
RUN chmod +x collect_data.sh process_data.sh

# Installer gdown (utilisé dans collect_data.sh)
RUN pip install gdown

# Exposer le port utilisé par Streamlit
EXPOSE 8501

# Commande par défaut pour exécuter le pipeline et Streamlit
CMD bash -c "./collect_data.sh && ./process_data.sh && streamlit run application/app_streamlit.py --server.port=8501 --server.headless=true"
