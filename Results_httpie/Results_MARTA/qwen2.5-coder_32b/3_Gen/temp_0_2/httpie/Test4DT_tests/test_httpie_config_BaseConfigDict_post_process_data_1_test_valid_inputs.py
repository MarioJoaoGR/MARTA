
import pytest
from unittest.mock import patch, MagicMock
from httpie.config import BaseConfigDict

def test_post_process_data():
    config = BaseConfigDict(path=MagicMock())
    data = {'key': 'value'}
    
    processed_data = config.post_process_data(data)
    
    assert processed_data == {'key': 'value'}
