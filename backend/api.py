from fastapi import FastAPI
from pydantic import BaseModel, Field

from backend.calculator.calculation import monthly_calculations

# note for me - to start api server: uv run fastapi dev
# make sure you are in cd backend

app = FastAPI()



MONTHS = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]

class Items(BaseModel):
    contribution: float = Field(ge=10, le=333)
    years: int = Field(ge=1, le=40)


# This listens for data submissions from client
# then runs the calcualtions with the given data
# returns it back in JSON

@app.post("/calculation")
def run_calculation(data: Items):
    result, with_interest, without_interest, interest_only, boost_only = monthly_calculations(data.contribution, data.years)
    labels = []
    # this helps range() make sense with the given result of years
    # so if 3 years then the count would be (1,2,3)
    for year in range(1, data.years + 1):
        for month in MONTHS:
            labels.append(f"{month} Y{year}")

    return {
            "result": result,
            "labels": labels,
            "with_interest": with_interest,
            "without_interest": without_interest,
            "interest_only": interest_only,
            "boost_only": boost_only,
            }
