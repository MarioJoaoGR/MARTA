
import pytest
from ansible.cli.console import ConsoleCLI

def test_edge_case_empty_timeout():
    with pytest.raises(ValueError) as excinfo:
        cli = ConsoleCLI(args={})
    assert str(excinfo.value) == 'A non-empty list for args is required'
