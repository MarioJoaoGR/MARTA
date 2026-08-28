
import pytest
from thonny.jedi_utils import ThonnyCompletion

def test_valid_creation():
    completion = ThonnyCompletion(name='print', complete='print()', type='function', description='Prints to the console.', parent=None, full_name='builtins.print')
    assert completion.name == 'print'
    assert completion.complete == 'print()'
    assert completion.type == 'function'
    assert completion.description == 'Prints to the console.'
    assert completion.parent is None
    assert completion.full_name == 'builtins.print'

def test_getitem_method():
    completion = ThonnyCompletion(name='print', complete='print()', type='function', description='Prints to the console.', parent=None, full_name='builtins.print')
    assert completion['name'] == 'print'
    assert completion['complete'] == 'print()'
    assert completion['type'] == 'function'
    assert completion['description'] == 'Prints to the console.'
    assert completion['parent'] is None
    assert completion['full_name'] == 'builtins.print'

def test_invalid_input():
    with pytest.raises(TypeError):
        ThonnyCompletion()
