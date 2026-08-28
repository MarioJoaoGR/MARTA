
import pytest
from tornado.locale import Locale, LOCALE_NAMES



def test_invalid_input_none():
    with pytest.raises(NotImplementedError):
        locale = Locale(code='en-US')
        locale.translate("Hello", plural_message="Hellos", count=None)