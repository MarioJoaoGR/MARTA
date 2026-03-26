
import pytest
from pymonet.semigroups import First

def test_valid_case():
    first1 = First(1)
    first2 = First(2)
    combined_first = first1.concat(first2)
    assert combined_first.value == 1
