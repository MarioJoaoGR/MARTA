
import pytest
from isort._vendored.tomli._parser import loads, TOMLDecodeError

def test_valid_input_complex_document():
    toml_string = """
    [section]
    key=value
    number=3.14
    list=[1, 2, 3]
    """
    
    with pytest.raises(TOMLDecodeError):
        loads(toml_string)
