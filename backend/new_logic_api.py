from fastapi import FastAPI
from pydantic import BaseModel, Field
from .new_logic_api import LifetimeCalculator

# note for me - to start api server: uv run fastapi dev
# make sure you are in cd backend
app = FastAPI()


MONTHS = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]

class Items(BaseModel):
    contribution: float = Field(ge=10, le=333)
    years: int = Field(ge=1, le=40)


calculator = LifetimeCalculator()

@app.get("/Calculation")
async def root(data: Items):
    calculator = LifetimeCalculator(data.contribution, data.years)

    (accrued_contribution, 
    accrued_interest,
    accrued_boost,
    with_interest_data,
    without_interest_data
    ) = calculator

    # this helps range() make sense with the given result of years
    # so if 3 years then the count would be (1,2,3)
    labels = []
    for year in range(1, data.years + 1):
        for month in MONTHS:
            labels.append(f"{month} Year {year}")

    return{
        "accured_contribution": accrued_contribution,
        "accrued_interest":  accrued_interest,
        "accrued_boost": accrued_boost,
        "with_interest_data": with_interest_data,
        "without_interest_data": without_interest_data,
    }