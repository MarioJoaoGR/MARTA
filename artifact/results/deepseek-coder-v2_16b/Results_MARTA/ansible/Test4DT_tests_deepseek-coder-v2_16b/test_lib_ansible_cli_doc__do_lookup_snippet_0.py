
import pytest
from ansible.cli.doc import _do_lookup_snippet

def test_valid_input():
    doc = {
        'plugin': 'examplePlugin',
        'options': {
            'option1': {
                'type': 'string',
                'description': 'Description of option1',
                'required': True,
                'default': 'default_value'
            },
            'option2': {
                'type': 'int',
                'description': 'Description of option2',
                'required': False,
                'default': 0
            }
        }
    }
    expected = [
        '# option1(string): Description of option1',
        '# option2(int): Description of option2',
        '',
        'lookup(\'examplePlugin\', option1=\'default_value\', option2=0)'
    ]
    assert _do_lookup_snippet(doc) == expected

def test_edge_case():
    doc = None
    with pytest.raises(TypeError):
        _do_lookup_snippet(doc)

def test_invalid_input():
    doc = {
        'plugin': 'examplePlugin',
        'options': {
            'option1': {
                'type': 'string',
                'description': 'Description of option1',
                'required': True,
                'default': None
            }
        }
    }
    with pytest.raises(ValueError):
        _do_lookup_snippet(doc)
