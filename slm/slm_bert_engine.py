import pickle
import re

# Load models
vectorizer = pickle.load(open("/home/sabaris/storage/Coimbatore_SLM/slm_engine/vectorizer.pkl", "rb"))
area_model = pickle.load(open("/home/sabaris/storage/Coimbatore_SLM/slm_engine/area_model.pkl", "rb"))
food_model = pickle.load(open("/home/sabaris/storage/Coimbatore_SLM/slm_engine/food_model.pkl", "rb"))

def extract_qty(text):
    match = re.search(r"\d+", text)
    return int(match.group()) if match else 1

def predict(text):

    X = vectorizer.transform([text])

    area = area_model.predict(X)[0]
    food = food_model.predict(X)[0]
    qty = extract_qty(text)

    return {
        "area": area,
        "item": food,
        "quantity": qty
    }
