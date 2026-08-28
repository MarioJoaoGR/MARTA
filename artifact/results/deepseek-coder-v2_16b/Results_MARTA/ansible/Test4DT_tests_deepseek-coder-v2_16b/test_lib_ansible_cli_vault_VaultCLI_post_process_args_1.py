
import pytest
from ansible.cli.vault import VaultCLI



def test_invalid_inputs():
    with pytest.raises(ValueError):
        VaultCLI(args=[])