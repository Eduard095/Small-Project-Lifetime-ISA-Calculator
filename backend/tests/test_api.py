from fastapi.testclient import TestClient
from pytest import approx
from backend.api import app

client = TestClient(app)


#test case 1: test if given values calculates correct result
def test_valid_input_returns_results():
    response = client.post("/calculation", json={"contribution": 200, "years": 1})
    assert response.json()["result"] == approx("3019.61")

#test case 2: test if contribution is rejected with code 422 if out of bound
def test_contribution_too_high_is_rejected():
    response = client.post("/calculation", json={"contribution": 3333, "years": 1})
    assert response.status_code == 422

#test case 3: test if contribution with letters is rejected
def test_contribution_with_letters_is_rejected():
    response = client.post("/calculation", json={"contribution": "abc", "years": 1})
    assert response.status_code == 422

# test case 4: test if year is rejected with code 422 if out of bound
def test_years_too_high_is_rejected():
    response = client.post("/calculation", json={"contribution": 50, "years": 50})
    assert response.status_code == 422

# test case 5: years attribute missing is rejected
def test_years_missing_field_is_rejected():
    response = client.post("/calculator", json={"contribution": 50})
    assert response.status_code == 404

# test case 6: maximum value is not rejected
def test_maximum_contribution_is_allowed():
    response = client.post("/calculator", json={"contribution": 333, "years":40})
    assert response.status_code == 404
    
