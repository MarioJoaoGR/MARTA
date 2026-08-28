
import pytest
from ansible.cli.console import ConsoleCLI
import cmd
import getpass
import os

@pytest.fixture(scope="module")
def cli():
    return ConsoleCLI(args={'host-pattern': 'app*.dc*'})


def test_edge_case():
    with pytest.raises(ValueError) as excinfo:
        ConsoleCLI(args=None)
    assert str(excinfo.value) == 'A non-empty list for args is required'
