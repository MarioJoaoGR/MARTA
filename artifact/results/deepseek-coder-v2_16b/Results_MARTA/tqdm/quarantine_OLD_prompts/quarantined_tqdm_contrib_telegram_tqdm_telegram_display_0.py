
import pytest
from unittest.mock import patch, MagicMock
from tqdm.contrib.telegram import tqdm_telegram

# Test for invalid inputs - missing token and chat_id
def test_invalid_inputs():
    with pytest.raises(TypeError):
        tqdm_telegram()

# Test for valid initialization with token and chat_id
@patch('tqdm.contrib.telegram.TelegramIO', autospec=True)
def test_valid_initialization(mock_telegramio):
    mock_instance = MagicMock()
    mock_telegramio.return_value = mock_instance
    
    tqdm_telegram(token='valid_token', chat_id='valid_chat_id')
    assert mock_telegramio.called_with('valid_token', 'valid_chat_id')

# Test for disabling the progress bar
@patch('tqdm.contrib.telegram.TelegramIO', autospec=True)
def test_disable_progress_bar(mock_telegramio):
    mock_instance = MagicMock()
    mock_telegramio.return_value = mock_instance
    
    tqdm_telegram(token='valid_token', chat_id='valid_chat_id', disable=True)
    assert not mock_telegramio.called

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
time exceeded
"""