import pickle
from fastapi import FastAPI
from pydantic import BaseModel

with open('pipeline_v1.bin', 'rb') as f:
    pipeline = pickle.load(f)

print("Pipeline loaded successfully!")

app = FastAPI()

class Client(BaseModel):
    lead_source: str
    number_of_courses_viewed: int
    annual_income: float

@app.get("/")
def read_root():
    return {"message": "Model prediction service is running"}

@app.post("/predict")
def predict(client: Client):
    # Convert to dictionary format for prediction
    client_data = client.dict()
    # Make prediction
    prediction = pipeline.predict([client_data])[0]
    
    # Get probability if available
    if hasattr(pipeline, 'predict_proba'):
        probability = pipeline.predict_proba([client_data])[0]
        return {
            "prediction": int(prediction),
            "probability": float(probability[1])
        }
    else:
        return {
            "prediction": int(prediction)
        }