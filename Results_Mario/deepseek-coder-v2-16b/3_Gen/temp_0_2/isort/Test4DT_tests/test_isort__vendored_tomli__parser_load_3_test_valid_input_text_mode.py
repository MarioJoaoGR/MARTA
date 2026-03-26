
from isort._vendored.tomli._parser import load
import pytest
from typing import Dict, Any, Callable

# Define a mock ParseFloat function for testing purposes
def mock_parse_float(value: str):
    return float(value)

@pytest.mark.parametrize("parse_float", [mock_parse_float])
def test_valid_input_text_mode(tmp_path, parse_float):
    # Create a sample TOML file content
    toml_content = """key1 = "value1"
key2 = 3.14
key3 = [1, 2, 3]"""
    
    # Write the TOML content to a temporary file
    toml_file_path = tmp_path / "example.toml"
    with open(toml_file_path, "w") as f:
        f.write(toml_content)
    
    # Open the file in text mode for reading
    with open(toml_file_path, "r") as f:
        result = load(f, parse_float=parse_float)
    
    # Check if the parsed content matches the expected dictionary
    assert isinstance(result, dict)
    assert result["key1"] == "value1"
    assert result["key2"] == pytest.approx(3.14)  # Using approx for floating-point comparison
    assert result["key3"] == [1, 2, 3]
