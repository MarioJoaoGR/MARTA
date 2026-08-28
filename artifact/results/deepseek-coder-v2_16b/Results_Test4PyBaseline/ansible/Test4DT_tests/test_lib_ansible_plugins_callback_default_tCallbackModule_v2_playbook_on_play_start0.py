
import pytest
from ansible.plugins.callback.default import CallbackModule

# Test Case 1: Play with no name and in normal mode
def test_v2_playbook_on_play_start_no_name():
    callback = CallbackModule()
    play = type('Play', (object,), {'get_name': lambda self: '', 'check_mode': False})()
    callback.v2_playbook_on_play_start(play)
    assert callback._display.banner.call_args[0][0] == "PLAY"

# Test Case 2: Play with no name and in check mode
def test_v2_playbook_on_play_start_no_name_check_mode():
    callback = CallbackModule()
    play = type('Play', (object,), {'get_name': lambda self: '', 'check_mode': True})()
    callback.v2_playbook_on_play_start(play)
    assert callback._display.banner.call_args[0][0] == "PLAY [CHECK MODE]"

# Test Case 3: Play with name and in normal mode
def test_v2_playbook_on_play_start_with_name():
    callback = CallbackModule()
    play = type('Play', (object,), {'get_name': lambda self: 'example_play', 'check_mode': False})()
    callback.v2_playbook_on_play_start(play)
    assert callback._display.banner.call_args[0][0] == "PLAY [example_play]"

# Test Case 4: Play with name and in check mode
def test_v2_playbook_on_play_start_with_name_check_mode():
    callback = CallbackModule()
    play = type('Play', (object,), {'get_name': lambda self: 'example_play', 'check_mode': True})()
    callback.v2_playbook_on_play_start(play)
    assert callback._display.banner.call_args[0][0] == "PLAY [example_play] [CHECK MODE]"
