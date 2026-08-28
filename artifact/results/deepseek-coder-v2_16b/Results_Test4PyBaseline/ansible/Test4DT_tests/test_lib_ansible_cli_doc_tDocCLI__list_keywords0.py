
import pytest
from ansible.cli.doc import DocCLI
import re
import pkgutil
from yaml import load as from_yaml

@pytest.fixture
def doc_cli():
    return DocCLI(args=['--list-modules'])  # Assuming args is a list containing the command-line argument for listing modules.

def test_init(doc_cli):
    assert isinstance(doc_cli, DocCLI)
    assert hasattr(doc_cli, 'plugin_list')