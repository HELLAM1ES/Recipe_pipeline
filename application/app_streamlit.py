import os
import streamlit as st
import base64
import pandas as pd
from generate_recipe_openai import generate_recipe  # Assurez-vous que ce fichier est correctement configuré

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
        st.image(image_path, caption="L'équipe Clicook", use_column_width=True)
    st.write(
 """
        ### L'histoire de Clicook
        Nous sommes **Charlotte**, **Chirine**, et **Hella**, trois étudiantes passionnées en Mastère MOOSEF à Paris. 
        Issues de parcours académiques variés, nous partageons deux grandes passions : **l'intelligence artificielle** et **la cuisine**.  
        
        ### Pourquoi Clicook ?
        En tant qu'étudiantes, nous savons combien il peut être difficile de trouver le temps de cuisiner des repas sains, équilibrés et délicieux 
        tout en jonglant avec les cours, les projets et les deadlines. Clicook est né de ce besoin : une **solution innovante** pour répondre aux 
        défis de la vie quotidienne en matière de cuisine.

        ### Ce que nous proposons
        Avec **Clicook**, nous voulons simplifier l'art de cuisiner grâce à deux outils principaux :
        - Une **intelligence artificielle** capable de générer des recettes personnalisées adaptées à vos préférences alimentaires.
        - Un moteur de recherche performant pour explorer des milliers de recettes en fonction des ingrédients que vous avez sous la main.

        ### Nos valeurs
        - **Innovation** : Tirer parti des dernières technologies pour révolutionner votre expérience culinaire.
        - **Accessibilité** : Permettre à tout le monde, même sans expérience en cuisine, de préparer des plats délicieux.
        - **Écologie** : Réduire le gaspillage alimentaire en utilisant ce que vous avez déjà chez vous.

        ### Notre mission
        Clicook, c'est plus qu'une simple application : c'est une **communauté** qui valorise l'ingéniosité culinaire et la technologie pour 
        vous accompagner dans la préparation de vos repas. Que vous soyez un étudiant occupé, un parent débordé ou un amateur de cuisine, 
        **Clicook est fait pour vous !**

        ### Rejoignez-nous !
        Ensemble, redécouvrons le plaisir de cuisiner, en combinant **innovation** et **simplicité**.

        ---
        """
    )
    render_footer()

# Page : Générer avec IA
def ia_choice_page():
    render_navbar()
    st.title("Générer une recette avec l'IA")
    num_people = st.number_input("Pour combien de personnes ?", min_value=1, value=2)
    healthy = st.radio("Healthy ?", ["Oui", "Non"])
    vegetarian = st.radio("Végétarien ?", ["Oui", "Non"])
    sweet_or_savory = st.radio("Sucré ou salé ?", ["Sucré", "Salé"])
    if st.button("Générer"):
        with st.spinner("Génération de recette en cours..."):
            preferences = {
                "num_people": num_people,
                "healthy": healthy == "Oui",
                "vegetarian": vegetarian == "Oui",
                "sweet_or_savory": sweet_or_savory.lower(),
            }
            recipe = generate_recipe(preferences)
            st.success("Votre recette générée :")
            st.text_area("Recette complète", recipe, height=300)
    render_footer()

# Page : Recherche dans CSV
def csv_search_page():
    render_navbar()
    st.title("Recherche dans les données CSV")
    ingredients = st.text_input("Entrez vos ingrédients, séparés par des virgules :")
    if st.button("Rechercher"):
        try:
            data = pd.read_csv(CSV_FILE_PATH)
            search_ingredients = [i.strip().lower() for i in ingredients.split(",")]

            def contains_all_ingredients(row):
                return all(ingredient in row["ingredients"].lower() for ingredient in search_ingredients)

            filtered_data = data[data.apply(contains_all_ingredients, axis=1)]
            if filtered_data.empty:
                st.warning("Aucune recette trouvée.")
            else:
                for _, row in filtered_data.iterrows():
                    st.subheader(row["title"])
                    st.write(f"Ingrédients : {row['ingredients']}")
                    st.write(f"Instructions : {row['directions']}")
                    st.markdown("---")
        except Exception as e:
            st.error(f"Erreur lors du chargement des données : {e}")
    render_footer()

# Gestion des pages
page = st.experimental_get_query_params().get("page", ["home"])[0]

if page == "home":
    home_page()
elif page == "about_us":
    about_us_page()
elif page == "ia_choice":
    ia_choice_page()
elif page == "csv_search":
    csv_search_page()

