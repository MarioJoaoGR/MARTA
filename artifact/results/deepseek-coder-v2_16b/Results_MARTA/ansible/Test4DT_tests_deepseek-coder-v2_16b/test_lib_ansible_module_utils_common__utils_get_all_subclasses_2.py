
import pytest
from ansible.module_utils.common._utils import get_all_subclasses

def test_get_all_subclasses_valid_class():
    class BaseClass: pass
    class SubClass1(BaseClass): pass
    class SubClass2(SubClass1): pass
    
    result = get_all_subclasses(BaseClass)
    assert set([SubClass1, SubClass2]) == result

def test_get_all_subclasses_no_subclasses():
    class NoSubclasses: pass
    
    result = get_all_subclasses(NoSubclasses)
    assert set() == result
