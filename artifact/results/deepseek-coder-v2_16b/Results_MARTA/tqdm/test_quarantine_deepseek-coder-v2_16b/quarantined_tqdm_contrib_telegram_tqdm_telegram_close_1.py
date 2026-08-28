
import pytest
from tqdm.contrib.telegram import tqdm_telegram
from unittest.mock import patch, MagicMock

def test_invalid_inputs():
    iterable = range(10)
    with pytest.raises(ValueError):
        tqdm_telegram(iterable, token='test_token', chat_id=None)

def test_edge_cases():
    iterable = []
    with patch('tqdm.contrib.telegram.TelegramIO', autospec=True) as mock_tgio:
        tqdm_instance = tqdm_telegram(iterable, token='test_token', chat_id='test_chat_id')
        assert isinstance(tqdm_instance, tqdm_telegram)
        mock_tgio.assert_not_called()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
time exceeded
"""