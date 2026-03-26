
import pytest
from isort.setuptools_commands import ISortCommand
from unittest.mock import patch, MagicMock

@pytest.mark.parametrize("invalid_input", [None, 123, {}])
def test_invalid_input(invalid_input):
    with patch('isort.setuptools_commands.ISortCommand') as mock_class:
        mock_instance = mock_class.return_value
        mock_instance.finalize_options.side_effect = TypeError("Invalid input type")
        
        with pytest.raises(TypeError) as excinfo:
            mock_instance.finalize_options()
            
        assert str(excinfo.value) == "Invalid input type"
