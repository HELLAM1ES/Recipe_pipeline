# **Clicook - Votre assistant culinaire propulsé par l'IA 🍴**

Bienvenue sur **Clicook**, une application interactive qui génère des recettes personnalisées grâce à l'intelligence artificielle et permet la recherche de recettes via un fichier CSV. Conçue pour les étudiants, parents ou amateurs de cuisine, **Clicook** simplifie votre quotidien en cuisine.

---

## **🛠 Prérequis**

Avant de commencer, assurez-vous d'avoir installé les outils suivants sur votre machine :

- **Git** : pour cloner le projet.
- **Docker** : pour exécuter le projet dans un conteneur.
- **Python 3.9+** (si vous souhaitez exécuter le projet manuellement sans Docker).

---

## **🚀 Installation**

### **Option 1 : Cloner le projet via GitHub**

1. **Clonez le projet depuis GitHub :**
   ```bash
   git clone https://github.com/HELLAM1ES/recipe_pipeline.git
   cd recipe_pipeline
   ```

2. **Construisez l'image Docker :**
   ```bash
   docker build -t clicook-app .
   ```

3. **Exécutez le conteneur Docker :**
   ```bash
   docker run -p 8501:8501 clicook-app
   ```

4. **Accédez à l'application dans votre navigateur :**
   ```
   http://localhost:8501
   ```

---

### **Option 2 : Via Docker Hub**

1. **Récupérez l'image Docker directement depuis Docker Hub :**
   ```bash
   docker pull HELLAM1ES/clicook-app:latest
   ```

2. **Exécutez le conteneur Docker :**
   ```bash
   docker run -p 8501:8501 HELLAM1ES/clicook-app:latest
   ```

3. **Accédez à l'application dans votre navigateur :**
   ```
   http://localhost:8501
   ```

---

## **📄 Fonctionnalités**

### 1. **Génération de recettes avec l'IA 🤖**
Personnalisez vos recettes en fonction de :
   - **Type de plat** : entrée, plat principal, dessert ou boisson.
   - **Saveurs préférées** : sucrée, salée, épicée ou acide.
   - **Ingrédients à inclure ou à éviter**.
   - **Régime alimentaire** : végétarien, vegan, sans gluten, etc.
   - **Budget**, **nombre de portions**, et **équipements disponibles**.

---

### 2. **Recherche dans les recettes 📊**
Trouvez des recettes adaptées grâce au moteur de recherche basé sur vos ingrédients :
   - **Ingrédients à inclure**.
   - **Nombre maximum d'ingrédients** pour la recette.
   - Résultats affichés avec des titres améliorés et instructions claires.

---

### 3. **"Qui sommes-nous ?" et Guide ℹ️**
   - Découvrez l'équipe derrière **Clicook**.
   - Consultez le guide pour apprendre à utiliser l'application.

---

## **🛠 Exécution manuelle sans Docker**

Si vous préférez exécuter le projet sans Docker, suivez ces étapes :

1. **Clonez le projet :**
   ```bash
   git clone https://github.com/HELLAM1ES/recipe_pipeline.git
   cd recipe_pipeline
   ```

2. **Créez un environnement virtuel et activez-le :**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Sur Linux/Mac
   venv\Scripts\activate     # Sur Windows
   ```

3. **Installez les dépendances Python :**
   ```bash
   pip install -r requirements.txt
   ```

4. **Lancez l'application Streamlit :**
   ```bash
   streamlit run application/app_streamlit.py
   ```

5. **Accédez à l'application :**
   ```
   http://localhost:8501
   ```

---

## **🔑 Configuration des clés API**

Si vous utilisez l'IA (OpenAI), créez un fichier `.env` dans le répertoire principal du projet avec le contenu suivant :

```bash
OPENAI_API_KEY=VOTRE_CLE_API
```

**Remarque** : Remplacez `VOTRE_CLE_API` par votre clé API OpenAI.

---
## 📁 Structure du projet

```plaintext
recipe_pipeline/
│
├── application/               # Contient les scripts Streamlit pour l'interface utilisateur
│   ├── app_streamlit.py       # Script principal pour lancer l'application Streamlit
│   └── generate_recipe_openai.py  # Génération de recettes via OpenAI API
│
├── collect/                   # Scripts pour collecter les données
│   └── collect_data.sh        # Télécharge les données depuis Google Drive
│
├── process/                   # Scripts pour nettoyer les données
│   └── process_data.py        # Nettoie les données brutes et les prépare
│
├── data/                      # Contient les fichiers de données (non inclus dans Git)
│   ├── recipes.csv            # Données brutes téléchargées (générées)
│   └── cleaned_recipes.csv    # Données nettoyées (générées)
│
├── assets/                    # Ressources visuelles pour l'application
│   ├── icone_IA.png           # Icône pour l'IA
│   ├── icone_base.png         # Icône pour la recherche dans CSV
│   └── nous.jpg               # Image de l'équipe Clicook
│
├── Dockerfile                 # Fichier Docker pour containeriser l'application
├── main.sh                    # Script pour exécuter tout le pipeline (collecte, nettoyage et application)
├── requirements.txt           # Dépendances Python pour exécuter l'application
└── README.md                  # Documentation du projet

## **🛀 Nettoyage des conteneurs Docker**

Si vous souhaitez arrêter ou supprimer les conteneurs Docker après usage :

1. **Listez les conteneurs en cours d'exécution :**
   ```bash
   docker ps
   ```

2. **Arrêtez un conteneur :**
   ```bash
   docker stop <ID_DU_CONTENEUR>
   ```

3. **Supprimez un conteneur :**
   ```bash
   docker rm <ID_DU_CONTENEUR>
   ```

---

## **👥 Contributeurs**

- **Charlotte**, **Chirine**, et **Hella**  
- **Projet développé dans le cadre du Mastère MOOSEF à Paris.**

---

## **📩 Contact**

Pour toute question, suggestion ou collaboration, contactez-nous :  
📧 **votre.email@example.com**

---

## **📝 Licence**

Ce projet est sous licence **MIT**.
