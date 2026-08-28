
import pytest
from ansible.cli.console import ConsoleCLI

@pytest.fixture(scope="module")
def console_instance():
    return ConsoleCLI(args={})


def test_edge_case():
    with pytest.raises(ValueError):
        cli = ConsoleCLI(args=None)