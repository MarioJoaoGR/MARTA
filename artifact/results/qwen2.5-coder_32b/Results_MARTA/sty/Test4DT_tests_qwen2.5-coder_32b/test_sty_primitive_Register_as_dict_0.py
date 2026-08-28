
import pytest
from sty.primitive import Register

def test_happy_path():
    my_register = Register()
    my_register.color1 = 'red'
    my_register.color2 = 'blue'
    expected_dict = {'color1': 'red', 'color2': 'blue'}
    assert my_register.as_dict() == expected_dict

def test_edge_case_no_string_attributes():
    my_register = Register()
    expected_dict = {}
    assert my_register.as_dict() == expected_dict

def test_invalid_input_non_string_attributes():
    my_register = Register()
    my_register.color1 = 'red'
    my_register.number_attribute = 42
    my_register.list_attribute = [1, 2, 3]
    expected_dict = {'color1': 'red'}
    assert my_register.as_dict() == expected_dict
