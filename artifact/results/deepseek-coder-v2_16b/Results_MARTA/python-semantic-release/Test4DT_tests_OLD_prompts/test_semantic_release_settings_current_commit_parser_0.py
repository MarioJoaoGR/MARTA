
import pytest
from unittest.mock import MagicMock, patch
from semantic_release.settings import current_commit_parser
from semantic_release import ImproperConfigurationError

def test_none_configuration():
    config = None
    
    with pytest.raises(ImproperConfigurationError):
        current_commit_parser()

def test_invalid_configuration():
    config = {'commit_parser': 'nonexistentmodule.parse_function'}
    
    with pytest.raises(ImproperConfigurationError):
        current_commit_parser()

def test_mocked_invalid_configuration():
    config = {'commit_parser': 'nonexistentmodule.parse_function'}
    
    with patch('semantic_release.settings.current_commit_parser', MagicMock(side_effect=ImproperConfigurationError("Unable to import parser"))):
        with pytest.raises(ImproperConfigurationError):
            current_commit_parser()
