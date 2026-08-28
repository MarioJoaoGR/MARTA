
import pytest
from unittest.mock import patch, MagicMock
from tqdm.contrib.telegram import TelegramIO




def test_exception_handling():
    with patch('tqdm.contrib.telegram.Session', side_effect=Exception("Mocked Exception")):
        with pytest.raises(Exception):
            TelegramIO(token='valid_token', chat_id='valid_chat_id')