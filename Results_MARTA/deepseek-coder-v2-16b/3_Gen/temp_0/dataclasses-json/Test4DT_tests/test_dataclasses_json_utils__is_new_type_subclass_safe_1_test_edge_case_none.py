
import pytest
from dataclasses_json.utils import _is_new_type_subclass_safe

def test_edge_case_none():
    class A: pass
    class B(A): pass
    assert _is_new_type_subclass_safe(B, A) == True

    class C: pass
    assert _is_new_type_subclass_safe(C, int) == False

    class D(str): pass
    assert _is_new_type_subclass_safe(D, str) == True
