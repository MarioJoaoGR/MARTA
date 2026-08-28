# Module: ansible.module_utils.common._utils
import pytest
from ansible.module_utils.common._utils import get_all_subclasses

# Define some base classes and subclasses for testing
class BaseClass: pass
class Subclass1(BaseClass): pass
class Subclass2(Subclass1): pass
class Subclass3(BaseClass): pass

def test_get_all_subclasses():
    # Call the function with a specific class instance
    all_subclasses = get_all_subclasses(BaseClass)
    
    # Check that the result includes all subclasses of BaseClass
    assert set([cls.__name__ for cls in all_subclasses]) == {'Subclass1', 'Subclass2', 'Subclass3'}

# Additional test cases to ensure robustness and edge cases
def test_get_all_subclasses_empty():
    # Test with a class that has no subclasses
    class NoSubclasses: pass
    assert get_all_subclasses(NoSubclasses) == set()

def test_get_all_subclasses_single_level():
    # Test with a class having only direct subclasses
    class SingleLevelBase: pass
    class DirectSubclass1(SingleLevelBase): pass
    class DirectSubclass2(SingleLevelBase): pass
    assert set([cls.__name__ for cls in get_all_subclasses(SingleLevelBase)]) == {'DirectSubclass1', 'DirectSubclass2'}

def test_get_all_subclasses_multiple_inheritance():
    # Test with a class having multiple inheritance
    class MultiInheritanceBase: pass
    class MIChild1(MultiInheritanceBase): pass
    class MIChild2(MultiInheritanceBase): pass
    class MIGrandchild(MIChild1, MIChild2): pass
    assert set([cls.__name__ for cls in get_all_subclasses(MultiInheritanceBase)]) == {'MIChild1', 'MIChild2', 'MIGrandchild'}

if __name__ == "__main__":
    pytest.main()
