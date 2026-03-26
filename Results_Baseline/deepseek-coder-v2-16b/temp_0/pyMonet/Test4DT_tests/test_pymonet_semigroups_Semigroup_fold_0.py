# Module: pymonet.semigroups
import pytest
from pymonet.semigroups import Semigroup  # Assuming the module name is pymonet.semigroups

# Test instantiation with different types of values
def test_instantiation():
    s1 = Semigroup(5)
    assert s1.value == 5
    
    s2 = Semigroup("hello")
    assert s2.value == "hello"
    
    s3 = Semigroup([1, 2, 3])
    assert s3.value == [1, 2, 3]
    
    s4 = Semigroup({'a': 1, 'b': 2})
    assert s4.value == {'a': 1, 'b': 2}

# Test fold method with different types of values and functions
def test_fold():
    semigroup = Semigroup(10)
    
    def add_one(x):
        return x + 1
    
    result = semigroup.fold(add_one)
    assert result == 11
    
    def multiply_by_two(x):
        return x * 2
    
    result = Semigroup(3).fold(multiply_by_two)
    assert result == 6
    
    def sum_list(lst):
        return sum(lst)
    
    result = Semigroup([1, 2, 3]).fold(sum_list)
    assert result == 6
    
    def dict_sum(d):
        return sum(d.values())
    
    result = Semigroup({'a': 1, 'b': 2}).fold(dict_sum)
    assert result == 3

# Test fold method with a function that returns the same type as the initial value
def test_fold_same_type():
    semigroup = Semigroup([4, 5, 6])
    
    def average(lst):
        return sum(lst) / len(lst)
    
    result = semigroup.fold(average)
    assert result == 5.0  # The average of [4, 5, 6] is 5.0

# Test fold method with a function that modifies the type (e.g., converting to string)
def test_fold_type_change():
    semigroup = Semigroup(123)
    
    def str_value(x):
        return str(x)
    
    result = semigroup.fold(str_value)
    assert result == "123"

# Test fold method with a function that returns None (to ensure it handles non-applicable cases)
def test_fold_none():
    semigroup = Semigroup(456)
    
    def do_nothing(_):
        return None
    
    result = semigroup.fold(do_nothing)
    assert result is None

if __name__ == "__main__":
    pytest.main()
