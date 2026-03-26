
import pytest
from typing import Dict

class Flags:
    """Flags that map to parsed keys/namespaces."""
    FROZEN = 0
    EXPLICIT_NEST = 1

    def __init__(self) -> None:
        self._flags: Dict[str, dict] = {}

def test_valid_case():
    flags = Flags()
    assert hasattr(flags, '_flags')
    assert isinstance(flags._flags, dict)
    assert len(flags._flags) == 0
