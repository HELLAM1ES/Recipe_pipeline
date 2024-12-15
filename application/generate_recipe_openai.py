import openai

# Configurez votre clé API OpenAI
openai.api_key = "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"


def ask_user_preferences():
    """
    Pose des questions à l'utilisateur pour personnaliser la recette.
    :return: Dictionnaire contenant les préférences de l'utilisateur.
    """
    print("Bienvenue dans le générateur de recettes personnalisées !\n")
    
    # Questions de base
    num_people = input("Pour combien de personnes souhaitez-vous cuisiner ? ")
    healthy = input("Voulez-vous une recette healthy ? (oui/non) ").strip().lower() == "oui"
    vegetarian = input("Préférez-vous une recette végétarienne ? (oui/non) ").strip().lower() == "oui"

    # Type de recette (dynamique)
    if vegetarian:
        main_type = "végétarienne"
    else:
        main_type = input("Préférez-vous de la viande, du poisson, ou autre ? (viande/poisson/autre) ").strip().lower()

    # Saveur
    sweet_or_savory = input("Voulez-vous une recette sucrée ou salée ? (sucrée/salée) ").strip().lower()

    # Temps de préparation
    prep_time = input("Combien de temps avez-vous pour cuisiner ? (moins de 15 min, 30 min, 1 heure, etc.) ").strip()

    # Équipements
    equipment = input("Quels équipements avez-vous ? (four, mixeur, plaque de cuisson, etc.) ").strip()

    # Allergies
    allergies = input("Avez-vous des allergies ou des ingrédients à éviter ? (séparés par des virgules) ").strip()

    # Budget
    budget = input("Quel est votre budget pour les ingrédients ? (en euros) ").strip()

    # Retour des préférences sous forme de dictionnaire
    return {
        "num_people": num_people,
        "healthy": healthy,
        "vegetarian": vegetarian,
        "main_type": main_type,
        "sweet_or_savory": sweet_or_savory,
        "prep_time": prep_time,
        "equipment": equipment,
        "allergies": allergies,
        "budget": budget
    }


def generate_recipe(preferences):
    """
    Génère une recette personnalisée en fonction des préférences utilisateur.
    """
    # Construction du prompt basé sur les clés du dictionnaire preferences
    prompt = (
        f"Créer une recette {preferences['flavor']} pour un {preferences['dish_type']}. "
        f"Inclure les ingrédients suivants : {preferences['include_ingredients']} "
        f"et exclure les ingrédients suivants : {preferences['exclude_ingredients']}. "
        f"Le régime alimentaire doit être {preferences['dietary_preferences']}. "
        f"Le budget maximal est de {preferences['budget']} euros.\n\n"
        "La recette doit inclure :\n"
        "- Un titre\n"
        "- Une liste d'ingrédients\n"
        "- Des étapes claires et numérotées pour préparer le plat."
    )

    # Appel fictif à OpenAI pour illustration
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4-turbo",
            messages=[
                {"role": "system", "content": "Tu es un assistant culinaire expert en recettes."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=500,
            temperature=0.7
        )

        # Retourne la recette générée
        return response['choices'][0]['message']['content'].strip()

    except Exception as e:
        return f"Erreur lors de la génération de la recette : {e}"

