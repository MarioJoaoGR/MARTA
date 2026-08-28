
# Module: ansible.playbook.play_context
# test_play_context.py
from ansible.playbook.play_context import PlayContext

def test_basic_initialization():
    play_config = {'force_handlers': True}
    passwords = {'conn_pass': 'password123', 'become_pass': 'root'}
    context = PlayContext(play=play_config, passwords=passwords)
    
    assert hasattr(context, 'force_handlers') and context.force_handlers == True
    assert hasattr(context, 'password') and context.password == 'password123'
    assert hasattr(context, 'become_pass') and context.become_pass == 'root'

def test_initialization_with_cli_arguments():
    context = PlayContext(play={'force_handlers': True}, passwords={'conn_pass': 'password123', 'become_pass': 'root'})
    context.set_attributes_from_cli()  # Assuming CLI arguments are set accordingly
    
    assert hasattr(context, 'force_handlers') and context.force_handlers == True
    assert hasattr(context, 'password') and context.password == 'password123'
    assert hasattr(context, 'become_pass') and context.become_pass == 'root'

def test_initialization_without_passwords():
    context = PlayContext(play={'force_handlers': True})
    
    assert hasattr(context, 'force_handlers') and context.force_handlers == True
    assert hasattr(context, 'password') and context.password == ''
    assert hasattr(context, 'become_pass') and context.become_pass == ''

def test_initialization_with_connection_lock_file_descriptor():
    context = PlayContext(play={'force_handlers': True}, passwords={'conn_pass': 'password123', 'become_pass': 'root'}, connection_lockfd=10)
    
    assert hasattr(context, 'force_handlers') and context.force_handlers == True
    assert hasattr(context, 'password') and context.password == 'password123'
    assert hasattr(context, 'become_pass') and context.become_pass == 'root'
    assert hasattr(context, 'connection_lockfd') and context.connection_lockfd == 10

def test_set_become_plugin():
    context = PlayContext()
    context.set_become_plugin('sudo')
    
    assert hasattr(context, '_become_plugin') and context._become_plugin == 'sudo'
