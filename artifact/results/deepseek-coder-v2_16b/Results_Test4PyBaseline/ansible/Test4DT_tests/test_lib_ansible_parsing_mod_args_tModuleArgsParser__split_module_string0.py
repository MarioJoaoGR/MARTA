# Module: ansible.parsing.mod_args
import pytest
from ansible.parsing.mod_args import ModuleArgsParser
from ansible.errors import AnsibleAssertionError

# Test initialization with a simple module and args
def test_init_with_simple_module():
    parser = ModuleArgsParser(task_ds={'module': 'copy', 'args': {'src': 'a', 'dest': 'b'}})
    assert parser._task_ds == {'module': 'copy', 'args': {'src': 'a', 'dest': 'b'}}

# Test initialization with a more complex argument structure
def test_init_with_complex_args():
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

# Test initialization with a standard YAML form for command-type modules
def test_init_with_yaml_form():
    parser = ModuleArgsParser(task_ds={
        'command': 'pwd',
        'args': {
            'chdir': '/tmp'
        }
    })
    assert parser._task_ds == {'command': 'pwd', 'args': {'chdir': '/tmp'}}

# Test initialization with an invalid task_ds type
def test_init_with_invalid_type():
    with pytest.raises(AnsibleAssertionError) as e:
        ModuleArgsParser(task_ds='invalid_type')
    assert str(e.value) == "the type of 'task_ds' should be a dict, but is a <class 'str'>"

# Test _split_module_string method with a valid module string
def test_split_module_string():
    parser = ModuleArgsParser()
    module_name, args_str = parser._split_module_string('copy src=a dest=b')
    assert module_name == 'copy' and args_str == 'src=a dest=b'

# Test _split_module_string method with a single token string
def test_split_module_string_single_token():
    parser = ModuleArgsParser()
    module_name, args_str = parser._split_module_string('copy')
    assert module_name == 'copy' and args_str == ''
