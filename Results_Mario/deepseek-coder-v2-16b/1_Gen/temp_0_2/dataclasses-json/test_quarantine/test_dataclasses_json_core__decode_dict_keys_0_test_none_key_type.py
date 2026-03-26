
from dataclasses_json import core as dcj_core
from typing import Any, TypeVar, Tuple, Dict, List, Callable

def _decode_dict_keys(key_type, xs, infer_missing):
    """
    Because JSON object keys must be strs, we need the extra step of decoding
    them back into the user's chosen python type
    """
    decode_function = key_type
    # handle NoneType keys... it's weird to type a Dict as NoneType keys
    # but it's valid...
    # Issue #341 and PR #346:
    #   This is a special case for Python 3.7 and Python 3.8.
    #   By some reason, "unbound" dicts are counted
    #   as having key type parameter to be TypeVar('KT')
    if key_type is None or key_type == Any or isinstance(key_type, TypeVar):
        decode_function = key_type = (lambda x: x)
    # handle a nested python dict that has tuples for keys. E.g. for
    # Dict[Tuple[int], int], key_type will be typing.Tuple[int], but
    # decode_function should be tuple, so map() doesn't break.
    #
    # Note: _get_type_origin() will return typing.Tuple for python
    # 3.6 and tuple for 3.7 and higher.
    elif dcj_core._get_type_origin(key_type) in {tuple, Tuple}:
        decode_function = tuple
        key_type = key_type

    return map(decode_function, _decode_items(key_type, xs, infer_missing))

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_core__decode_dict_keys_0_test_none_key_type
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_dict_keys_0_test_none_key_type.py:29:32: E0602: Undefined variable '_decode_items' (undefined-variable)


"""