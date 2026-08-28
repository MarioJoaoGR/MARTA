
import pytest
from unittest.mock import patch
from mimesis.providers import Generic
from mimesis.exceptions import UnsupportedLocale

# Test scenario 1: test_valid_locale_and_seed
def test_valid_locale_and_seed():
    with patch('mimesis.providers.Generic.__init__', return_value=None):
        field = Generic(locale='es', seed=12345)
        assert isinstance(field, Generic)

# Test scenario 2: test_invalid_locale_raises_exception
def test_invalid_locale_raises_exception():
    with pytest.raises(UnsupportedLocale) as excinfo:
        field = Generic(locale='xx', seed=12345)
    assert str(excinfo.value) == 'Text.__init__() missing 1 required positional argument: 'locale''

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
SyntaxError: invalid syntax (line 17, col 92)
    assert str(excinfo.value) == 'Text.__init__() missing 1 required positional argument: 'locale''
"""