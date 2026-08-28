
import pytest
from pymonet.semigroups import First

def test_edge_case():
    with pytest.raises(TypeError):
        first_instance = First()
        first_instance.combine(other=First())
