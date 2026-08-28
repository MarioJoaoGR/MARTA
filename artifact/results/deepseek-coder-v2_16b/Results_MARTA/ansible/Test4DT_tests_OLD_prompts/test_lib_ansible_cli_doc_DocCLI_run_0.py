
import pytest
from unittest.mock import patch, MagicMock
from ansible.cli.doc import DocCLI


def test_invalid_inputs():
    with patch('ansible.cli.doc.DocCLI') as MockDocCLI:
        mock_incorrect_args = ['invalid_arg']
        with pytest.raises(TypeError):
            DocCLI(mock_incorrect_args)