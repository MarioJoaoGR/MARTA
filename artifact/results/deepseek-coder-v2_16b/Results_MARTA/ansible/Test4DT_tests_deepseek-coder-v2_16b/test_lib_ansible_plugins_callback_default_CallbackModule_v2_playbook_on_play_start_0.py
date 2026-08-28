
import pytest
from unittest.mock import patch
from ansible.plugins.callback.default import CallbackModule

class MockPlay:
    def __init__(self, name=None):
        self.name = name
        self.check_mode = False

    def get_name(self):
        return self.name or ""

    def check_mode(self):
        return self.check_mode



def test_error_case():
    callback_module = CallbackModule()
    with pytest.raises(AttributeError):
        callback_module.v2_playbook_on_play_start(None)