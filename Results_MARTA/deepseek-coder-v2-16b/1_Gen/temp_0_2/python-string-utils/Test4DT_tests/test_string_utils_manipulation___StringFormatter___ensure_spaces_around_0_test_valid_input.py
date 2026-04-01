
import re
from string_utils.manipulation import __StringFormatter, InvalidInputError

def test_valid_input():
    formatter = __StringFormatter("Hello World")
    assert formatter.format() == "Hello World"
