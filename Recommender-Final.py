from flask import Flask, request, jsonify
import joblib
import pandas as pd
from pymongo import MongoClient
from datetime import datetime
import html

app = Flask(__name__)

# Charger le modèle (chargé une seule fois au démarrage de l'application)
model = joblib.load('Tree2.joblib')

# Connexion à MongoDB
client = MongoClient('mongodb://localhost:27017')
db = client['assurance']
information_collection = db['information']

def calculate_age(date_of_birth):
    today = datetime.today()
    birth_date = datetime.strptime(date_of_birth, "%Y-%m-%d")
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

def determine_nature_client(address):
    lowercase_address = address.lower().replace(" ", "_")
    return "PARTICULIER" if "maroc" in lowercase_address else "MDM"

def prepare_data(data):
    age = calculate_age(data['date_of_birth'])
    nature_client = determine_nature_client(data['address'])
    input_data = pd.DataFrame([[age,
                                1 if nature_client == 'MDM' else 0,
                                1 if nature_client == 'PARTICULIER' else 0,
                                1 if data['sexe'] == 'F' else 0,
                                1 if data['sexe'] == 'M' else 0,
                                1 if data['situation_familiale'] == 'single' else 0,
                                1 if data['situation_familiale'] == 'Divorced' else 0,
                                1 if data['situation_familiale'] == 'Married' else 0,
                                1 if data['situation_familiale'] == 'widow' else 0]],
                                columns=['Age', 'NATURE CLIENT_MDM', 'NATURE CLIENT_PARTICULER',
                                       'Sexe_F', 'Sexe_M', 'SITUATION FAMILIALE_C',
                                       'SITUATION FAMILIALE_D', 'SITUATION FAMILIALE_M', 'SITUATION FAMILIALE_V'])
    return input_data

@app.route('/predict/<date_of_birth>/<address>/<sexe>/<situation_familiale>', methods=['GET'])
def predict(date_of_birth, address, sexe, situation_familiale):
    try:
        input_data = prepare_data({
            "date_of_birth": date_of_birth,
            "address": address,
            "sexe": sexe,
            "situation_familiale": situation_familiale
        })

        prediction = model.predict(input_data)
        product_info = information_collection.find_one({"id": prediction[0]})
        
        if product_info:
            product_info.pop("_id", None)
            product_info["description"] = html.escape(product_info["description"])
            return jsonify({"prediction": prediction.tolist(), "product_info": product_info})
        else:
            return jsonify({"error": "Aucune information trouvée pour la prédiction."}), 404

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)