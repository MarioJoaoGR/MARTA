
import pytest
from unittest.mock import patch, MagicMock
from tqdm.contrib.telegram import ttgrange

# Scenario 1: Basic usage with range in Python 3+
def test_ttgrange_basic():
    with patch('tqdm.contrib.telegram.tqdm_telegram') as mock_tqdm_telegram:
        for i in ttgrange(100, token='your_bot_token', chat_id='your_chat_id'):
            pass
    assert mock_tqdm_telegram.called

# Scenario 2: Using ttgrange with a custom progress bar description
def test_ttgrange_with_custom_description():
    with patch('tqdm.contrib.telegram.tqdm_telegram') as mock_tqdm_telegram:
        for i in ttgrange(100, token='your_bot_token', chat_id='your_chat_id', unit="it", desc="Processing items"):
            print(f"Processing item {i}")
    assert mock_tqdm_telegram.called

# Scenario 3: Using ttgrange with a different progress bar format
def test_ttgrange_with_different_format():
    with patch('tqdm.contrib.telegram.tqdm_telegram') as mock_tqdm_telegram:
        for i in ttgrange(100, token='your_bot_token', chat_id='your_chat_id', unit="it", desc="Processing items"):
            pass
    assert mock_tqdm_telegram.called
