import pandas as pd
import os

# Définir le chemin absolu vers le répertoire parent pour garantir des références correctes
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
input_file = os.path.join(BASE_DIR, 'data', 'recipes.csv')
output_file = os.path.join(BASE_DIR, 'data', 'cleaned_recipes.csv')

def clean_recipes():
    """
    Charger les données brutes, les nettoyer et enregistrer dans un nouveau fichier.
    """
    # Vérifier si le fichier nettoyé existe déjà
    if os.path.exists(output_file):
        print(f"Le fichier nettoyé {output_file} existe déjà. Nettoyage non nécessaire.")
        return

    print(f"Chargement des données depuis {input_file}...")

    # Charger les données dans un DataFrame
    try:
        df = pd.read_csv(input_file)
    except FileNotFoundError:
        raise FileNotFoundError(f"Le fichier d'entrée est introuvable : {input_file}")

    # Vérifier que les colonnes essentielles sont présentes
    required_columns = ["title", "ingredients", "directions", "NER"]
    missing_columns = [col for col in required_columns if col not in df.columns]
    if missing_columns:
        raise ValueError(f"Les colonnes suivantes sont absentes du fichier CSV : {missing_columns}")

    # Nettoyage des données
    df = df.dropna(subset=required_columns).drop_duplicates()
    try:
        df['ingredients'] = df['ingredients'].apply(eval)  # Convertir les chaînes en listes Python
        df['NER'] = df['NER'].apply(eval)  # Convertir les chaînes en listes Python
    except Exception as e:
        raise ValueError(f"Erreur lors de la conversion des colonnes 'ingredients' ou 'NER' : {e}")

    # Enregistrer les données nettoyées dans un fichier CSV
    try:
        df.to_csv(output_file, index=False)
        print(f"Données nettoyées enregistrées dans {output_file}")
    except PermissionError:
        raise PermissionError(f"Impossible d'écrire dans le fichier de sortie : {output_file}")

    # Afficher un aperçu des 5 premières lignes
    print("\nAperçu des données nettoyées (5 premières lignes) :")
    print(df.head())

if __name__ == "__main__":
    clean_recipes()
