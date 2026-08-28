
import pytest
from ansible.cli.console import ConsoleCLI
import os
import readline
import atexit
from unittest.mock import patch

@pytest.fixture(scope="module")
def console_cli():
    return ConsoleCLI(args={'host-pattern': 'app*.dc*'})

def test_run_command(console_cli):
    with pytest.raises(KeyError):
        console_cli.run()

def test_list_modules(console_cli):
    with pytest.raises(KeyError):
        modules = console_cli.list_modules()
