
import pytest
from concurrent.futures import Future
import types
from typing import Optional, Tuple, Union
from tornado.concurrent import future_set_exc_info

# Test cases for the future_set_exc_info function
def test_future_set_exc_info_basic():
    f = Future()
    exc_info = (Exception, Exception("Task failed"), None)
    future_set_exc_info(f, exc_info)
    assert f.exception() == exc_info[1]

def test_future_set_exc_info_cancelled():
    f = Future()
    f.cancel()
    exc_info = (Exception, Exception("Task failed"), None)
    future_set_exc_info(f, exc_info)