# Module: tqdm.contrib.telegram
import pytest
from unittest.mock import patch, MagicMock
from tqdm.contrib.telegram import ttgrange
from tqdm import tqdm

# Mock the necessary functions and classes for testing
@patch('tqdm.contrib.telegram.tqdm_telegram')
@patch('tqdm.auto.range', lambda *args: range(*args))  # Use built-in range on Python 3+
def test_ttgrange(mock_tqdm):
    mock_instance = MagicMock()
    mock_tqdm.return_value = mock_instance
    
    # Test ttgrange with default arguments
    for i in ttgrange(100):
        pass
    assert mock_tqdm.called_once_with(range(100), {})
    
    # Test ttgrange with additional keyword arguments
    for i in ttgrange(100, desc="Processing", unit="item"):
        pass
    assert mock_tqdm.called_once_with(range(100), {'desc': 'Processing', 'unit': 'item'})
    
    # Test ttgrange with custom total items and description
    for i in ttgrange(200, desc="Custom Processing", unit="task"):
        pass
    assert mock_tqdm.called_once_with(range(200), {'desc': 'Custom Processing', 'unit': 'task'})

if __name__ == "__main__":
    pytest.main()
