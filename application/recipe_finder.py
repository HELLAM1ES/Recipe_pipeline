import pandas as pd

# Chemin vers les données nettoyées
DATA_FILE = './data/cleaned_recipes.csv'

def load_data():
    """
    Charger les données nettoyées depuis le fichier CSV.
    """
    df = pd.read_csv(DATA_FILE)
    df['ingredients'] = df['ingredients'].apply(eval)  # Convertir les chaînes en listes Python
    df['NER'] = df['NER'].apply(eval)  # Convertir les chaînes en listes Python
    return df

def find_recipes(df, ingredients_list):
    """
    Trouver des recettes qui contiennent tous les ingrédients donnés.
    """
    # Filtrer les recettes qui contiennent tous les ingrédients de la liste
    matched_recipes = df[df['NER'].apply(lambda x: all(ingredient in x for ingredient in ingredients_list))]
    return matched_recipes

def main():
    # Charger les données
    print("Chargement des données nettoyées...")
    recipes_df = load_data()

    print("\nBienvenue dans le moteur de recherche de recettes !")
    print("Entrez une liste d'ingrédients pour trouver des recettes correspondantes.")
    print("Exemple : sugar, butter, vanilla\n")

    # Demander les ingrédients à l'utilisateur
    user_input = input("Entrez vos ingrédients, séparés par des virgules : ").strip()

    if user_input:
        # Transformer l'entrée utilisateur en liste d'ingrédients
        ingredients_list = [ingredient.strip().lower() for ingredient in user_input.split(",")]

        # Rechercher des recettes
        matched_recipes = find_recipes(recipes_df, ingredients_list)

        # Afficher les résultats
        if not matched_recipes.empty:
            print(f"\nRecettes trouvées ({len(matched_recipes)} résultat(s)) :\n")
            for index, row in matched_recipes.head(5).iterrows():
                print(f"- {row['title']}")
                print(f"  Ingrédients : {', '.join(row['ingredients'])}")
                print(f"  Instructions : {row['directions']}")
                print(f"  Lien : {row['link']}\n")
        else:
            print("\nAucune recette trouvée avec tous les ingrédients donnés.")
    else:
        print("\nVous n'avez pas entré d'ingrédients. Veuillez réessayer.")

if __name__ == "__main__":
    main()
