# Module: dataclasses_json.utils
import pytest
from collections import Counter

# Import the function from its module
from dataclasses_json.utils import _is_counter

def test_custom_subclass_of_counter():
    class MyCounter(Counter): pass
    assert _is_counter(MyCounter) is True

def test_not_a_subclass_of_counter():
    class NotACounter(list): pass
    assert _is_counter(NotACounter) is False

def test_builtin_counter_class():
    from collections import Counter
    assert _is_counter(Counter) is True
