
# Module: ansible.parsing.mod_args
# test_module_args_parser.py
from ansible.parsing.mod_args import ModuleArgsParser
import pytest
from unittest.mock import patch  # Assuming this is the correct way to mock in your environment

@pytest.fixture
def parser():
    return ModuleArgsParser(task_ds={'module': 'copy', 'args': {'src': 'a', 'dest': 'b'}})

def test_basic_usage(parser):
    assert parser._task_ds == {'module': 'copy', 'args': {'src': 'a', 'dest': 'b'}}

def test_legacy_form():
    parser = ModuleArgsParser(task_ds={'action': {'module': 'shell', 'args': {'cmd': 'echo hi'}}})
    assert parser._task_ds == {'module': 'shell', 'args': {'cmd': 'echo hi'}}

def test_shorthand_local_action():
    parser = ModuleArgsParser(task_ds={'local_action': 'shell echo hi'})
    assert parser._task_ds == {'module': 'shell', 'args': {'cmd': 'echo hi'}}

def test_complex_args_form():
    parser = ModuleArgsParser(task_ds={'copy': {'src': 'a', 'dest': 'b'}})
    assert parser._task_ds == {'module': 'copy', 'args': {'src': 'a', 'dest': 'b'}}

def test_standard_yaml_form():
    parser = ModuleArgsParser(task_ds={'action': {'module': 'copy', 'args': {'src': 'a', 'dest': 'b'}}})
    assert parser._task_ds == {'module': 'copy', 'args': {'src': 'a', 'dest': 'b'}}

def test_gross_but_legal_form():
    parser = ModuleArgsParser(task_ds={'action': {'module': 'copy', 'args': {'src': 'a', 'dest': 'b'}}})
    assert parser._task_ds == {'module': 'copy', 'args': {'src': 'a', 'dest': 'b'}}

def test_invalid_type():
    with pytest.raises(AssertionError):  # Assuming this is the correct error to raise
        ModuleArgsParser(task_ds={'module': 'copy', 'args': ['a', 'b']})

def test_normalize_old_style_args_dict():
    parser = ModuleArgsParser()
    action, args = parser._normalize_old_style_args({'module': 'shell', 'args': {'cmd': 'echo hi'}})
    assert action == 'shell' and args == {'cmd': 'echo hi'}

def test_normalize_old_style_args_string():
    parser = ModuleArgsParser()
    action, args = parser._normalize_old_style_args('shell echo hi')
    assert action == 'shell' and args == {'cmd': 'echo hi'}
