import mlflow 
import mlflow.pyfunc
from fastapi import FastAPI
from fastapi import HTTPException
from pydantic import BaseModel
from src.cleaning import clean_text
app = FastAPI(title="Spam Filter API")
mlflow.set_tracking_uri("sqlite:////home/stayn/Projects/Spam_Filter/notebooks/mlflow.db")
class Message(BaseModel) :
    text : str
MODEL_URI = "models:/spam_filter_models@champion"
try:
    print("loading model")
    model = mlflow.pyfunc.load_model(MODEL_URI)
    print("model successfully loaded")
except:
    print("error occured while trying to load model")
    model = None
@app.get("/")
def root() :
    return {"message": "The Spam Filter API is running."}
@app.post("/predict")
def predict(msg : Message) :

    if model == None :
        raise HTTPException(status_code=503 , detail="prediction model is unavailable")
    try :
        result = int(model.predict([clean_text(msg.text)])[0])
        if result == 1:
            return {"prediction": "Spam"}
        else :
            return {"prediction": "Ham"}
    except :
        raise HTTPException(status_code=500 , detail="Inference error")