
import pytest
from tornado.queues import Queue
from tornado.concurrent import Future
from collections import deque
from threading import Event

# Test for valid input in put_nowait method

# Test for invalid input in put_nowait method

# Test for valid input in get_nowait method
def test_get_nowait_valid():
    q = Queue(maxsize=1)
    q.put_nowait(1)
    item = q.get_nowait()
    assert item == 1
    assert q.empty()

# Test for invalid input in get_nowait method