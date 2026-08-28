
import pytest
from unittest.mock import patch, MagicMock
from ansible.cli.adhoc import AdHocCLI



def test_invalid_inputs():
    with patch('ansible.cli.adhoc.AdHocCLI') as mock_cli:
        instance = mock_cli.return_value
        instance.parser = MagicMock()
        instance.parser.parse_args.side_effect = TypeError("Missing required options")
        
        with pytest.raises(TypeError):
            adhoc_cli = AdHocCLI()