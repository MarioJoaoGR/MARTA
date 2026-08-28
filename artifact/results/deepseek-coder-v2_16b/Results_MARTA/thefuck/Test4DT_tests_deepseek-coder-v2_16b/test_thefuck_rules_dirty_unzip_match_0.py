
import pytest
from thefuck.rules.dirty_unzip import match as dirty_unzip_match


def test_valid_input_without_d_flag():
    command = {'script_parts': ['unzip', 'example.zip']}
    with pytest.raises(AttributeError):  # Assuming _is_bad_zip will be called internally by match
        assert dirty_unzip_match(command)

def test_invalid_input_none():
    command = None
    with pytest.raises(AttributeError):  # Assuming is_app will be called internally by match
        assert not dirty_unzip_match(command)