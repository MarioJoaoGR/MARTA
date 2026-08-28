
import pytest
from ansible.parsing.mod_args import ModuleArgsParser
from ansible.errors import AnsibleAssertionError, AnsibleParserError
from collections import namedtuple

# Define a simple string type for testing purposes
string_types = (str,)

# Mock the necessary parts of the ansible module and utils
class MockModule:
    def __init__(self, **kwargs):
        self.kwargs = kwargs

    @property
    def args(self):
        return self.kwargs

class MockArgsParser:
    def _normalize_old_style_args(self, thing):
        action = None
        args = {}
        if isinstance(thing, dict):
            if 'module' in thing:
                module_name = thing['module']
                action = module_name.split()[0]
                for key, value in thing.items():
                    if key != 'module':
                        args[key] = value
        elif isinstance(thing, string_types):
            parts = thing.split()
            if len(parts) > 0:
                action = parts[0]
                for part in parts[1:]:
                    key, value = part.split('=', 1)
                    args[key] = value
        else:
            raise AnsibleParserError("unexpected parameter type in action: %s" % type(thing), obj=None)
        return (action, args)

# Test cases for ModuleArgsParser._normalize_old_style_args
def test_normalize_old_style_args_dict():
    parser = MockArgsParser()
    thing = {'module': 'copy', 'src': 'a', 'dest': 'b'}
    action, args = parser._normalize_old_style_args(thing)
    assert action == 'copy'
    assert args == {'src': 'a', 'dest': 'b'}

def test_normalize_old_style_args_string():
    parser = MockArgsParser()
    thing = 'copy src=a dest=b'
    action, args = parser._normalize_old_style_args(thing)
    assert action == 'copy'
    assert args == {'src': 'a', 'dest': 'b'}

def test_normalize_old_style_args_invalid():
    parser = MockArgsParser()
    thing = 123  # Invalid type
    with pytest.raises(AnsibleParserError):
        parser._normalize_old_style_args(thing)
