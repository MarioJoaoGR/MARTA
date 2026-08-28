
import pytest
from ansible.cli.console import ConsoleCLI

def test_valid_input_enable_check_mode():
    cli = ConsoleCLI(args={'host-pattern': 'app*.dc*'})
    assert cli.check_mode is None  # Initial state should be unset
    
    cli.do_check('yes')
    assert cli.check_mode is True

def test_edge_case_disable_check_mode():
    cli = ConsoleCLI(args={'host-pattern': 'app*.dc*'})
    assert cli.check_mode is None  # Initial state should be unset
    
    cli.do_check('no')
    assert cli.check_mode is False
