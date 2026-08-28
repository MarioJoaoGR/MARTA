
import pytest
from ansible.cli.vault import VaultCLI

def test_invalid_inputs():
    with pytest.raises(ValueError) as excinfo:
        VaultCLI(args=[])
    assert str(excinfo.value) == 'A non-empty list for args is required'
