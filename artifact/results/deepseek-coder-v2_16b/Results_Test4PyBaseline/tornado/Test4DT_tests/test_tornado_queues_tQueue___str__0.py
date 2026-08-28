# Module: tornado.queues
import pytest
from tornado.queues import Queue
from tornado.ioloop import IOLoop
from tornado import gen
import collections
from threading import Event

# Test initialization with default maxsize
def test_queue_init_default():
    q = Queue()
    assert q._maxsize == 0

# Test initialization with specified maxsize
def test_queue_init_specified():
    q = Queue(maxsize=2)
    assert q._maxsize == 2

# Test putting items into the queue
@gen.coroutine
def test_put():
    q = Queue(maxsize=2)
    yield q.put(1)
    yield q.put(2)
    assert len(q._queue) == 2
    item, future = q._putters.pop()
    assert item == 1
    assert not future.done()

# Test getting items from the queue
@gen.coroutine
def test_get():
    q = Queue(maxsize=2)
    yield q.put(1)
    item = yield q.get()
    assert item == 1
    assert len(q._queue) == 0

# Test task_done method
@gen.coroutine
def test_task_done():
    q = Queue(maxsize=2)
    yield q.put(1)
    yield q.get()
    q.task_done()
    assert q._unfinished_tasks == 0

# Test join method to wait for all tasks to be processed
@gen.coroutine
def test_join():
    q = Queue(maxsize=2)
    IOLoop.current().spawn_callback(lambda: IOLoop.current().add_callback(test_put))
    yield q.put(1)
    yield q.put(2)
    IOLoop.current().spawn_callback(lambda: IOLoop.current().add_callback(test_get))
    yield q.get()
    yield q.join()
    assert q._unfinished_tasks == 0

# Test raising TypeError when maxsize is None
def test_init_maxsize_none():
    with pytest.raises(TypeError):
        Queue(maxsize=None)

# Test raising ValueError when maxsize is negative
def test_init_maxsize_negative():
    with pytest.raises(ValueError):
        Queue(maxsize=-1)
