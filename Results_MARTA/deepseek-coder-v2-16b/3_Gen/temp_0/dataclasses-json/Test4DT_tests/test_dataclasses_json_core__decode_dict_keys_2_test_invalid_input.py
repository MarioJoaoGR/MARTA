
import pytest
from dataclasses_json.core import _decode_dict_keys, _get_type_origin
from typing import Any, TypeVar, Tuple, Dict

def test_invalid_input():
    my_invalid_dict = {'string': 'value', (2, 3): 'another value'}
    with pytest.raises(TypeError):
        result_invalid_keytype = _decode_dict_keys([int], my_invalid_dict, infer_missing=True)
