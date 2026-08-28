
import pytest
from ansible.cli.doc import DocCLI

@pytest.fixture
def doccli():
    return DocCLI(args=['--list-modules'])  # Assuming args is a list containing the command-line argument for listing modules.

# Test initialization of DocCLI
def test_init(doccli):
    assert isinstance(doccli, DocCLI)
    assert hasattr(doccli, 'plugin_list')