
import pytest
from dataclasses_json import core as dcj_core
from typing import TypeVar, Any, Tuple, Dict, Union

def test_invalid_input():
    my_dict = {'a': 'value', (2, 3): 'another value'}
    key_type = [int]
    infer_missing = True
    
    with pytest.raises(TypeError):
        dcj_core._decode_dict_keys(key_type, my_dict, infer_missing)
