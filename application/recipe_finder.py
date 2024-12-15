import pandas as pd

def filter_recipes_by_ingredients(csv_file_path, include_ingredients, exclude_ingredients, max_ingredients=None):
    """
    Filtre les recettes à partir des ingrédients inclus/exclus et d'une limite sur le nombre d'ingrédients.

    :param csv_file_path: Chemin vers le fichier CSV contenant les recettes.
    :param include_ingredients: Liste d'ingrédients à inclure.
    :param exclude_ingredients: Liste d'ingrédients à exclure.
    :param max_ingredients: Nombre maximal d'ingrédients pour la recette.
    :return: DataFrame filtré des recettes.
    """
    try:
        # Charger les données depuis le fichier CSV
        data = pd.read_csv(csv_file_path)
        
        # Prétraitement des colonnes
        data['ingredients'] = data['ingredients'].fillna("").str.lower()
        
        # Appliquer les filtres d'inclusion
        if include_ingredients:
            include_ingredients = [i.strip().lower() for i in include_ingredients.split(",")]
            data = data[data['ingredients'].apply(lambda x: all(ingredient in x for ingredient in include_ingredients))]

        # Appliquer les filtres d'exclusion
        if exclude_ingredients:
            exclude_ingredients = [i.strip().lower() for i in exclude_ingredients.split(",")]
            data = data[~data['ingredients'].apply(lambda x: any(ingredient in x for ingredient in exclude_ingredients))]

        # Appliquer la limite du nombre d'ingrédients
        if max_ingredients:
            data = data[data['ingredients'].apply(lambda x: len(x.split(',')) <= max_ingredients)]

        return data

    except Exception as e:
        raise Exception(f"Erreur lors du filtrage des recettes : {e}")
