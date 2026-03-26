
import pytest
from typing import Dict

class Flags:
    """Flags that map to parsed keys/namespaces."""
    FROZEN = 0
    EXPLICIT_NEST = 1

    def __init__(self) -> None:
        self._flags: Dict[str, dict] = {}

    def add_flag(self, name: str, details: dict):
        """Adds a new flag or updates an existing one."""
        if name in self._flags:
            raise ValueError(f"Flag '{name}' already exists.")
        self._flags[name] = details

def test_valid_input():
    flags = Flags()
    assert hasattr(flags, '_flags') and isinstance(flags._flags, dict)
    assert len(flags._flags) == 0
    
    # Adding a valid flag
    flags.add_flag('my_flag', {'value': True})
    assert 'my_flag' in flags._flags
    assert flags._flags['my_flag'] == {'value': True}

    # Attempting to add the same flag should raise an error
    with pytest.raises(ValueError):
        flags.add_flag('my_flag', {'value': False})
