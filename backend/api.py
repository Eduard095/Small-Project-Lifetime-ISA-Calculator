from fastapi import FastAPI
from pydantic import BaseModel, Field

from backend.calculator.calculation import monthly_calculations, data_with_interest_return, data_without_interest_return

# note for me - to start api server: uv run fastapi dev
# make sure you are in cd backend

app = FastAPI()

months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]

class Items(BaseModel):
    contribution: float = Field(ge=10, le=333)
    years: int = Field(ge=1, le=40)


# This listens for data submissions from client
# then runs the calcualtions with the given data
# returns it back in JSON
@app.post("/calculation")
def run_calculation(data: Items):
    with_interest = data_with_interest_return()
    without_interest = data_without_interest_return()
    result = monthly_calculations(data.contribution, data.years)
    return {
            "result": result,
            "labels": months,
            "with_interest": with_interest,
            "without_interest": without_interest,
            }

