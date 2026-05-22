
import pytest
from pathlib import Path
from unittest.mock import patch, MagicMock
from httpie.config import BaseConfigDict

@pytest.fixture
def base_config():
    return BaseConfigDict(path=Path('/some/file/path'))

def test_post_process_data_default(base_config):
    data = {'key': 'value'}
    processed_data = base_config.post_process_data(data)
    assert processed_data == data

@patch('httpie.config.BaseConfigDict.post_process_data')
def test_post_process_data_custom(mock_post_process, base_config):
    mock_post_process.return_value = {'key': 'value', 'custom_key': 'custom_value'}
    processed_data = base_config.post_process_data({'key': 'value'})
    assert processed_data == {'key': 'value', 'custom_key': 'custom_value'}
