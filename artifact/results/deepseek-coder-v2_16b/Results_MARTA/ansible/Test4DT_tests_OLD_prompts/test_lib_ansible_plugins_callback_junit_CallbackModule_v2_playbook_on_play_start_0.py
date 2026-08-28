
import os
from unittest.mock import patch
from ansible.plugins.callback.junit import CallbackModule


def test_playbook_on_play_start():
    with patch('ansible.plugins.callback.junit.os.getenv', return_value='default_dir'):
        callback = CallbackModule()
        play_name = "test_play"
        callback._play_name = play_name  # Simulate the play start event
        assert callback._play_name == play_name