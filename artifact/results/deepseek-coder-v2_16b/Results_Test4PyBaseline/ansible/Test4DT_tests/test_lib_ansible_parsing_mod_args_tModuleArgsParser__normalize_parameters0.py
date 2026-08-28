
# Module: ansible.parsing.mod_args
# test_module_args_parser.py
from ansible.parsing.mod_args import ModuleArgsParser
import pytest
from unittest.mock import patch

def test_init():
    # Test initialization with default values
    parser = ModuleArgsParser()
    assert parser._task_ds == {}
    assert parser._collection_list is None
    assert isinstance(parser._task_attrs, frozenset)
    assert not parser.resolved_action

def test_init_with_task_ds():
    # Test initialization with a task dictionary
    task_ds = {'module': 'copy', 'args': {'src': 'a', 'dest': 'b'}}
    parser = ModuleArgsParser(task_ds=task_ds)
    assert parser._task_ds == task_ds
    assert parser._collection_list is None
    assert isinstance(parser._task_attrs, frozenset)
    assert not parser.resolved_action

def test_init_with_invalid_type():
    # Test initialization with an invalid type for task_ds
    with pytest.raises(AssertionError):  # Corrected the error name to match Python's built-in AssertionError
        ModuleArgsParser(task_ds="not a dictionary")

def test_normalize_parameters_string():
    # Test normalizing parameters from a string
    parser = ModuleArgsParser()
    action, args = parser._normalize_parameters('copy', 'copy', {'src': 'a', 'dest': 'b'})
    assert action == 'copy'