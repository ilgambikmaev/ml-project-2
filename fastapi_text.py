from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()

classifier = pipeline("sentiment-analysis")  # модель из text.py

class TextInput(BaseModel):
    text: str

@app.post("/predict")
def predict(input: TextInput):
    result = classifier(input.text)
    return {"result": result}
