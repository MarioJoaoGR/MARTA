
import pytest
import re
from your_module import is_python_identifier  # Replace 'your_module' with the actual module name where the function is defined

# Define a regex pattern for Python identifiers
_VALID_IDENTIFIER_STRING_REGEX = r'^[a-zA-Z_][a-zA-Z0-9_]*$'

@pytest.mark.parametrize("tested_str, expected", [
    ("my_variable", True),
    ("123abc", False),
    ("_underscore", True)
])
def test_is_python_identifier(tested_str, expected):
    assert is_python_identifier(tested_str) == expected
