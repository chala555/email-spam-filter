from fastapi import FastAPI
from pydantic import BaseModel
from src.cleaning import clean_text
import joblib
import os

app = FastAPI(title="Spam Filter API")
#loading the trained model and vectorizer
## setting path 
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(PROJECT_ROOT, 'models', 'logistic_regression_model.pkl')
VECTORIZER_PATH = os.path.join(PROJECT_ROOT, 'models', 'tfidf_vectorizer.pkl')
model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)
#http requests
class Message(BaseModel) :
    text : str
@app.get("/")
def root() :
    return {"message": "The Spam Filter API is running."}
@app.post("/predict")
def predict(msg : Message) :
    vector = vectorizer.transform([clean_text(msg.text)])
    result = model.predict(vector)[0]
    print(clean_text(msg.text))
    if result == 1 :
        return {"prediction": "Spam"}
    else :
        return {"prediction": "Ham"}