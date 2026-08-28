
import pytest
from tqdm.contrib.telegram import tqdm, trange
from unittest.mock import patch
from io import StringIO

# Assuming you have obtained a valid bot token and chat ID from Telegram BotFather and your interactions with the bot
BOT_TOKEN = 'your_bot_token'
CHAT_ID = 'your_chat_id'

@pytest.fixture(autouse=True)
def mock_telegram_io():
    with patch('tqdm.contrib.telegram.TelegramIO') as mock_tg:
        yield mock_tg

def test_tqdm_with_iterable():
    iterable = [1, 2, 3, 4, 5]
    progress_bar = tqdm(iterable, token=BOT_TOKEN, chat_id=CHAT_ID)
    assert hasattr(progress_bar, 'tgio'), "Expected `tgio` attribute to be set"

def test_trange():
    with patch('sys.stdout', new=StringIO()) as fake_output:
        for i in trange(100, token=BOT_TOKEN, chat_id=CHAT_ID):
            pass