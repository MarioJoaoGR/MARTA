
import pytest
from tornado.locale import Locale



def test_invalid_input():
    with pytest.raises(NotImplementedError):
        locale = Locale(code='en-US')
        locale.translate("Hello", count=-1)