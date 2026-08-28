
import pytest
from ansible.playbook.play_context import PlayContext

def test_set_become_plugin():
    play_context = PlayContext()
    plugin = "MyBecomePlugin"
    play_context.set_become_plugin(plugin)
    assert hasattr(play_context, '_become_plugin')
    assert play_context._become_plugin == plugin
