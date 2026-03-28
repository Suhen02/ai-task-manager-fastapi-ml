import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

texts = [
    "buy groceries",
    "team meeting",
    "finish project",
    "call parents",
    "urgent bug fix",
    "prepare presentation"
]

labels = ["Personal", "Work", "Work", "Personal", "Work", "Work"]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)

model = LogisticRegression()
model.fit(X, labels)

with open("app/ml/model.pkl", "wb") as f:
    pickle.dump((vectorizer, model), f)