
import pytest
from ansible.cli.doc import DocCLI

def test_edge_case():
    with pytest.raises(ValueError):
        doc_cli = DocCLI(None)
