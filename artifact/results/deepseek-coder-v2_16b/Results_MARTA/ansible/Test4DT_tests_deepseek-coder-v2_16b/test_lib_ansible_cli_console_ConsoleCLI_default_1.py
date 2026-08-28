
import pytest
from ansible.cli.console import ConsoleCLI
import os

@pytest.fixture(scope="module")
def cli():
    return ConsoleCLI(args={'host-pattern': 'app_servers'})


def test_invalid_input_comment(cli):
    assert cli.default('# This is a comment') is False

def test_list_hosts(cli):
    with pytest.raises(TypeError):
        cli.default('list')