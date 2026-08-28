
import pytest
from ansible.parsing.mod_args import ModuleArgsParser

# Define valid task data and collection list for testing
valid_task_ds = {'action': 'copy src=a dest=b'}
valid_collection_list = ['ansible.builtin']

def test_valid_input():
    parser = ModuleArgsParser(task_ds=valid_task_ds, collection_list=valid_collection_list)
    action, args, delegate_to = parser.parse()
    
    assert action == 'copy'
    assert args == {'src': 'a', 'dest': 'b'}
