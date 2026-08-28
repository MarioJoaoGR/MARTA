
import pytest
from ansible.parsing.mod_args import ModuleArgsParser
from ansible.errors import AnsibleAssertionError

# Test initialization with a basic task definition dictionary
def test_init_with_basic_task_definition():
    parser = ModuleArgsParser(task_ds={'module': 'copy', 'args': {'src': 'a', 'dest': 'b'}})
    assert parser._task_ds == {'module': 'copy', 'args': {'src': 'a', 'dest': 'b'}}

# Test initialization with a more complex YAML-like structure in the task definition
def test_init_with_complex_yaml_structure():
    parser = ModuleArgsParser(task_ds={
        'action': {
            'module': 'copy',
            'args': {
                'src': 'a',
                'dest': 'b'
            }
        }
    })
    assert parser._task_ds == {'action': {'module': 'copy', 'args': {'src': 'a', 'dest': 'b'}}}

# Test initialization with a legacy form for a shell command
def test_init_with_legacy_form():
    parser = ModuleArgsParser(task_ds={'action': 'shell echo hi'})
    assert parser._task_ds == {'action': 'shell echo hi'}

# Test initialization with a shorthand local action
def test_init_with_shorthand_local_action():
    parser = ModuleArgsParser(task_ds={'local_action': 'shell echo hi'})
    assert parser._task_ds == {'local_action': 'shell echo hi'}

# Test initialization with a task definition dictionary and a collection list
def test_init_with_collection_list():
    parser = ModuleArgsParser(task_ds={'module': 'copy', 'args': {'src': 'a', 'dest': 'b'}}, collection_list=['ansible.posix'])
    assert parser._collection_list == ['ansible.posix']

# Test initialization with a task definition dictionary and no collection list provided
def test_init_without_collection_list():
    parser = ModuleArgsParser(task_ds={'module': 'copy', 'args': {'src': 'a', 'dest': 'b'}})
    assert parser._collection_list is None

# Test initialization with a task definition dictionary and an invalid type for task_ds
def test_init_with_invalid_type_for_task_ds():
    with pytest.raises(AnsibleAssertionError) as excinfo:
        ModuleArgsParser(task_ds='not a dict')
    assert "the type of 'task_ds' should be a dict, but is a <class 'str'>" in str(excinfo.value)

# Test parsing a task definition with legacy form
def test_parse_legacy_form():
    parser = ModuleArgsParser(task_ds={'action': 'shell echo hi'})
    parsed_action, parsed_args, delegate_to = parser.parse()
    assert parsed_action == 'shell'