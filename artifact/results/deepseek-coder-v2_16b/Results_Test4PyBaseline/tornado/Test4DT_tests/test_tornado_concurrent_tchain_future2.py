
import pytest
from tornado.concurrent import Future
from concurrent.futures import Future as CFuture
from tornado.ioloop import IOLoop
from tornado.gen import _NullFuture

def chain_future(a, b):
    def set_result():
        a.add_done_callback(lambda f: b.set_result(f.result()))
    if a.done():
        if a.exception() is not None:
            b.set_exception(a.exception())
        else:
            b.set_result(a.result())
    else:
        a.add_done_callback(lambda f: set_result())

# Test cases for chain_future function
def test_chain_future_tornado():
    a = Future()
    b = Future()
    
    chain_future(a, b)
    
    assert not b.done(), "b should not be done yet"
    
    a.set_result("success")