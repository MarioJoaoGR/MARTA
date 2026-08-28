
import pytest
from ansible.module_utils.common._utils import get_all_subclasses



def test_get_all_subclasses_basic_usage():
    class A: pass
    class B(A): pass
    class C(B): pass
    
    subclasses = get_all_subclasses(A)
    assert set([cls.__name__ for cls in subclasses]) == {'B', 'C'}

def test_get_all_subclasses_no_subclasses():
    class NoSubclasses: pass
    
    subclasses = get_all_subclasses(NoSubclasses)
    assert not subclasses