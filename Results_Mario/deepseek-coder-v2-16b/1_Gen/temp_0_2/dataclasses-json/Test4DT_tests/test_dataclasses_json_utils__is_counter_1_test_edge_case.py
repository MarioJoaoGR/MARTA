
import pytest
from dataclasses_json.utils import _is_counter, _get_type_origin
from collections import Counter

def test_edge_case():
    class MyCounter(Counter[str]): pass
    
    # Test if MyCounter is a subclass of Counter
    assert _is_counter(MyCounter) == True
