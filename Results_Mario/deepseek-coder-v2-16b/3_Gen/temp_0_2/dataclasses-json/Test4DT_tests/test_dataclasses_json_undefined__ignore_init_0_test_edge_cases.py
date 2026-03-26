
import pytest
from dataclasses import dataclass
from dataclasses_json.undefined import _IgnoreUndefinedParameters

@dataclass
class MyClass:
    a: int
    b: int = None
    c: int = 0

def test_edge_cases():
    # Test with None values
    instance1 = MyClass(a=1, b=None)
    assert instance1.a == 1
    assert instance1.b is None
    assert instance1.c == 0

    # Test with empty values
    instance2 = MyClass(a=1, b=0, c=0)
    assert instance2.a == 1
    assert instance2.b == 0
    assert instance2.c == 0

    # Test with None and empty values
    instance3 = MyClass(a=1)
    assert instance3.a == 1
    assert instance3.b is None
    assert instance3.c == 0

    # Test with all None values
    instance4 = MyClass(a=None, b=None, c=None)
    assert instance4.a is None
    assert instance4.b is None
    assert instance4.c is None
