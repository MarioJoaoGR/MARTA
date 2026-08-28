
import pytest
from tornado.locale import Locale, LOCALE_NAMES



def test_invalid_input():
    with pytest.raises(NotImplementedError):
        locale = Locale(code='fr')