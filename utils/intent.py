def detect_intent(text):

    text = text.lower()

    if any(word in text for word in ["cancel", "cancel pannunga", "vendam"]):
        return "cancel"

    if any(word in text for word in ["change", "modify", "maatunga"]):
        return "modify"

    return "order"
