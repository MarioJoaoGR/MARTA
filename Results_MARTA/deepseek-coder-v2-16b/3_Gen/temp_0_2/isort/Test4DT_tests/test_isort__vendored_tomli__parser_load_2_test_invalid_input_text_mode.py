
import pytest
from isort._vendored.tomli._parser import load, TOMLDecodeError
from io import StringIO
import warnings

def test_invalid_input_text_mode():
    with open('example.toml', 'w') as file:
        file.write("invalid_content")
    
    with open('example.toml', 'r') as file:
        fp = StringIO(file.read())  # Use StringIO to simulate a file object in memory
        with pytest.warns(DeprecationWarning):
            with warnings.catch_warnings():
                # Cause all warnings to be triggered.
                warnings.simplefilter("always")
                with pytest.raises(TOMLDecodeError):
                    data = load(fp)
