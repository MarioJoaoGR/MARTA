
import pytest
from pymonet.semigroups import Last  # Correctly importing from the module path

def test_edge_case_none():
    """
    Test the edge case where None is used as a value in the Last semigroup.
    """
    last1 = Last(None)  # Instantiating a Last with None value
    last2 = Last("hello")  # Instantiating another Last with a string value
    
    combined_last = last1.concat(last2)  # Combining the two Last instances
    assert combined_last.value == "hello"  # Assert that the latest value is retained
