
import pytest
from ansible.cli.console import ConsoleCLI
import os

@pytest.fixture(scope="module")
def console_cli():
    return ConsoleCLI(args={'host-pattern': 'app_servers'})


def test_invalid_input_comment(console_cli):
    assert not console_cli.default('# This is a comment')

def test_no_host_found(console_cli):
    console_cli.cwd = None
    assert not console_cli.default('shell -a "yum update -y"')