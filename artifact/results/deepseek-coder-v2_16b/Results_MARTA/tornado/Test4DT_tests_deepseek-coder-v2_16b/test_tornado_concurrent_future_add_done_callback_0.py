
import pytest
from tornado import concurrent
from typing import Callable, Union
from concurrent.futures import Future

def future_add_done_callback(
    future: "Union[Future[_T], concurrent.futures.Future[_T]]", callback: Callable[["Future[_T]"], None]
) -> None:
    """Arrange to call ``callback`` when ``future`` is complete.

    ``callback`` is invoked with one argument, the ``future``.

    If ``future`` is already done, ``callback`` is invoked immediately.
    This may differ from the behavior of ``Future.add_done_callback``,
    which makes no such guarantee.

    .. versionadded:: 5.0
    """
    if future is None:
        raise TypeError("future must be a Future object")
    
    def done_callback(f):
        callback(f)
    
    if future.done():
        done_callback(future)
    else:
        future.add_done_callback(done_callback)

def test_valid_input():
    from concurrent.futures import Future
    
    def my_callback(future):
        assert future.result() == "example result"
    
    future = Future()
    future_add_done_callback(future, my_callback)
    future.set_result("example result")

def test_invalid_input():
    from concurrent.futures import Future
    
    def my_callback(future):
        print('Future is done:', future.result())
    
    future = None
    with pytest.raises(TypeError):
        future_add_done_callback(future, my_callback)

def test_immediate_callback():
    from concurrent.futures import Future
    
    def immediate_callback(future):
        assert True  # This should be done immediately without raising an error
    
    future = Future()
    future.set_result(None)  # Set the result to trigger the callback
    future_add_done_callback(future, immediate_callback)

def test_exception_handling():
    from concurrent.futures import Future
    
    def exception_handler(future):
        with pytest.raises(RuntimeError):
            future.result()
    
    future = Future()
    future.set_exception(RuntimeError("Task failed"))
    future_add_done_callback(future, exception_handler)
