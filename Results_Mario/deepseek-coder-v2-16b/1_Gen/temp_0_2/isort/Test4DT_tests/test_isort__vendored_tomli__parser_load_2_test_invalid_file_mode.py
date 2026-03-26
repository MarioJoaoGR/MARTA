
import pytest
from isort._vendored.tomli._parser import load
from io import StringIO
from typing import Dict, Any, Callable

# Mocking ParseFloat if necessary
ParseFloat = Callable[[str], float]  # Assuming ParseFloat is a callable that takes a string and returns a float

def test_invalid_file_mode():
    with pytest.raises(ValueError):
        # Create a StringIO object with invalid TOML content
        fp = StringIO("this is not valid toml")
        load(fp)  # Call the function without parse_float argument since it's mocked in this test
