
import pytest
from concurrent.futures import Future
from tornado.concurrent import future_set_exc_info, future_set_exception_unless_cancelled

def test_future_set_exc_info():
    # Create a Future object
    my_future = Future()
    
    # Define the exception information
    exc_tuple = (Exception, Exception("Something went wrong"), None)
    
    # Call the function to set an exception if the future is not cancelled
    future_set_exc_info(my_future, exc_tuple)
    
    # Check that the future has the correct exception set
    assert my_future.done()
    with pytest.raises(Exception) as e:
        my_future.result()  # This should raise an Exception if the exception is properly set
    assert str(e.value) == "Something went wrong"

if __name__ == "__main__":
    pytest.main()
