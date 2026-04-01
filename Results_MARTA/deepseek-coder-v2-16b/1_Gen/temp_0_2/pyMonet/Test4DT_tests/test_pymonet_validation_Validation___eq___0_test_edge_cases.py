
import pytest
from pymonet.validation import Validation

@pytest.mark.parametrize("val1, val2", [
    (Validation(None, []), Validation(None, [])),
    (Validation(10, ['Error']), Validation(10, ['Error'])),
    (Validation(None, ['Error 1', 'Error 2']), Validation(None, ['Error 1', 'Error 2']))
])
def test_validation_eq(val1, val2):
    assert val1 == val2
