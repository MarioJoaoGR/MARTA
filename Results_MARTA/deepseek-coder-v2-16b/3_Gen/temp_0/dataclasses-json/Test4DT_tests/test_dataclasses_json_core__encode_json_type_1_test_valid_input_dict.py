
import pytest
from dataclasses_json.core import Json  # Replace 'your_module' with the actual module name
from unittest.mock import MagicMock

# Mock _ExtendedEncoder to avoid importing it directly
class _ExtendedEncoder:
    def default(self, value):
        return value

def test_valid_input_dict():
    from dataclasses_json.core import _encode_json_type  # Replace 'your_module' with the actual module name
    
    # Mock _ExtendedEncoder to avoid importing it directly
    _ExtendedEncoder.default = MagicMock(side_effect=_ExtendedEncoder().default)
    
    example_dict = {"key1": [1, 2], "key2": {"nestedKey": "nestedValue"}}
    encoded_dict = _encode_json_type(example_dict)
    
    assert isinstance(encoded_dict, dict)
    assert all(isinstance(k, str) for k in encoded_dict.keys())  # Assuming keys are always strings due to JSON compatibility
    assert all(isinstance(v, (list, dict)) or not isinstance(v, Json.__args__) for v in encoded_dict.values())
    
    if isinstance(encoded_dict["key2"], dict):
        assert "nestedKey" in encoded_dict["key2"]
        assert encoded_dict["key2"]["nestedKey"] == "nestedValue"

if __name__ == "__main__":
    pytest.main()
