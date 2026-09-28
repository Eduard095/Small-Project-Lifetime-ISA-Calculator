from fastapi import FastAPI
from pydantic import BaseModel
from backend.calculator import calculation


app = FastAPI()

class Items(BaseModel):
    contribution: float
    years: int

#This listens for data submissions from client
#then runs the calcualtions with the given data
#returns it back in JSON
@app.post("/calculation")
def run_calculation(data: Items):
    result = calculation(data.contribution, data.years)
    return {"result": result}