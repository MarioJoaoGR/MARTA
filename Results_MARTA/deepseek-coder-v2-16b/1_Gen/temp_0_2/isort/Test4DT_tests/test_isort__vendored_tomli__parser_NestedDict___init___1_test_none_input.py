
from isort._vendored.tomli._parser import NestedDict
import toml

def test_none_input():
    nd = NestedDict()
    assert nd.dict == {}

    # Example usage with a nested structure
    toml_content = '''
    [section1]
    key1 = "value1"
    [section2]
    key2 = "value2"
    '''
    nd.dict = toml.loads(toml_content)
    assert nd.dict == {'section1': {'key1': 'value1'}, 'section2': {'key2': 'value2'}}
