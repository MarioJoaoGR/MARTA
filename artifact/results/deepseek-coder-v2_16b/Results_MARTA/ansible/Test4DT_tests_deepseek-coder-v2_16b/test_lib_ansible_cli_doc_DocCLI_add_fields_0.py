
import pytest
from ansible.cli.doc import DocCLI

def test_edge_case():
    # Setup: None
    with pytest.raises(ValueError):
        doc_cli = DocCLI(args=None)
