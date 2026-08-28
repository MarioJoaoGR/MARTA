
import pytest
from urllib.parse import unquote_plus

def do_urldecode(string):
    return unquote_plus(string) if hasattr(unquote_plus, '__call__') else string.replace('%', '%25').replace('+', ' ')

# Test scenarios
@pytest.mark.parametrize("input_string, expected", [("Hello%20World", "Hello World")])
def test_valid_input(input_string, expected):
    assert do_urldecode(input_string) == expected

@pytest.mark.parametrize("input_string, expected", [("%E4%B8%AD%E6%96%87", "中文")])
def test_chinese_characters(input_string, expected):
    assert do_urldecode(input_string) == expected

@pytest.mark.parametrize("input_string, expected", [("InvalidInput", "InvalidInput")])
def test_invalid_input(input_string, expected):
    assert do_urldecode(input_string) == expected
