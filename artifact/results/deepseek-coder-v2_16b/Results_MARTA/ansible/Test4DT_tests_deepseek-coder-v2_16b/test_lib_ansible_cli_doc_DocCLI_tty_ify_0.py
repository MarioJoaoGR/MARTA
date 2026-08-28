
import pytest
from ansible.cli.doc import DocCLI

def test_valid_input():
    with pytest.raises(ValueError) as excinfo:
        doc_cli = DocCLI([])
    assert str(excinfo.value) == "A non-empty list for args is required"

def test_edge_case():
    with pytest.raises(ValueError) as excinfo:
        doc_cli = DocCLI([])
    assert str(excinfo.value) == "A non-empty list for args is required"
