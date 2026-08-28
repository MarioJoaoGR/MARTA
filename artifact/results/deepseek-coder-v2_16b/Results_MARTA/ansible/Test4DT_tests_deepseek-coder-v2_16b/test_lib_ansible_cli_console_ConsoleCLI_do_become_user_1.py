
import pytest
from ansible.cli.console import ConsoleCLI

# Test for valid input to become_user command

# Test for edge case where no input is provided to become_user command
def test_edge_case_become_user():
    cli = ConsoleCLI(args={'host-pattern': 'app*.dc*'})
    with pytest.raises(Exception):
        cli.do_become_user('')
    assert cli.become_user is None

# Test for invalid input to become_user command