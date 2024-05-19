from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from model import *
import numpy as np


class Patient(BaseModel):
    age: int | None = None
    sex: int | None = None
    cp: int | None = None
    trtbps: int | None = None
    chol: int | None = None
    fbs: int | None = None
    restecg: int | None = None
    thalachh: int | None = None
    exng: int | None = None
    oldpeak: int | None = None
    slp: int | None = None
    caa: int | None = None
    thall: int | None = None
    
    def to_numpy(self):
        return np.array([self.age, self.sex, self.cp, self.trtbps, self.chol, self.fbs, 
                         self.restecg, self.thalachh, self.exng, self.oldpeak, self.slp, self.caa, self.thall])
    
def model_routine():
    df = load_data()
    model = train_model(df)
    save_model(model)
    return load_model()

app = FastAPI()
app.model = model_routine()

@app.post("/predict/")
async def predict_patient_status(patients: List[Patient]):
    pred_data = pd.DataFrame(np.array([patient.to_numpy() for patient in patients]), columns = DF_COLUMNS)
    preds = app.model.predict(pred_data).tolist()
    return {'predictions' : preds}

@app.get("/")
async def predict_patient_status():
    return 'Hello world !'
