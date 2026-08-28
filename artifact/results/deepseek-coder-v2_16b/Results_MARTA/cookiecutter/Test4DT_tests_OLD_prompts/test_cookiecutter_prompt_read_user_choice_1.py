
import pytest
from unittest.mock import patch, MagicMock
from cookiecutter.prompt import read_user_choice

# Test for valid input scenario

# Test for invalid options type scenario
def test_invalid_options_type():
    with pytest.raises(TypeError):
        read_user_choice('color', None)

# Test for empty options list scenario
def test_empty_options_list():
    with pytest.raises(ValueError):
        read_user_choice('color', [])