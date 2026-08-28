
import pytest
from ansible.parsing.mod_args import ModuleArgsParser
from ansible.errors import AnsibleAssertionError, AnsibleParserError

# Test cases for the parse method of ModuleArgsParser class
def test_parse_basic():
    parser = ModuleArgsParser(task_ds={'module': 'copy', 'args': {'src': 'file.txt', 'dest': 'backup/'}})
    action, args, delegate_to = parser.parse()
    assert action == 'copy'
    assert args == {'_raw_params': 'src=file.txt dest=backup/', '_uses_shell': True}
    assert delegate_to is None

def test_parse_local_action():
    parser = ModuleArgsParser(task_ds={'local_action': 'shell echo hi'})
    action, args, delegate_to = parser.parse()
    assert action == 'shell'
    assert args == {'_raw_params': 'echo hi', '_uses_shell': True}
    assert delegate_to == 'localhost'

def test_parse_complex_args():
    parser = ModuleArgsParser(task_ds={'copy': {'src': 'file.txt', 'dest': 'backup/'}})
    action, args, delegate_to = parser.parse()
    assert action == 'copy'
    assert args == {'src': 'file.txt', 'dest': 'backup/'}
    assert delegate_to is None

def test_parse_yaml_like_structure():
    parser = ModuleArgsParser(task_ds={
        'action': {
            'module': 'copy',
            'args': {'src': 'file.txt', 'dest': 'backup/'}
        }
    })
    action, args, delegate_to = parser.parse()
    assert action == 'copy'
    assert args == {'src': 'file.txt', 'dest': 'backup/'}
    assert delegate_to is None

def test_parse_skip_action_validation():
    parser = ModuleArgsParser(task_ds={'action': 'copy', 'args': {'src': 'file.txt', 'dest': 'backup/'}}, collection_list=['ansible.builtin'])
    action, args, delegate_to = parser.parse(skip_action_validation=True)
    assert action == 'copy'
    assert args == {'src': 'file.txt', 'dest': 'backup/'}
    assert delegate_to is None

def test_parse_invalid_task_ds():
    with pytest.raises(AnsibleAssertionError):
        parser = ModuleArgsParser(task_ds={'module': 'copy', 'args': {'src': 'file.txt', 'dest': 'backup/'}})
        action, args, delegate_to = parser.parse()
