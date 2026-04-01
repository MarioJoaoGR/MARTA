
import pytest
from string_utils.manipulation import __RomanNumbers

def test_edge_case():
    # Test with an edge case Roman numeral that has a clear subtraction pattern (e.g., 'IV')
    assert __RomanNumbers.decode('IV') == 4
