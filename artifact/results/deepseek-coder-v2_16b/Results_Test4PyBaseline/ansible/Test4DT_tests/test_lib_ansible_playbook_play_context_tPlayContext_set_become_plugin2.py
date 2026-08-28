
# Module: ansible.playbook.play_context
# test_play_context.py
from ansible.playbook.play_context import PlayContext

def test_set_become_plugin():
    context = PlayContext()
    plugin = 'sudo'
    context.set_become_plugin(plugin)
    
    assert hasattr(context, '_become_plugin') and context._become_plugin == plugin, f"Expected _become_plugin to be set to {plugin}, but got {getattr(context, '_become_plugin', 'Not Set')}"

def test_set_become_plugin_with_none():
    context = PlayContext()
    context.set_become_plugin(None)
    