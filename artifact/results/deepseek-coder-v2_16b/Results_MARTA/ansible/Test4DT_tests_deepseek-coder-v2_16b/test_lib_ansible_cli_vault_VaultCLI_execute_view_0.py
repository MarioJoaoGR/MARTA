
import pytest
from ansible.cli.vault import VaultCLI

@pytest.fixture(scope="module")
def edge_case_instance():
    return VaultCLI(args=None)


def test_edge_case():
    with pytest.raises(ValueError):
        VaultCLI(args=None)