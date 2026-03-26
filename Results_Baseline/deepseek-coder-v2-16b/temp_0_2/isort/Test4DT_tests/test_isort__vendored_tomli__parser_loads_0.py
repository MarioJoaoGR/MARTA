
import pytest
from tomli import TOMLDecodeError, loads  # Importing the missing variable

# Test cases for the `loads` function from the `tomli` module

def test_basic_usage():
    toml_string = '''name = "Tom"
    age = 35
    hobbies = ["reading", "sports"]'''
    parsed_toml = loads(toml_string)
    assert parsed_toml == {'name': 'Tom', 'age': 35, 'hobbies': ['reading', 'sports']}

def test_custom_parse_float():
    def parse_custom_float(s: str):
        try:
            return float(s)
        except ValueError:
            raise ValueError(f"Cannot convert '{s}' to float.")

    toml_string = '''number = "3.14"'''
    parsed_toml = loads(toml_string, parse_float=parse_custom_float)