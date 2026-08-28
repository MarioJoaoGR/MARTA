
import pytest
from pymonet.semigroups import Last


def test_combining_with_non_empty():
    last1 = Last(10)
    last2 = Last(20)
    
    # Combining with a non-empty instance should return the value of the non-empty instance
    combined_last = last1.concat(last2)
    assert combined_last.value == 20
