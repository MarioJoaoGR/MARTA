
import pytest
from pathlib import Path
from unittest.mock import patch, MagicMock
from httpie.config import BaseConfigDict

def test_valid_inputs():
    with patch('httpie.config.BaseConfigDict', autospec=True):
        config = BaseConfigDict(path=Path('/some/file/path'))
        assert isinstance(config, BaseConfigDict)
        assert config.path == Path('/some/file/path')
        
        # Test post_process_data method
        data = {'key': 'value'}
        processed_data = config.post_process_data(data)
        assert processed_data == data
