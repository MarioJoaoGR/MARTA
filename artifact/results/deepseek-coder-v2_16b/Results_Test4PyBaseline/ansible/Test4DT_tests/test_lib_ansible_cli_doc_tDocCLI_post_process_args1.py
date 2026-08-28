
# Module: ansible.cli.doc
# test_doccli.py
from ansible.cli.doc import DocCLI
import pytest

@pytest.fixture
def cli():
    return DocCLI(args=['--list-modules'])  # Initialize with a list of arguments for testing

def test_init(cli):
    assert isinstance(cli, DocCLI)
    assert hasattr(cli, 'plugin_list')