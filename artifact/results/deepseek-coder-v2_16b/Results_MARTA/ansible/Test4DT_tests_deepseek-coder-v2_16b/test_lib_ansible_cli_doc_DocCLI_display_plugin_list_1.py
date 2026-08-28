
import pytest
from ansible.cli.doc import DocCLI


def test_edge_cases():
    with pytest.raises(ValueError):
        DocCLI(args=None)
