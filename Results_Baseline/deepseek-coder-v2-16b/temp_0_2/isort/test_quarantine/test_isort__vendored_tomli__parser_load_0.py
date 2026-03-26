
# Module: Test4DT_tests.test_isort__vendored_tomli__parser_load_0
import pytest
from io import StringIO, BytesIO
from tomli import load as original_load
from tomli._parser import loads
import warnings

# Test cases for the `load` function from the `tomli` module.

def test_load_text_file():
    toml_data = '''name = "Tom"
    age = 35
    hobbies = ["reading", "sports"]'''
    fp = StringIO(toml_data)
    parsed_toml = original_load(fp)
    assert parsed_toml == {'name': 'Tom', 'age': 35, 'hobbies': ['reading', 'sports']}

def test_load_binary_file():
    toml_data = b'''name = "Tom"
    age = 35
    hobbies = ["reading", "sports"]'''
    fp = BytesIO(toml_data)
    parsed_toml = original_load(fp)
    assert parsed_toml == {'name': 'Tom', 'age': 35, 'hobbies': ['reading', 'sports']}

def test_custom_parse_float():
    def custom_parse_float(s):
        try:
            return float(s)
        except ValueError:
            raise ValueError(f"Cannot convert '{s}' to float.")
    
    toml_data = '''name = "Tom"
    age = 35
    hobbies = ["reading", "sports"]'''
    fp = StringIO(toml_data)
    parsed_toml = original_load(fp, parse_float=custom_parse_float)
    assert parsed_toml == {'name': 'Tom', 'age': 35, 'hobbies': ['reading', 'sports']}

def test_deprecation_warning():
    toml_data = '''name = "Tom"
    age = 35
    hobbies = ["reading", "sports"]'''
    fp = StringIO(toml_data)
    with pytest.warns(DeprecationWarning):
        parsed_toml = original_load(fp)
    assert parsed_toml == {'name': 'Tom', 'age': 35, 'hobbies': ['reading', 'sports']}

def test_invalid_input():
    toml_data = "invalid toml"
    fp = StringIO(toml_data)
    with pytest.raises(ValueError):
        parsed_toml = original_load(fp)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort__vendored_tomli__parser_load_0
isort/Test4DT_tests/test_isort__vendored_tomli__parser_load_0.py:6:0: E0611: No name 'loads' in module 'tomli._parser' (no-name-in-module)


"""