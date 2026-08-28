
import pytest
from ansible.cli.console import ConsoleCLI


def test_edge_case_empty_args():
    with pytest.raises(ValueError) as excinfo:
        ConsoleCLI(args={})
    assert str(excinfo.value) == 'A non-empty list for args is required', "Expected ValueError when initializing with empty args"
