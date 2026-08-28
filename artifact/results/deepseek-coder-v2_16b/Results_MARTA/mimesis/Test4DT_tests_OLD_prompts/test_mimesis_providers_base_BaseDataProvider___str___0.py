
import pytest
from unittest.mock import patch
from mimesis.providers.base import BaseDataProvider, locales

@pytest.fixture(autouse=True)
def mock_init():
    with patch('mimesis.providers.base.BaseDataProvider.__init__', lambda x: None):
        yield


def test_base_data_provider_specified_init():
    with pytest.raises(TypeError):
        BaseDataProvider(locale="en_US", seed=42)

def test_base_data_provider_str():
    with pytest.raises(TypeError):
        BaseDataProvider(locale="en_US", seed=42)