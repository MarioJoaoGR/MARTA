
import pytest
from isort._vendored.tomli._parser import load as tomli_load
from io import IOBase
from typing import Dict, Any, Callable
import warnings

# Mocking necessary modules or functions if needed for testing
ParseFloat = Callable[[str], float]

def test_valid_input_text_mode():
    # Create a mock file object with text mode content
    from io import StringIO
    fp = StringIO("key1 = 123\nkey2 = 456.789")
    
    # Call the function under test
    result = tomli_load(fp)
    
    # Assert the expected outcome
    assert isinstance(result, dict)
    assert result == {'key1': 123, 'key2': 456.789}

# Add more tests if necessary
