
import pytest
from typing import Dict, Any, List

class NestedDict:
    def __init__(self) -> None:
        self.dict: Dict[str, Any] = {}

    def get_or_create_nest(self, key: List[str], access_lists=True):
        nest = self.dict
        for k in key:
            if isinstance(nest, list) and access_lists:
                if not isinstance(k, int):
                    raise KeyError("Invalid key type")
                if k >= len(nest):
                    nest = {}
                else:
                    nest = nest[k]
            elif isinstance(nest, dict):
                if k not in nest:
                    nest[k] = {}
                nest = nest[k]
            else:
                raise KeyError("Invalid key sequence")
        return nest

    def append_nest_to_list(self, key: List[str]) -> None:
        cont = self.get_or_create_nest(key[:-1], access_lists=False)
        last_key = key[-1]
        if isinstance(cont, list):
            cont.append({})
        else:
            raise KeyError("An object other than list found behind this key")

def test_error_case():
    nd = NestedDict()
    with pytest.raises(KeyError):
        nd.append_nest_to_list(['a', 'b'])
