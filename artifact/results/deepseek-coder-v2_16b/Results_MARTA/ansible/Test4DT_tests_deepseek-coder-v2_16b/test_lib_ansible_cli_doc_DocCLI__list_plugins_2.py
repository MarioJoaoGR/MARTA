
import pytest
from ansible.cli.doc import DocCLI


def test_invalid_input():
    # Setup: Attempt to create an instance of DocCLI with no args
    with pytest.raises(ValueError):
        doc_cli = DocCLI([])