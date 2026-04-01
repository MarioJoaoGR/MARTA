
from pymonet.semigroups import Last  # Correctly importing from the specified module path

def test_error_case():
    last1 = Last(10)
    last2 = Last(20)
    
    combined_last = last1.concat(last2)
    
    assert combined_last.value == 20
