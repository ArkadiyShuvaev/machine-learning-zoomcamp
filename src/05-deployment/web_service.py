from fastapi import FastAPI
from pydantic import BaseModel
from prediction_service import predict

app = FastAPI()


class PredictionRecord(BaseModel):
    lead_source: str
    number_of_courses_viewed: int
    annual_income: float

@app.get("/")
async def root():
    return "Hello world!"

@app.post("/api/predictions")
async def predictions(model: PredictionRecord):
    result = predict(model)
    return result