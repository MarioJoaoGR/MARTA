
import pytest
from ansible.cli.console import ConsoleCLI

def test_edge_case():
    args = None
    with pytest.raises(ValueError):
        ConsoleCLI(args)


