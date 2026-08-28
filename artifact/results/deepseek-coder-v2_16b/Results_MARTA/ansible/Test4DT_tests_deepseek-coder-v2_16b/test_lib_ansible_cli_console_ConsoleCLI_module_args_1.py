
import pytest
from ansible.cli.console import ConsoleCLI

def test_valid_input_cd_list():
    console = ConsoleCLI(args={'host-pattern': 'app_servers'})
    assert isinstance(console, ConsoleCLI)

def test_edge_case_none_input():
    with pytest.raises(ValueError):
        console = ConsoleCLI(args={})
