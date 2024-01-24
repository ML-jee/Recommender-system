from pymongo import MongoClient

# Remplacez "user", "<password>" et "assuranceprediction" par vos informations
username = "user"
password = "0000"
cluster_name = "assuranceprediction"

# Construisez l'URI de connexion
uri = f"mongodb+srv://{username}:{password}@{cluster_name}.khaplur.mongodb.net/?retryWrites=true&w=majority"

# Créez un client MongoDB
client = MongoClient(uri)

# Sélectionnez la base de données
db = client.Assurance  # Remplacez "ma_base_de_donnees" par le nom de votre base de données

# Sélectionnez la collection
collection = db.info2  # Remplacez "ma_collection" par le nom de votre collection

# Exemple : insérez un document
# data = {"key": "value"}
# result = collection.insert_one(data)
# print(f"Document inséré avec l'ID : {result.inserted_id}")


# Your JSON data
json_data =[
  {
    "id": "MaRetraite",
    "produit": "MaRetraite",
    "description": "Permet de constituer progressivement une épargne pour la retraite. Adaptation des contributions en fonction de la capacité financière. Avantages fiscaux pour les contrats d'une durée ≥ 8 ans. Deux assurances décès toutes causes et invalidité totale et définitive. Rémunération des cotisations avec des intérêts annuels et une participation aux bénéfices."
  },
  {
    "id": "AlInjadAlMoumtaz",
    "produit": "Al Injad Al Moumtaz",
    "description": "Assurance offrant une assistance permanente au souscripteur, à sa famille et à son véhicule. Couverture universelle étendue pour les personnes physiques et les véhicules. Large choix de prestations pour couvrir divers besoins."
  },
  {
    "id": "AvenirMesEnfants",
    "produit": "AvenirMesEnfants",
    "description": "Solution pratique et accessible pour assurer l'avenir des enfants. Ouverte au personnel. Cotisations à partir de 200 DH par mois. Frais de fonctionnement attractifs."
  },
  {
    "id": "AlInjadChaabi",
    "produit": "Al Injad Chaabi",
    "description": "Produit d'assistance complet pour les déplacements, couvrant le souscripteur, sa famille et son véhicule. Tarification attractive, prestations complètes, couverture complète en cas de décès, assistance médicale et technique."
  },
  {
    "id": "INJADAchamil",
    "produit": "INJAD ACHAMIL",
    "description": "Assurance pour voyages à l'étranger offrant une couverture complète. Possibilité d'assurer les parents. Assistance médicale, gestion des formalités administratives en cas de décès, accompagnement en cas de décès, etc."
  }
]


# # Insert the data into MongoDB
# collection.insert_many(json_data)

# Close the MongoDB connection
client.close()

print("Data inserted into MongoDB successfully.")
