
import pytest
from ansible.cli.playbook import PlaybookCLI

@pytest.fixture(scope="module")
def playbook_cli():
    return PlaybookCLI()


def test_edge_cases():
    with pytest.raises(TypeError):
        PlaybookCLI()