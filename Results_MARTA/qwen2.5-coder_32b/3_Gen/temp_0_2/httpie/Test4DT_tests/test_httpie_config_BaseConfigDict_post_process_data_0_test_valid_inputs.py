
import pytest
from httpie.config import BaseConfigDict
from unittest.mock import patch, MagicMock
from typing import Dict, Any

@pytest.fixture
def base_config():
    return BaseConfigDict(path=MagicMock())

def test_post_process_data_default(base_config):
    data = {'key': 'value'}
    assert base_config.post_process_data(data) == data

@patch('httpie.config.BaseConfigDict.post_process_data')
def test_post_process_data_custom(mock_post_process, base_config):
    mock_post_process.return_value = {'key': 'value', 'additional_key': 'additional_value'}
    assert base_config.post_process_data({'key': 'value'}) == {'key': 'value', 'additional_key': 'additional_value'}
