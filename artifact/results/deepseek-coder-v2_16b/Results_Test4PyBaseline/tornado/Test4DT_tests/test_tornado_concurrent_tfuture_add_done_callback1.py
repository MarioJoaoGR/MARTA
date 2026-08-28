
import pytest
from concurrent.futures import Future, ThreadPoolExecutor
from typing import Callable, Union

# Import the function to be tested
def future_add_done_callback(
    future: "Union[Future[_T], futures.Future[_T]]", callback: Callable[["futures.Future[_T]"], None]
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
        assert future.done() is True
        print("Future is done:", future.result())
    
    future = Future()
    future_add_done_callback(future, my_callback)
    
    # Act
    future.set_result("example result")
    
    # Assert
    assert future.done() is True
    assert future.result() == "example result"

def test_future_add_done_callback_not_called_if_not_done():
    # Arrange
    from concurrent.futures import Future, ThreadPoolExecutor
    
    def my_callback(future):
        pytest.fail("Callback should not be called if the future is not done.")
    
    future = Future()
    future_add_done_callback(future, my_callback)
    
    # Act & Assert (nothing to act since no change in state)
    assert not future.done()

def test_future_add_done_callback_multiple_callbacks():
    # Arrange
    from concurrent.futures import Future, ThreadPoolExecutor
    
    def callback1(future):
        print("Callback 1:", future.result())
    
    def callback2(future):
        print("Callback 2:", future.result())
    
    future = Future()
    future_add_done_callback(future, callback1)
    future_add_done_callback(future, callback2)
    
    # Act
    future.set_result("example result")
    
    # Assert
    assert future.done() is True
    assert future.result() == "example result"

def test_future_add_done_callback_with_executor():
    # Arrange
    from concurrent.futures import Future, ThreadPoolExecutor
    
    def my_callback(future):
        print("Future is done:", future.result())
    
    executor = ThreadPoolExecutor()
    future = executor.submit(lambda: 42)
    future_add_done_callback(future, my_callback)
    
    # Act & Assert (nothing to act since no change in state)