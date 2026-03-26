
from pymonet.semigroups import One

def test_edge_case():
    one = One(True)  # Create an instance of One with True value
    assert str(one) == 'One[value=True]'
