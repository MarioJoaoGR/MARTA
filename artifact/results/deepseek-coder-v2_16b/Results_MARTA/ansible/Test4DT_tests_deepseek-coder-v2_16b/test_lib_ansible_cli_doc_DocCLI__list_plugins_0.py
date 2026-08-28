
import pytest
from ansible.cli.doc import DocCLI


def test_invalid_input():
    # Setup: Attempt to create a DocCLI without any arguments
    with pytest.raises(ValueError) as excinfo:
        doc_cli = DocCLI([])
    assert str(excinfo.value) == 'A non-empty list for args is required', "Expected ValueError message"