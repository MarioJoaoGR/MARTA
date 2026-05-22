
import pytest
from unittest.mock import patch, MagicMock
from httpie.config import BaseConfigDict

def test_pre_process_data():
    config = BaseConfigDict(path='some/file/path')
    
    # Test with a dictionary containing string values
    data = {'option1': 'value1', 'option2': 'value2'}
    processed_data = config.pre_process_data(data)
    assert processed_data == {'option1': 'value1', 'option2': 'value2'}
    
    # Test with a dictionary containing non-string values
    data = {'option1': 1, 'option2': True}
    processed_data = config.pre_process_data(data)
    assert processed_data == {'option1': 1, 'option2': True}
    
    # Test with an empty dictionary
    data = {}
    processed_data = config.pre_process_data(data)
    assert processed_data == {}
