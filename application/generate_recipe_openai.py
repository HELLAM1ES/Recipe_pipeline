import openai

# Configurez votre clé API OpenAI
openai.api_key = "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"

def ask_user_preferences():
    """
    Pose des questions à l'utilisateur pour personnaliser la recette.
    :return: Dictionnaire contenant les préférences de l'utilisateur.
    """
    print("Bienvenue dans le générateur de recettes personnalisées !\n")
    
    # Posez les questions à l'utilisateur
    num_people = input("Pour combien de personnes souhaitez-vous cuisiner ? ")
    healthy = input("Voulez-vous une recette healthy ? (oui/non) ").strip().lower() == "oui"
    vegetarian = input("Préférez-vous une recette végétarienne ? (oui/non) ").strip().lower() == "oui"
    main_type = input("Préférez-vous de la viande, du poisson, ou autre ? (viande/poisson/autre) ").strip().lower()
    sweet_or_savory = input("Voulez-vous une recette sucrée ou salée ? (sucrée/salée) ").strip().lower()

    # Retournez les préférences sous forme de dictionnaire
    return {
        "num_people": num_people,
        "healthy": healthy,
        "vegetarian": vegetarian,
        "main_type": main_type,
        "sweet_or_savory": sweet_or_savory
    }

def generate_recipe(preferences):
    """
    Génère une recette en fonction des préférences de l'utilisateur.
    :param preferences: Dictionnaire des préférences.
    :return: Recette générée sous forme de texte.
    """
    # Construire le prompt basé sur les préférences
    healthy_text = "healthy" if preferences["healthy"] else "gourmande"
    vegetarian_text = "végétarienne" if preferences["vegetarian"] else f"avec {preferences['main_type']}"
    
    prompt = (
        f"Créer une recette {healthy_text}, {preferences['sweet_or_savory']} et {vegetarian_text} "
        f"pour {preferences['num_people']} personnes.\n\n"
        "La recette doit inclure :\n"
        "- Un titre clair pour la recette\n"
        "- Une liste d'ingrédients\n"
        "- Des étapes détaillées et numérotées pour préparer le plat\n"
        "Merci de formater la réponse comme suit :\n"
        "Titre : [Nom de la recette]\n"
        "Ingrédients :\n"
        "- [Ingrédient 1]\n"
        "- [Ingrédient 2]\n"
        "Étapes :\n"
        "1. Première étape\n"
        "2. Deuxième étape\n"
        "3. Troisième étape\n"
    )

    try:
        # Appel à l'API OpenAI
        response = openai.ChatCompletion.create(
            model="gpt-4-turbo",  # Utilisez le modèle GPT-4 Turbo
            messages=[
                {"role": "system", "content": "You are a helpful assistant specialized in creating recipes."},
                {"role": "user", "content": prompt},
            ],
            max_tokens=512,
            temperature=0.7
        )
        # Retourner le texte généré
        return response['choices'][0]['message']['content'].strip()
    
    except Exception as e:
        return f"Erreur lors de la génération de la recette : {e}"

if __name__ == "__main__":
    # Posez les questions à l'utilisateur
    preferences = ask_user_preferences()
    
    # Générez la recette en fonction des réponses
    print("\nGénération de la recette en cours...\n")
    recipe = generate_recipe(preferences)
    
    # Affichez la recette générée
    print("\nRecette générée :\n")
    print(recipe)
