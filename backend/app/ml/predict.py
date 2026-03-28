import pickle

with open("app/ml/model.pkl", "rb") as f:
    vectorizer, model = pickle.load(f)

def predict_category(text: str):
    X = vectorizer.transform([text])
    return model.predict(X)[0]

def predict_priority(text: str):
    if "urgent" in text.lower():
        return "High"
    return "Medium"