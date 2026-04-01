
import pytest
from dataclasses import dataclass
from typing import List, Set, Dict, Collection
from dataclasses_json.utils import _is_collection

def test_error_case():
    @dataclass
    class MyList:
        def __iter__(self):
            yield 1
    
    my_custom_list = MyList()
    assert not _is_collection(my_custom_list.__class__)
