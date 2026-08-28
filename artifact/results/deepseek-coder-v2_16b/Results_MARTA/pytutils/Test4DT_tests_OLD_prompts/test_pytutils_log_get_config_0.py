
import pytest
from unittest.mock import patch
from pytutils.log import get_config

def test_empty_dictionary_input():
    with pytest.raises(ValueError):
        config = get_config(default={})
