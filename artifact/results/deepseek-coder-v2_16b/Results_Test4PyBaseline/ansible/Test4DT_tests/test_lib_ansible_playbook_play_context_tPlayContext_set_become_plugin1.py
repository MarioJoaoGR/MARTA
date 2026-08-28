
# Module: ansible.playbook.play_context
# test_play_context.py
from ansible.playbook.play_context import PlayContext

def test_set_become_plugin():
    context = PlayContext()
    assert hasattr(context, '_become_plugin') and context._become_plugin is None
    
    # Test setting a become plugin
    context.set_become_plugin('sudo')
    assert hasattr(context, '_become_plugin') and context._become_plugin == 'sudo'

def test_set_become_plugin_with_none():
    context = PlayContext()
    context.set_become_plugin(None)
    assert hasattr(context, '_become_plugin') and context._become_plugin is None

def test_set_become_plugin_multiple_times():
    context = PlayContext()
    context.set_become_plugin('sudo')
    assert hasattr(context, '_become_plugin') and context._become_plugin == 'sudo'
    
    # Setting it again should not change the value
    context.set_become_plugin('sudo')
    assert hasattr(context, '_become_plugin') and context._become_plugin == 'sudo'

def test_set_become_plugin_with_invalid():
    context = PlayContext()
    context.set_become_plugin('invalid_plugin')
    # The function should not raise an error or change the value if the plugin is invalid
    assert hasattr(context, '_become_plugin') and context._become_plugin == 'invalid_plugin'
