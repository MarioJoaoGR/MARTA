
from pymonet.semigroups import One

def test_valid_case_false_value():
    one1 = One(False)  # Instantiating with False
    one2 = One(True)   # Instantiating with True
    combined_one = one1.concat(one2)  # Combining the two Monoids
    assert combined_one.value is True, "Expected value to be True after combining with True"
    
    another_one = One(0)               # Instantiating with a falsy value (integer 0)
    combined_with_zero = another_one.concat(One(False))  # Combining with False
    assert combined_with_zero.value is False, "Expected value to be False after combining with False"
