
import pytest
from io import StringIO
from unittest.mock import patch, MagicMock
from ansible.cli.vault import VaultCLI



def test_invalid_inputs():
    with pytest.raises(TypeError):
        VaultCLI()  # No arguments provided