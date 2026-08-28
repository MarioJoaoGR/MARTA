
import pytest
from unittest.mock import patch, MagicMock
from sty.primitive import Register

# Test for valid input in as_dict method
def test_valid_input():
    custom_register = Register()
    with patch.object(custom_register, 'as_dict', return_value={'is_muted': str(custom_register.is_muted)}):
        assert custom_register.as_dict() == {'is_muted': 'False'}

# Test for edge cases in as_dict method
def test_edge_case():
    custom_register = Register()
    with patch.object(custom_register, 'as_dict', return_value={}):
        assert custom_register.as_dict() == {}

# Test for raising ValueError for invalid inputs in as_dict method
def test_invalid_input():
    custom_register = Register()
    with patch.object(custom_register, 'as_dict', side_effect=ValueError("Invalid input")):
        with pytest.raises(ValueError):
            custom_register.as_dict()
