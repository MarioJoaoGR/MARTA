
import pytest
from dataclasses_json.core import _decode_dict_keys


def test_decode_dict_keys_none():
    xs = [{'name': 'Alice', 'age': '30'}, {'name': 'Bob', 'age': '25'}]
    decoded_dicts = list(_decode_dict_keys(None, xs, infer_missing=False))
    assert decoded_dicts == [{'name': 'Alice', 'age': '30'}, {'name': 'Bob', 'age': '25'}]


