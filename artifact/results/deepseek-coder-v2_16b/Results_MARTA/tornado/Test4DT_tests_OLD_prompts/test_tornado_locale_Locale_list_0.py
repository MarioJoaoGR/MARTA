
import pytest
from unittest.mock import patch
from tornado.locale import LOCALE_NAMES, Locale



def test_invalid_input():
    with pytest.raises(Exception) as e:
        Locale(code=None)
    assert str(e.value) == "'NoneType' object has no attribute 'startswith'"