from fastapi.testclient import TestClient
from pytest import approx
from backend.api import app

client = TestClient(app)


#test case 1: test if given values calculates correct result
def test_valid_input_returns_results():
    response = client.post("/calculation", json={"contribution": 200, "years": 1})
    assert response.json()["result"] == approx(3019.61)

#test case 2: test if contribution is rejected with code 422 if out of bound
def test_contribution_too_high_is_rejected():
    response = client.post("/calculation", json={"contribution": 3333, "years": 1})
    assert response.assert_status == 422

