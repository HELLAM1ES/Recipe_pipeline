# Clicook: Votre assistant culinaire intelligent

Clicook est une application alimentée par l'intelligence artificielle, conçue pour simplifier la création et la recherche de recettes. Grâce à des intégrations comme OpenAI, elle génère des recettes personnalisées ou vous aide à rechercher dans des bases de données CSV.

---

## **Fonctionnalités**

- **Génération de recettes avec IA** : Spécifiez vos préférences (végétarien, healthy, etc.) et laissez l'IA créer une recette.
- **Recherche dans les données CSV** : Entrez vos ingrédients et trouvez des recettes correspondantes.
- **Exécution complète via Docker** : Collecte, nettoyage des données et lancement de l'application.

---

## **Prérequis**

Avant de commencer, assurez-vous d'avoir les éléments suivants installés :
- [Docker](https://docs.docker.com/get-docker/)
- Un compte OpenAI et une clé API (à placer dans un fichier `.env`).

---

## **Installation et Exécution**

### **1. Clonez le projet**
```bash
git clone https://github.com/<votre-nom-utilisateur>/recipe_pipeline.git
cd recipe_pipeline
