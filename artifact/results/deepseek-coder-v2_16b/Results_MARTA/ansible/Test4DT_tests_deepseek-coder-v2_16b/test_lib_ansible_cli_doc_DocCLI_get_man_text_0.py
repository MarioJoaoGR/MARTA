
import pytest
from ansible.cli.doc import DocCLI



def test_invalid_input():
    with pytest.raises(ValueError):
        DocCLI(args=[])  # Assuming args is a list of arguments passed to the function