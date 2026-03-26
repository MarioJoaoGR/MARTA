
import toml
from isort._vendored.tomli._parser import NestedDict
import pytest

def test_valid_input():
    nd = NestedDict()
    toml_content = '''
    [section1]
    key1 = "value1"
    [section2]
    key2 = "value2"
    '''
    nd.dict = toml.loads(toml_content)
    
    assert isinstance(nd.dict, dict)
    assert len(nd.dict) == 2
    assert nd.dict['section1'] == {'key1': 'value1'}
    assert nd.dict['section2'] == {'key2': 'value2'}
