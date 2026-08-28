
import pytest
from ansible.cli.console import ConsoleCLI


def test_edge_case_empty_list():
    with pytest.raises(ValueError):
        ConsoleCLI(args={})
