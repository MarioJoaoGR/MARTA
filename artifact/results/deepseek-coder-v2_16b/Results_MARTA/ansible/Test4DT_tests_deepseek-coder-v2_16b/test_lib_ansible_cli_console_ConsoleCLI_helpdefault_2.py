
import pytest
from ansible.cli.console import ConsoleCLI

def test_edge_case_list_groups():
    args = {}
    with pytest.raises(ValueError):
        console_cli = ConsoleCLI(args)
