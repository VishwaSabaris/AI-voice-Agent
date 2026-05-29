import re

NORMALIZATION_MAP = {
    "koymuda": "coimbatore",
    "koimedu": "coimbatore",
    "kovai": "coimbatore",
    "கோயம்புத்தூர்": "coimbatore",

    "biriyani": "biryani",
    "பிரியாணி": "biryani",

    "friedrice": "fried rice",
    "சாதம்": "rice"
}

def normalize(text):
    text = text.lower()
    words = re.split(r'\s+', text)
    return " ".join([NORMALIZATION_MAP.get(w, w) for w in words])
