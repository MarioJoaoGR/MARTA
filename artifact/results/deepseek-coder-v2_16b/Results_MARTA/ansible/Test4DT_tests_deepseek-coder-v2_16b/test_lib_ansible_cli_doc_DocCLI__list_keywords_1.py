
import pytest
from ansible.cli.doc import DocCLI

def test_valid_inputs():
    """Test that DocCLI initializes correctly with valid inputs."""
    args = ['arg1', 'arg2']  # Example of minimal valid arguments
    cli = DocCLI(args)
    assert isinstance(cli, DocCLI), "Expected an instance of DocCLI"
    assert hasattr(cli, 'plugin_list'), "Expected the object to have a plugin_list attribute"

def test_invalid_inputs():
    """Test that DocCLI raises ValueError when initialized with None."""
    with pytest.raises(ValueError):
        invalid_instance = DocCLI(None)
