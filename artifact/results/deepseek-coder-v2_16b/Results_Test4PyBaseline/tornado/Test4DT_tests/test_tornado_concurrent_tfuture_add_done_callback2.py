# Module: tornado.concurrent
import pytest
from concurrent.futures import Future, ThreadPoolExecutor
from typing import Callable, Union

# Import the function to be tested
def future_add_done_callback(
    future: "Union[futures.Future[_T], Future[_T]]", callback: Callable[..., None]
) -> None:
    """Arrange to call ``callback`` when ``future`` is complete.

    ``callback`` is invoked with one argument, the ``future``. If ``future`` is already done, 
    ``callback`` is invoked immediately. This may differ from the behavior of ``Future.add_done_callback``, 
    which makes no such guarantee.

    .. versionadded:: 5.0

    Parameters:
        future (Union[futures.Future[_T], Future[_T]]): The future object to monitor for completion.
        callback (Callable[..., None]): The function to call when the future is done. It will be called with the future as its only argument.

    Returns:
        None
    """
    pass

# Test cases for future_add_done_callback
def test_future_add_done_callback_immediate_call():
    # Arrange
    from concurrent.futures import Future, ThreadPoolExecutor
    
    def my_callback(future):
        assert future.done() == True
        assert future.result() == "example result"
    
    future = Future()
    future_add_done_callback(future, my_callback)
    
    # Act
    future.set_result("example result")
    
    # Assert
    assert future.done() == True
    assert future.result() == "example result"

def test_future_add_done_callback_no_call():
    # Arrange
    from concurrent.futures import Future, ThreadPoolExecutor
    
    def my_callback(future):
        pytest.fail("Callback should not be called before the future is done.")
    
    future = Future()
    future_add_done_callback(future, my_callback)
    
    # Act & Assert (no action needed as we expect no call to callback)

def test_future_add_done_callback_with_executor():
    # Arrange
    from concurrent.futures import Future, ThreadPoolExecutor
    
    def my_callback(future):
        assert future.done() == True
        assert future.result() == 5
    
    executor = ThreadPoolExecutor()
    future = executor.submit(lambda: 2 + 3)
    future_add_done_callback(future, my_callback)
    
    # Act (wait for the future to complete in a real-world scenario this would be handled by the event loop)
    import time
    while not future.done():
        time.sleep(0.1)
    
    # Assert
    assert future.done() == True
    assert future.result() == 5

# Add more test cases as needed to cover different scenarios and edge cases
