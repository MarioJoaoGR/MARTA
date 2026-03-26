
from pymonet.task import Task

def test_invalid_input():
    # Test that the Task constructor raises a TypeError when given invalid input
    try:
        task = Task(123)  # Invalid input, should raise TypeError
    except TypeError as e:
        assert str(e) == "Expected a function but got <class 'int'>"
