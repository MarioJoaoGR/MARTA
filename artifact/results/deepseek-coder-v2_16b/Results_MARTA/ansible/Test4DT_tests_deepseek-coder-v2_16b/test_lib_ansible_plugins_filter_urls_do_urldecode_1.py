
import pytest
from urllib.parse import unquote_plus

def do_urldecode(string):
    return unicode_urldecode(string)

@pytest.mark.parametrize("input_string, expected", [
    ('Hello%20World', 'Hello World'),
])
def test_valid_input(input_string, expected):
    assert do_urldecode(input_string) == expected

@pytest.mark.parametrize("input_string", [None])
def test_edge_case_none(input_string):
    with pytest.raises(TypeError):
        do_urldecode(input_string)

@pytest.mark.parametrize("input_string, expected", [
    ('Hello%20World!', 'Hello World!'),
])
def test_invalid_input(input_string, expected):
    with pytest.raises(TypeError):
        do_urldecode(input_string)
