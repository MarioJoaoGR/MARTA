
import pytest
from docstring_parser.common import DocstringReturns

def test_valid_inputs():
    metadata = DocstringReturns(args=['arg1', 'arg2'], description='This function does something.', type_name='int', is_generator=False, return_name='result')
    
    assert isinstance(metadata.args, list)
    assert metadata.args == ['arg1', 'arg2']
    assert metadata.description == 'This function does something.'
    assert metadata.type_name == 'int'
    assert metadata.is_generator is False
    assert metadata.return_name == 'result'
