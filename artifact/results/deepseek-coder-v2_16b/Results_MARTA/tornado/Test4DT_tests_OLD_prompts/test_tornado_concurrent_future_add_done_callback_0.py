
import pytest
from unittest.mock import patch, MagicMock
from concurrent.futures import Future
from tornado.concurrent import Future as TornadoFuture

def future_add_done_callback(future, callback):
    if not isinstance(future, (TornadoFuture,)):
        raise TypeError("The first argument must be an instance of tornado.concurrent.Future")
    if not callable(callback):
        raise TypeError("The second argument must be a callable function")
    future.add_done_callback(callback)


def test_none_input():
    with pytest.raises(TypeError):
        future_add_done_callback(None, lambda x: print("This should not be called"))

def test_invalid_callback():
    future = TornadoFuture()
    with pytest.raises(TypeError):
        future_add_done_callback(future, 123)