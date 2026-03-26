
from typing import Any, Dict

import pytest


class NestedDict:
    def __init__(self) -> None:
        self.dict: Dict[str, Any] = {}

    def get_or_create_nest(self, key: list, *, access_lists=True) -> dict:
        cont = self.dict
        for k in key:
            if k not in cont:
                cont[k] = {}
            cont = cont[k]
            if access_lists and isinstance(cont, list):
                cont = cont[-1]
            if not isinstance(cont, dict):
                raise KeyError("There is no nest behind this key")
        return cont

    def append_nest_to_list(self, key: list) -> None:
        cont = self.get_or_create_nest(key[:-1])
        last_key = key[-1]
        if last_key in cont:
            lst = cont[last_key]
            if not isinstance(lst, list):
                raise KeyError("An object other than list found behind this key")
            lst.append({})
        else:
            cont[last_key] = [{}]

# Test cases for get_or_create_nest method
def test_get_or_create_nest():
    nd = NestedDict()
    # Retrieving a new nest
    assert nd.get_or_create_nest(['a', 'b', 'c']) == {}
    # Accessing an existing nest
    nd.dict['a'] = {'b': {}}