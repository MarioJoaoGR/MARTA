
import pytest
from ansible.cli.doc import DocCLI

def test_valid_inputs():
    with pytest.raises(ValueError):
        doccli = DocCLI([])

def test_edge_cases():
    with pytest.raises(ValueError):
        doccli = DocCLI([])

def test_invalid_inputs():
    with pytest.raises(ValueError):
        doccli = DocCLI([])
