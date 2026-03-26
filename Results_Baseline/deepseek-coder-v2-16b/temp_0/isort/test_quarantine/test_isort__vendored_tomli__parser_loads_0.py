
import tomllib
import pytest
from typing import Dict, Any, Callable
import decimal

# Define the ParseFloat type for clarity
ParseFloat = Callable[[str], Any]

def test_loads_simple_toml():
    toml_string = 'key1 = "value1"\nkey2 = 42'
    parsed_data = tomllib.loads(toml_string)
    assert isinstance(parsed_data, dict)
    assert parsed_data == {'key1': 'value1', 'key2': 42}

def test_loads_complex_toml():
    toml_string = """
    key1 = "value1"
    key2 = 42
    [section]
    nested_key = "nested_value"
    """
    
    def parse_float(s):
        try:
            return decimal.Decimal(s)
        except ValueError:
            return float(s)
    
    parsed_data = tomllib.loads(toml_string, parse_float=parse_float)
    assert isinstance(parsed_data, dict)
    assert parsed_data == {'key1': 'value1', 'key2': 42, 'section': {'nested_key': 'nested_value'}}

def test_loads_malformed_toml():
    malformed_toml = 'key1 = "value1"\nkey2 ='
    with pytest.raises(Exception) as e:
        parsed_data = tomllib.loads(malformed_toml)