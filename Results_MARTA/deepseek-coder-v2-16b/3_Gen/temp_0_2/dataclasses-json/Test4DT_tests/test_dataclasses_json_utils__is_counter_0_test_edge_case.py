
import pytest
from dataclasses_json.utils import _is_counter, _get_type_origin, Counter

def test_edge_case():
    class MyCounter(Counter): pass
    assert _is_counter(MyCounter) == True
    
    class NotACounter: pass
    assert _is_counter(NotACounter) == False
    
    from typing import List
    my_list = List[int]
    assert _is_counter(my_list) == False
