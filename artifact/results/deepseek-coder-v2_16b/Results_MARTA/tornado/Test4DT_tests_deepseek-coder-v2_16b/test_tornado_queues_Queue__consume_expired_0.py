
import pytest
from tornado.queues import Queue
from tornado.ioloop import IOLoop
import asyncio

# Test for edge case where maxsize is None
def test_maxsize_none():
    with pytest.raises(TypeError):
        q = Queue(maxsize=None)
