
# Module: pymonet.either
# test_either.py
from pymonet.either import Either, Left, Right
import pytest

# Test case for creating a Left instance with an error message
def test_left_instance():
    left_value = Either(Left("error message"))
    assert isinstance(left_value, Either)
    assert left_value.case(lambda x: f"Error: {x}", lambda x: x * 2) == "Error: error message"

# Test case for creating a Right instance with the value 42
def test_right_instance():
    right_value = Either(Right(42))
    assert isinstance(right_value, Either)
    assert right_value.case(lambda x: f"Error: {x}", lambda x: x * 2) == 84

# Test case for handling either case using the `case` method with a Left instance
def test_left_case():
    left = Either(Left("error message"))
    assert left.case(lambda x: f"Error: {x}", lambda x: x * 2) == "Error: error message"

# Test case for handling either case using the `case` method with a Right instance
def test_right_case():
    right = Either(Right(42))
    assert right.case(lambda x: f"Error: {x}", lambda x: x * 2) == 84

# Test case for applying a function within an Either structure using `ap` with Left instance
def test_left_ap():
    left_value = Left(42)
    right_value = Right("hello")
    
    def double_value(x):
        return x * 2
    
    result1 = left_value.ap(right_value)
    assert isinstance(result1, Left)
    assert result1.is_left()

# Test case for applying a function within an Either structure using `ap` with Right instance
def test_right_ap():
    right_value = Right("hello")
    left_value = Left(42)
    
    def double_value(x):
        return x * 2
    
    result2 = right_value.ap(left_value)
    assert isinstance(result2, Right)
    assert result2.is_right()

# Test case for transforming an Either instance into a Box monad using `to_box`
def test_to_box():
    either = Either(123)
    box = either.to_box()
    assert isinstance(box, type(either))
    assert box.value == 123

# Test case for transforming an Either instance into a Box monad using `to_box` with string value
def test_to_box_string():
    either = Either("Hello, World!")
    box = either.to_box()
    assert isinstance(box, type(either))
    assert box.value == "Hello, World!"

# Test case for transforming an Either instance into a Try monad using `to_try` with Left instance
def test_to_try_left():
    left = Either(Left("error message"))
    try_monad = left.to_try()
    assert isinstance(try_monad, type(either))
    assert not try_monad.is_success()

# Test case for transforming an Either instance into a Try monad using `to_try` with Right instance
def test_to_try_right():
    right = Either(Right(42))
    try_monad = right.to_try()
    assert isinstance(try_monad, type(either))
    assert try_monad.is_success()

# Test case for transforming an Either instance into a Lazy monad using `to_lazy`
def test_to_lazy():
    either = Either(5)
    lazy_either = either.to_lazy()
    assert lazy_either.fold() == 5

if __name__ == "__main__":
    pytest.main()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_either_Either_case_0
pyMonet/Test4DT_tests/test_pymonet_either_Either_case_0.py:71:38: E0602: Undefined variable 'either' (undefined-variable)
pyMonet/Test4DT_tests/test_pymonet_either_Either_case_0.py:78:38: E0602: Undefined variable 'either' (undefined-variable)
pyMonet/Test4DT_tests/test_pymonet_either_Either_case_0.py:85:11: E1101: Instance of 'Lazy' has no 'fold' member (no-member)


"""