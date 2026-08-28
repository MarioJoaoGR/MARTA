
import pytest
from ansible.cli.console import ConsoleCLI
import cmd
import os
import getpass

@pytest.fixture(scope="module")
def console_instance():
    args = {'host-pattern': 'app*.dc*'}
    return ConsoleCLI(args)

def test_valid_input_cd_pattern(console_instance):
    with pytest.raises(AttributeError):
        console_instance.onecmd('cd app*.dc*')

def test_edge_case_none_input(console_instance):
    with pytest.raises(AttributeError):
        console_instance.onecmd('cd')

def test_invalid_input_cd_pattern(console_instance):
    with pytest.raises(AttributeError):
        console_instance.onecmd('cd nonexistent*')
