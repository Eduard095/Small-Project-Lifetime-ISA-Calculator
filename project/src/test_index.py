#testing zone
from index import user_input


#1. check contribution is 10 <= x <= 333
#2. check years for now, years < 30
#3 make sure to return the correct values
def test_user_input(monkeypatch):
    #the two responses that 
    inputs = iter(["200", "5"])

    #replace the real input() with one that gives me the next fake input
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    contributing, years = user_input()
    
    assert contributing == 200.0
    assert years == 5