
import pytest
from isort._vendored.tomli._parser import NestedDict

def test_valid_input():
    nd = NestedDict()
    nd.append_nest_to_list(['a', 'b'])
    assert isinstance(nd.dict['a']['b'], list)
    assert len(nd.dict['a']['b']) == 1
    assert isinstance(nd.dict['a']['b'][0], dict)
