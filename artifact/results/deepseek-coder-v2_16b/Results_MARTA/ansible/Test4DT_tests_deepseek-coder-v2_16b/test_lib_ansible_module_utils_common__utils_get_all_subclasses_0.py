
import pytest
from ansible.module_utils.common._utils import get_all_subclasses

def test_get_all_subclasses_basic():
    class BaseClass: pass
    class SubClass1(BaseClass): pass
    class SubClass2(SubClass1): pass
    
    subclasses = get_all_subclasses(BaseClass)
    assert set([SubClass1, SubClass2]) == subclasses

def test_get_all_subclasses_no_subclasses():
    class NoSubclasses: pass
    
    subclasses = get_all_subclasses(NoSubclasses)
    assert set() == subclasses
