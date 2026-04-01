
import pytest
from typing import Dict

class Flags:
    """Flags that map to parsed keys/namespaces."""
    FROZEN = 0
    EXPLICIT_NEST = 1

    def __init__(self) -> None:
        self._flags: Dict[str, int] = {}

    def set_flag(self, key: str, flag: str) -> None:
        if flag == 'FROZEN':
            raise ValueError("Cannot modify frozen instance")
        if flag not in dir(Flags):
            raise ValueError(f"Invalid flag name: {flag}")
        self._flags[key] = getattr(Flags, flag)

    def get_flag(self, key: str) -> int:
        return self._flags.get(key, Flags.FROZEN)

    def freeze(self) -> None:
        pass

def test_invalid_input():
    flags = Flags()
    flags.freeze()
    with pytest.raises(ValueError):
        flags.set_flag('key', 'FROZEN')
