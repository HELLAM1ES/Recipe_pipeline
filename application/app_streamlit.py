import os
import streamlit as st
import base64
import pandas as pd
from generate_recipe_openai import generate_recipe  # Assurez-vous que ce fichier est correctement configuré
from recipe_finder import filter_recipes_by_ingredients

# Configuration de la page Streamlit
st.set_page_config(
    page_title="Clicook",
    page_icon="🍴",
    layout="wide",
)


# Définir le chemin absolu vers le dossier `assets` et le fichier CSV
ASSETS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../assets"))
CSV_FILE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../data/cleaned_recipes.csv"))

# CSS personnalisé

def inject_css():
    st.markdown(
        """
        <style>
        /* Global styles */
        body {
            font-family: 'Arial', sans-serif;
            background-color: #f8f9fa;
        }

        /* Navbar */
        .navbar {
            background-color: #2c3e50;
            padding: 15px 0;
            display: flex;
            justify-content: space-around;
            align-items: center;
            font-family: Arial, sans-serif;
            color: white;
        }

        .navbar a {
            text-decoration: none;
            color: white;
            font-weight: bold;
            padding: 10px 20px;
            transition: color 0.3s ease-in-out;
        }

        .navbar a:hover {
            color: #18bc9c;
        }

        /* Footer */
        .footer {
            background-color: #2c3e50;
            color: white;
            padding: 30px 0;
            display: flex;
            justify-content: space-around;
            flex-wrap: wrap;
            margin-top: 50px;
        }

        .footer-section h4 {
            color: #18bc9c;
            margin-bottom: 10px;
        }

        .footer-section a {
            color: white;
            text-decoration: none;
            display: block;
            margin-bottom: 5px;
            font-size: 0.9rem;
        }

        .footer-section a:hover {
            text-decoration: underline;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

# Inject CSS
inject_css()


# Barre de navigation
def render_navbar():
    st.markdown(
        """
        <div class="navbar">
            <a href="?page=home">Accueil</a>
            <a href="?page=about_us">Qui sommes-nous</a>
            <a href="?page=ia_choice">Générer avec IA</a>
            <a href="?page=csv_search">Recherche dans CSV</a>
            <a href="?page=guide">Guide</a>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Pied de page
def render_footer():
    st.markdown(
        """
        <div class="footer">
            <div class="footer-section">
                <h4>A propos</h4>
                <a href="#">Notre mission</a>
                <a href="#">Besoin d'aide ?</a>
                <a href="#">Plan de site</a>
            </div>
            <div class="footer-section">
                <h4>L'équipe Clicook</h4>
                <a href="#">Partenariats</a>
                <a href="#">Presse</a>
            </div>
            <div class="footer-section">
                <h4>Suivez-nous</h4>
                <a href="#"><img src="https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png" alt="Instagram" width="30"></a>
                <a href="#"><img src="https://upload.wikimedia.org/wikipedia/commons/4/44/Facebook_Logo.png" alt="Facebook" width="30"></a>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


# Fonction pour charger une image avec gestion des erreurs
def get_image(image_name):
    try:
        image_path = os.path.join(ASSETS_DIR, image_name)
        return image_path
    except Exception as e:
        st.error(f"Erreur : {e}")
        return None

# Page d'accueil
def home_page():
    render_navbar()
    st.title("Bienvenue sur Clicook")
    st.markdown("Votre assistant culinaire propulsé par l'IA et vos idées.")

    # Vérifier et afficher les icônes
    ia_image = get_image("icone_IA.png")
    csv_image = get_image("icone_base.png")

    if ia_image and csv_image:
        st.markdown(
            f"""
            <div style="display: flex; justify-content: space-around; margin: 50px 0;">
                <a href="?page=ia_choice">
                    <img src="data:image/png;base64,{base64.b64encode(open(ia_image, 'rb').read()).decode()}" style="width: 150px; height: 150px;" />
                    <p style="text-align: center;">Générer avec IA</p>
                </a>
                <a href="?page=csv_search">
                    <img src="data:image/png;base64,{base64.b64encode(open(csv_image, 'rb').read()).decode()}" style="width: 150px; height: 150px;" />
                    <p style="text-align: center;">Recherche dans CSV</p>
                </a>
            </div>
            """,
            unsafe_allow_html=True,
        )

    render_footer()

# Page "Qui sommes-nous"
def about_us_page():
    render_navbar()
    st.title("Qui sommes-nous ?")
    image_path = get_image("nous.jpg")

    if image_path:
    	st.image(image_path, caption="L'équipe Clicook", use_container_width=True)



    st.write(
 """

    ### **L'histoire de Clicook**
    Bienvenue chez **Clicook**, une initiative née de l'imagination et de la passion de trois étudiantes en Mastère **MOSEF** à Paris :  
    **Charlotte**, **Chirine** et **Hella**. Issues de parcours académiques divers – entre sciences de l'ingénieur, intelligence artificielle et gestion de projets – nous nous sommes réunies autour d'une ambition commune :  
    **transformer la cuisine du quotidien grâce à la technologie**.  

    Tout a commencé lors de nos études, où la rigueur des cours, les projets interminables et les deadlines serrées laissaient peu de temps pour préparer des repas équilibrés.  
    Comme beaucoup d'étudiants et de jeunes actifs, nous avons souvent été confrontées à des choix alimentaires rapides mais peu satisfaisants.  
    C'est dans ce contexte que l'idée de **Clicook** a germé :  
    *"Et si l'intelligence artificielle pouvait nous aider à mieux cuisiner, plus rapidement et avec les ingrédients déjà disponibles dans notre cuisine ?"*

    ---

    ### **Pourquoi Clicook ?**  
    En tant qu'étudiantes, nous connaissons les défis quotidiens liés à la préparation des repas :  
    - **Manque de temps** pour cuisiner entre les cours et les obligations.  
    - **Absence d'inspiration** lorsqu'il s'agit d'imaginer des recettes.  
    - **Budget limité**, qui rend l'optimisation des courses essentielle.  

    **Clicook** est né pour offrir une **solution innovante** :  
    des recettes **personnalisées, rapides et adaptées à vos besoins.**

    ---

    ### **Ce que nous proposons**  
    Avec **Clicook**, bénéficiez de deux outils puissants :  

    - 🧠 **Une intelligence artificielle** capable de générer des recettes personnalisées selon vos préférences alimentaires, votre budget et vos équipements.  
    - 🔎 **Un moteur de recherche** intuitif qui vous permet de trouver des recettes adaptées aux ingrédients que vous avez déjà chez vous.  

    Ensemble, ces fonctionnalités vous permettent de cuisiner **sans stress, sans gaspillage et en toute simplicité**.

    ---

    ### **Nos valeurs**  
    - 🚀 **Innovation** : Tirer parti des dernières avancées technologiques pour révolutionner votre expérience culinaire.  
    - 👩‍🍳 **Accessibilité** : Permettre à tout le monde, quel que soit son niveau en cuisine, de préparer des plats délicieux.  
    - 🌍 **Écologie** : Réduire le gaspillage alimentaire en utilisant ce que vous avez déjà dans votre réfrigérateur.  
    - 🤝 **Communauté** : Créer un espace d'échange et de partage autour de la passion de la cuisine.

    ---

    ### **Notre mission**  
    Chez **Clicook**, notre ambition est simple :  
    **Faire de la cuisine une expérience facile, agréable et innovante pour tous.**  

    Que vous soyez :  
    - Un **étudiant occupé** en quête de repas rapides,  
    - Un **parent débordé** cherchant des solutions simples,  
    - Ou un **amateur de cuisine** à la recherche de nouvelles inspirations,  

    **Clicook est fait pour vous !**  

    En combinant **technologie** et **créativité culinaire**, nous voulons vous accompagner dans chaque étape de la préparation de vos repas.

    ---

    ### **Rejoignez-nous !**  
    🚀 Rejoignez l'aventure **Clicook** dès aujourd'hui :  
    - Découvrez comment l'IA peut transformer vos habitudes culinaires.  
    - Partagez vos retours et vos recettes avec notre communauté grandissante.  

    Ensemble, redécouvrons le **plaisir de cuisiner**, en alliant **innovation, simplicité et saveur**. 🍽️✨  
    
        
        """
    )
    render_footer()

# Page : Générer avec IA

def ia_choice_page():
    """
    Page Streamlit pour générer une recette avec l'IA.
    """
    render_navbar()
    st.title("Générer une recette avec l'IA 🍽️")

    # Collecte des préférences de l'utilisateur
    st.write("### Vos préférences culinaires")

    # Type de plat
    dish_type = st.selectbox(
        "Quel type de plat souhaitez-vous ?",
        ["Entrée", "Plat principal", "Dessert", "Boisson"]
    )

    # Préférence de saveurs
    flavor = st.radio(
        "Préférence de saveurs :",
        ["Sucrée", "Salée", "Épicée", "Acide"]
    )

    # Ingrédients spécifiques
    include_ingredients = st.text_input(
        "Ingrédients à inclure (ex : tomate, poulet, chocolat) :", ""
    )

    exclude_ingredients = st.text_input(
        "Ingrédients à éviter (ex : gluten, lactose) :", ""
    )

    # Régime alimentaire
    dietary_preferences = st.radio(
        "Suivez-vous un régime spécifique ?",
        ["Aucun", "Végétarien", "Vegan", "Sans gluten"]
    )

    # Budget
    budget = st.slider(
        "Quel est votre budget en euros pour les ingrédients ?",
        5, 100, 20
    )

    # Vérification des incohérences
    if dietary_preferences in ["Végétarien", "Vegan"] and "viande" in include_ingredients.lower():
        st.warning("⚠️ Vous avez sélectionné un régime végétarien/vegan. La viande n'est pas autorisée.")
        include_ingredients = ""

    # Bouton pour générer la recette
    if st.button("Générer ma recette 🚀"):
        st.info("Génération de la recette en cours...")

        # Création du dictionnaire des préférences
        preferences = {
            "dish_type": dish_type,
            "flavor": flavor,
            "include_ingredients": include_ingredients,
            "exclude_ingredients": exclude_ingredients,
            "dietary_preferences": dietary_preferences,
            "budget": budget
        }

        # Appel de la fonction generate_recipe
        try:
            recipe = generate_recipe(preferences)
            st.success("🎉 Voici votre recette personnalisée :")
            st.markdown(recipe)  # Affiche la recette générée en markdown
        except Exception as e:
            st.error(f"❌ Erreur lors de la génération de la recette : {e}")

    render_footer()


# Page : Recherche dans CSV

def csv_search_page():
    render_navbar()
    st.title("🔎 Recherche de recettes dans la base CSV")

    # Options pour la recherche
    include_ingredients = st.text_input("📝 Ingrédients à inclure (séparés par des virgules) :")
    exclude_ingredients = st.text_input("❌ Ingrédients à exclure (séparés par des virgules) :")
    max_ingredients = st.number_input("🔢 Nombre maximal d'ingrédients dans la recette :", min_value=1, step=1, value=10)

    if st.button("Rechercher"):
        try:
            # Filtrer les recettes
            recipes = filter_recipes_by_ingredients(CSV_FILE_PATH, include_ingredients, exclude_ingredients, max_ingredients)

            # Afficher les recettes trouvées
            if recipes.empty:
                st.warning("Aucune recette ne correspond aux critères sélectionnés.")
            else:
                st.success(f"{len(recipes)} recette(s) trouvée(s) :")
                for _, row in recipes.iterrows():
                    # Titre stylisé de la recette
                    st.markdown(
                        f"""
                        <div style='
                            background-color: #FFFAE6; 
                            padding: 10px; 
                            border-radius: 5px; 
                            margin-top: 10px; 
                            box-shadow: 0px 2px 5px rgba(0,0,0,0.1);'
                        >
                            <h3 style='color: #2C3E50; text-align: center;'>{row['title']}</h3>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                    # Affichage des ingrédients sous forme de liste propre
                    st.markdown("**🛒 Ingrédients :**")
                    ingredients = eval(row['ingredients'])  # Convertir la chaîne en liste
                    for ingredient in ingredients:  # Afficher chaque élément proprement
                        st.markdown(f"- {ingredient}")

                    # Affichage des instructions sous forme de texte continu
                    st.markdown("**👨‍🍳 Instructions :**")
                    instructions = eval(row['directions'])  # Convertir en liste
                    instructions_text = " ".join(instructions)  # Fusionner les étapes
                    st.write(instructions_text)

                    # Ligne de séparation entre les recettes
                    st.markdown("---")

        except Exception as e:
            st.error(f"Erreur lors de la recherche : {e}")

    render_footer()

# Page Guide

def guide_page():
    render_navbar()
    st.title("Guide d'utilisation de Clicook 🚀")

    st.markdown("""
    ## Bienvenue dans le guide d'utilisation de **Clicook** 🍽️  
    Voici tout ce que vous devez savoir pour tirer le meilleur parti de notre application culinaire :

    ---

    ### 🔎 **Recherche dans le CSV**  
    - Entrez les ingrédients que vous **avez** dans le champ *"Ingrédients à inclure"*.  
    - Si vous souhaitez **éviter certains ingrédients**, renseignez-les dans le champ *"Ingrédients à exclure"*.  
    - Vous pouvez aussi **limiter** le nombre maximal d'ingrédients pour des recettes simples.  
    - Cliquez sur **Rechercher** pour voir les recettes correspondantes.

    #### Exemple :  
    - **Ingrédients à inclure** : *poulet, tomate*  
    - **Ingrédients à exclure** : *lactose*  
    - **Nombre maximal d'ingrédients** : *5*  

    Vous obtiendrez des recettes rapides et adaptées à votre cuisine !

    ---

    ### 🧠 **Génération de recette avec IA**  
    - Sélectionnez le **type de plat** : *entrée, plat principal, dessert ou boisson*.  
    - Indiquez vos **saveurs préférées** : *sucrée, salée, épicée ou acide*.  
    - Ajoutez les **ingrédients spécifiques** que vous souhaitez inclure ou éviter.  
    - Précisez votre **régime alimentaire** : *aucun, végétarien, vegan, sans gluten*.  
    - Fixez votre **budget** pour optimiser vos dépenses.  

    Cliquez sur **"Générer ma recette"** pour obtenir une recette personnalisée créée par notre IA.

    #### Exemple :  
    - **Type de plat** : *Plat principal*  
    - **Saveurs** : *Salée*  
    - **Ingrédients à inclure** : *poulet, riz*  
    - **Budget** : *15 euros*  

    L'IA vous proposera une recette savoureuse en quelques secondes.

    ---

    ### 👨‍🍳 **Astuce Cuisine**  
    - **Utilisez les filtres intelligemment** pour trouver des recettes simples avec peu d'ingrédients.  
    - **Explorez** les différentes saveurs pour des repas variés et équilibrés.  
    - **Ajoutez des équipements** disponibles dans l'application pour des suggestions adaptées à votre matériel.

    ---

    ### 🎯 **Rejoignez-nous sur les réseaux sociaux !**  
    Suivez-nous pour plus d'astuces, d'inspirations et pour partager vos propres créations culinaires :  
    - 📸 [Instagram](#)  
    - 👍 [Facebook](#)  

    Merci de choisir **Clicook** ! Ensemble, réinventons le plaisir de cuisiner. 🍲  
    """, unsafe_allow_html=True)

    render_footer()


# Gestion des pages
page = st.query_params.get("page", "home")

if page == "home":
    home_page()
elif page == "about_us":
    about_us_page()
elif page == "ia_choice":
    ia_choice_page()
elif page == "csv_search":
    csv_search_page()
elif page == "guide":
    guide_page()
