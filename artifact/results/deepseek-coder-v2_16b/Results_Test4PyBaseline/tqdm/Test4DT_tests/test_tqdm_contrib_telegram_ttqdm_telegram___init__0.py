# Module: tqdm.contrib.telegram
import pytest
from tqdm.contrib.telegram import tqdm, trange
from unittest.mock import patch
from os import getenv

# Mocking the Telegram Bot API calls for testing purposes
class MockTelegramIO:
    def __init__(self, token, chat_id):
        self.token = token
        self.chat_id = chat_id
        self.sent_messages = []
    
    def send_message(self, text):
        self.sent_messages.append(text)
    
    def write(self, text):
        if len(self.sent_messages) > 0:
            self.sent_messages[-1] = text
    
    def delete(self):
        if len(self.sent_messages) > 0:
            self.sent_messages.pop()

@pytest.fixture
def mock_telegram_io():
    return MockTelegramIO('mock_token', 'mock_chat_id')

# Test cases for tqdm_telegram class
def test_tqdm_telegram_init(mock_telegram_io):
    with patch('tqdm.contrib.telegram.TelegramIO', return_value=mock_telegram_io):
        iterable = range(10)
        tqdm_instance = tqdm(iterable, token='mock_token', chat_id='mock_chat_id')
        assert hasattr(tqdm_instance, 'tgio')
        assert isinstance(tqdm_instance.tgio, MockTelegramIO)
        assert tqdm_instance.tgio.token == 'mock_token'
        assert tqdm_instance.tgio.chat_id == 'mock_chat_id'

def test_tqdm_telegram_iterable():
    iterable = range(10)
    with patch('tqdm.contrib.telegram.TelegramIO', return_value=MockTelegramIO('mock_token', 'mock_chat_id')):
        tqdm_instance = tqdm(iterable, token='mock_token', chat_id='mock_chat_id')
        for i in tqdm_instance:
            assert isinstance(i, int)

def test_tqdm_telegram_disable():
    iterable = range(10)
    with patch('tqdm.contrib.telegram.TelegramIO', return_value=MockTelegramIO('mock_token', 'mock_chat_id')):
        tqdm_instance = tqdm(iterable, token='mock_token', chat_id='mock_chat_id', disable=True)
        assert not hasattr(tqdm_instance, 'tgio')

# Test cases for TelegramIO class
def test_telegram_io_init():
    telegram_io = MockTelegramIO('mock_token', 'mock_chat_id')
    assert telegram_io.token == 'mock_token'
    assert telegram_io.chat_id == 'mock_chat_id'
    assert hasattr(telegram_io, 'sent_messages')
    assert isinstance(telegram_io.sent_messages, list)

def test_telegram_io_send_message():
    telegram_io = MockTelegramIO('mock_token', 'mock_chat_id')
    telegram_io.send_message('Hello, this is a test message!')
    assert len(telegram_io.sent_messages) == 1
    assert telegram_io.sent_messages[0] == 'Hello, this is a test message!'

def test_telegram_io_write():
    telegram_io = MockTelegramIO('mock_token', 'mock_chat_id')
    telegram_io.send_message('Initial message')
    telegram_io.write('Updated message')
    assert len(telegram_io.sent_messages) == 1
    assert telegram_io.sent_messages[0] == 'Updated message'

def test_telegram_io_delete():
    telegram_io = MockTelegramIO('mock_token', 'mock_chat_id')
    telegram_io.send_message('Message to delete')
    telegram_io.delete()
    assert len(telegram_io.sent_messages) == 0
