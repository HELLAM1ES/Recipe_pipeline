FROM python:3.9-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier tout le projet
COPY . .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Donner les permissions d'exécution aux scripts shell
RUN chmod +x collect/collect_data.sh process/process_data.sh

# Installer gdown pour collect_data.sh
RUN pip install gdown

# Exposer le port de Streamlit
EXPOSE 8501

# Commande pour exécuter tout le pipeline
CMD bash main.sh
