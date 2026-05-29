import pickle
import re


# Load trained model
saved_model = pickle.load(
    open(
        "/home/sabaris/storage/Coimbatore_SLM/slm_engine/model.pkl",
        "rb"
    )
)

# Load models
vectorizer = saved_model["vectorizer"]
area_model = saved_model["area_model"]
food_model = saved_model["food_model"]
quantity_model = saved_model["quantity_model"]


def extract_number(text):
    """
    Extract number directly from speech.
    Example:
    '2 biryani'
    'இரண்டு பிரியாணி'
    """

    nums = re.findall(r"\d+", text)

    if nums:
        return nums[0]

    tamil_numbers = {
        "ஒரு": "1",
        "ஒன்று": "1",
        "இரண்டு": "2",
        "மூன்று": "3",
        "நான்கு": "4",
        "ஐந்து": "5"
    }

    text = text.lower()

    for word, value in tamil_numbers.items():
        if word in text:
            return value

    return None


def predict(text):

    X = vectorizer.transform([text])

    # Predict values
    area = area_model.predict(X)[0]
    food = food_model.predict(X)[0]
    quantity = quantity_model.predict(X)[0]

    # Prefer direct spoken number
    extracted_qty = extract_number(text)

    if extracted_qty:
        quantity = extracted_qty

    return {
        "area": area,
        "item": food,
        "quantity": str(quantity)
    }
