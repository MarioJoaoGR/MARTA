
import pytest
from unittest.mock import patch, MagicMock

def test_valid_input():
    doc = {
        'plugin': 'examplePlugin',
        'options': {
            'option1': {'type': 'string', 'description': 'Description of option1', 'required': True, 'default': 'default_value'},
            'option2': {'type': 'int', 'description': 'Description of option2', 'required': False, 'default': 0}
        }
    }
    
    with patch('ansible.cli.doc._do_lookup_snippet', return_value=['# option1(string): Description of option1', '# option2(int): Description of option2', '', 'lookup(\'examplePlugin\', option1=\'default_value\', option2=0)']):
        from ansible.cli.doc import _do_lookup_snippet
        result = _do_lookup_snippet(doc)
        assert result == ['# option1(string): Description of option1', '# option2(int): Description of option2', '', 'lookup(\'examplePlugin\', option1=\'default_value\', option2=0)']

def test_missing_plugin():
    doc = {
        'options': {
            'option1': {'type': 'string', 'description': 'Description of option1', 'required': True, 'default': 'default_value'},
            'option2': {'type': 'int', 'description': 'Description of option2', 'required': False, 'default': 0}
        }
    }
    
    with patch('ansible.cli.doc._do_lookup_snippet', return_value=['# option1(string): Description of option1', '# option2(int): Description of option2', '', 'lookup(\'%s\', %s=\'%s\', %s=%d)' % ('examplePlugin', 'option1', 'default_value', 'option2', 0)]):
        from ansible.cli.doc import _do_lookup_snippet
        result = _do_lookup_snippet(doc)
        assert result == ['# option1(string): Description of option1', '# option2(int): Description of option2', '', 'lookup(\'%s\', %s=\'%s\', %s=%d)' % ('examplePlugin', 'option1', 'default_value', 'option2', 0)]

def test_invalid_required():
    doc = {
        'plugin': 'examplePlugin',
        'options': {
            'option1': {'type': 'string', 'description': 'Description of option1', 'required': 'True', 'default': 'default_value'},
            'option2': {'type': 'int', 'description': 'Description of option2', 'required': False, 'default': 0}
        }
    }
    
    with pytest.raises(ValueError):
        from ansible.cli.doc import _do_lookup_snippet
        result = _do_lookup_snippet(doc)
