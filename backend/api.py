from fastapi import FastAPI
from pydantic import BaseModel, Field

from backend.calculator.calculation import monthly_calculations

# note for me - to start api server: uv run fastapi dev
# make sure you are in cd backend

app = FastAPI()


class Items(BaseModel):
    contribution: float = Field(ge=10, le=333)
    years: int = Field(ge=1, le=40)


# This listens for data submissions from client
# then runs the calcualtions with the given data
# returns it back in JSON
@app.post("/calculation")
def run_calculation(data: Items):
    result = monthly_calculations(data.contribution, data.years)
    return {"result": result}
