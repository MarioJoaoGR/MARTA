
import pytest
from thefuck.shells.generic import Generic

# Test initialization of Generic class
def test_generic_initialization():
    generic_instance = Generic()
    assert hasattr(generic_instance, 'friendly_name')
    assert generic_instance.friendly_name == 'Generic Shell'

# Test _get_version method
def test_get_version():
    generic_instance = Generic()
    version = generic_instance._get_version()
    assert version == ''

# Test info method with successful version retrieval
@pytest.mark.parametrize("mock_version, expected", [("", "Generic Shell"), ("1.2.3", "Generic Shell 1.2.3")])
def test_info_with_version(monkeypatch, mock_version, expected):
    def mock__get_version():
        return mock_version
    monkeypatch.setattr(Generic, '_get_version', mock__get_version)
    
    generic_instance = Generic()
    info_str = generic_instance.info()