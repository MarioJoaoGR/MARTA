
import pytest
from tqdm.contrib.telegram import tqdm_telegram
from unittest.mock import patch, MagicMock

def test_tqdm_telegram_init():
    iterable = []
    with patch('tqdm.contrib.telegram.TelegramIO', autospec=True) as mock_tgio:
        tqdm_instance = tqdm_telegram(iterable, token='test_token', chat_id='test_chat_id')
        assert isinstance(tqdm_instance, tqdm_telegram)
        mock_tgio.assert_called_once_with('test_token', 'test_chat_id')

