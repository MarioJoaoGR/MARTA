
import pytest
from unittest.mock import patch
from httpie.plugins.base import FormatterPlugin

def test_invalid_inputs():
    with pytest.raises(KeyError):
        invalid_kwargs = {'non_existent': 'argument'}
        formatter = FormatterPlugin(**invalid_kwargs)
