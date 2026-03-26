
from dataclasses_json.utils import _is_counter as _is_counter_func
from collections import Counter
import pytest

def test_valid_case():
    class MyCounter(Counter[str]): pass
    
    assert _is_counter_func(MyCounter) == True
