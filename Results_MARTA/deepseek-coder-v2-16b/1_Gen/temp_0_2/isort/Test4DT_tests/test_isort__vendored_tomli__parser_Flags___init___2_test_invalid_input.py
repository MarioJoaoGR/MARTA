
import pytest
from typing import Dict

class Flags:
    """Flags that map to parsed keys/namespaces."""
    FROZEN = 0
    EXPLICIT_NEST = 1

    def __init__(self) -> None:
        self._flags: Dict[str, dict] = {}

    def add_flag(self, flag_name: str, flag_value: dict):
        if not isinstance(flag_name, str) or not isinstance(flag_value, dict):
            raise ValueError("Invalid input type for flag name or value")
        self._flags[flag_name] = flag_value

def test_invalid_input():
    flags = Flags()
    
    # Test adding a flag with invalid type for the flag name
    with pytest.raises(ValueError):
        flags.add_flag(123, {'value': True})  # Invalid type for flag_name (int)

    # Test adding a flag with invalid type for the flag value
    with pytest.raises(ValueError):
        flags.add_flag('my_flag', 'invalid_type')  # Invalid type for flag_value (str)
