
import pytest
from pymonet.semigroups import Last

# Test valid case where Last is instantiated with a value
def test_valid_case():
    last_monoid = Last(value='test')
    assert str(last_monoid) == 'Last[value=test]'

# Test edge case where Last is instantiated without any value

# Test error case where Last is instantiated incorrectly (should raise TypeError)
def test_error_case():
    with pytest.raises(TypeError):
        Last()