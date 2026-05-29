from transformers import pipeline

# Load small fast model
nlp = pipeline("text-classification", model="distilbert-base-uncased")

# Custom mapping
AREA_MAP = {
    "koymuda": "Coimbatore",
    "koimedu": "Coimbatore",
    "koyambedu": "Koyambedu"
}

ITEMS = ["biryani", "dosa", "fried rice", "meals"]

def process(text):
    text_lower = text.lower()

    # Fix known errors
    for wrong, correct in AREA_MAP.items():
        if wrong in text_lower:
            text_lower = text_lower.replace(wrong, correct.lower())

    # Extract item
    item_found = "unknown"
    for item in ITEMS:
        if item in text_lower:
            item_found = item

    # Extract area (simple)
    area_found = "unknown"
    for area in ["coimbatore", "peelamedu", "saravanampatti", "singanallur"]:
        if area in text_lower:
            area_found = area.capitalize()

    return {
        "corrected": text_lower,
        "area": area_found,
        "item": item_found
    }
