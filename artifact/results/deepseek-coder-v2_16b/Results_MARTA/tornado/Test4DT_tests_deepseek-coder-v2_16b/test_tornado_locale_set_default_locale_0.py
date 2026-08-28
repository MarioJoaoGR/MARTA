
import pytest
from unittest.mock import patch
from tornado.locale import _default_locale, set_default_locale


def test_missing_lines():
    with pytest.raises(NotImplementedError):
        raise NotImplementedError("This feature is not implemented yet.")
