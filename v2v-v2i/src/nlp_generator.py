from transformers import pipeline

nlp_model = pipeline("text-generation", model="gpt-2")
def generate_alert(data):
    return nlp_model(f"Accident detected: {data}", max_length=30)
