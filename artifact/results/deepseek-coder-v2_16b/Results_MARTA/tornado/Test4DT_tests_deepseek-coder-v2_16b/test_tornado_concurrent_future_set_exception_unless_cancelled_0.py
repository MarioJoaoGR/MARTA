
import pytest
from concurrent.futures import Future
from tornado.concurrent import future_set_exception_unless_cancelled

def test_future_set_exception_on_non_cancelled():
    # Create a Future object
    my_future = Future()
    
    # Define an exception
    exc = Exception("Something went wrong")
    
    # Call the function to set an exception if the future is not cancelled
    future_set_exception_unless_cancelled(my_future, exc)
    
    # Assert that the exception was set correctly
    assert my_future.exception() == exc
