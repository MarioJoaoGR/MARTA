
import pytest
from unittest.mock import patch, MagicMock
from semantic_release.hvcs import get_domain, ImproperConfigurationError

# Test with a valid hvcs configuration in the config file
def test_valid_hvcs_configuration():
    with patch('semantic_release.hvcs.get_hvcs', return_value=MagicMock(domain=lambda: 'example.com')):
        assert get_domain() == 'example.com'

# Test when no hvcs configuration is provided
def test_missing_hvcs_configuration():
    with patch('semantic_release.hvcs.get_hvcs', side_effect=ImproperConfigurationError("No HVCS configured")):
        with pytest.raises(ImproperConfigurationError):
            get_domain()

# Test with an invalid hvcs configuration in the config file
def test_invalid_hvcs_configuration():
    with patch('semantic_release.hvcs.get_hvcs', side_effect=ImproperConfigurationError("Invalid HVCS helper class")):
        with pytest.raises(ImproperConfigurationError):
            get_domain()
