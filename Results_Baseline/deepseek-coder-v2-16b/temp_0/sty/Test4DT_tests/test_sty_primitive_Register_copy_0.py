
# Module: sty.primitive
import pytest
from unittest.mock import patch, MagicMock
from sty.primitive import Register
from copy import deepcopy

# Test the creation of a custom register
def test_create_custom_register():
    reg = Register()
    reg.renderfuncs['custom'] = lambda x: f"Custom {x}"
    assert reg.renderfuncs['custom']("function") == "Custom function"

# Test muting and unmuting the register
def test_mute_unmute():
    reg = Register()
    assert not reg.is_muted
    reg.is_muted = True
    assert reg.is_muted
    reg.is_muted = False
    assert not reg.is_muted

# Test exporting the register as a dictionary
def test_export_as_dict():
    reg = Register()
    dict_repr = reg.as_dict()
    assert isinstance(dict_repr, dict)

# Test exporting the register as a named tuple
def test_export_as_namedtuple():
    reg = Register()
    namedtuple_repr = reg.as_namedtuple()
    assert isinstance(namedtuple_repr, tuple)

# Test copying the register
def test_copy_register():
    reg = Register()
    copied_reg = reg.copy()
    assert copied_reg is not reg
    assert copied_reg.renderfuncs == reg.renderfuncs
    assert copied_reg.is_muted == reg.is_muted
    assert copied_reg.eightbit_call == reg.eightbit_call
    assert copied_reg.rgb_call == reg.rgb_call

# Test the copy method directly on the class
def test_copy_method():
    reg = Register()
    with patch('sty.primitive.deepcopy') as mock_deepcopy:
        mock_deepcopy.return_value = MagicMock()
        copied_reg = reg.copy()