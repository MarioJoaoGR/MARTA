# Module: pytutils.queues
import pytest
from queue import Queue
from threading import Thread
from pytutils.queues import multiplex

# Test the default behavior of multiplex with count=2
def test_multiplex_default():
    in_q = Queue()
    out_queues = multiplex(in_q)
    assert len(out_queues) == 2, "Expected two queues but got {}".format(len(out_queues))
    for q in out_queues:
        assert isinstance(q, Queue), "Each queue should be a Queue instance"

# Test the behavior of multiplex with count=3
def test_multiplex_count():
    in_q = Queue()
    out_queues = multiplex(in_q, count=3)
    assert len(out_queues) == 3, "Expected three queues but got {}".format(len(out_queues))
    for q in out_queues:
        assert isinstance(q, Queue), "Each queue should be a Queue instance"

# Test the behavior of multiplex with custom queue factory
def test_multiplex_custom_queue_factory():
    def custom_queue_factory():
        return Queue()
    
    in_q = Queue()
    out_queues = multiplex(in_q, queue_factory=custom_queue_factory)
    assert len(out_queues) == 2, "Expected two queues but got {}".format(len(out_queues))
    for q in out_queues:
        assert isinstance(q, Queue), "Each queue should be a Queue instance"

# Test the behavior of multiplex with an already populated queue
def test_multiplex_with_prepopulated_queue():
    in_q = Queue()
    in_q.put(1)
    out_queues = multiplex(in_q, count=2)
    for q in out_queues:
        assert not q.empty(), "Output queues should have items from the input queue"
        item = q.get()
        assert item == 1, "Items in output queues should match those of the input queue"
        q.put(item)  # Put back to simulate further processing

# Test the behavior of multiplex with an empty queue
def test_multiplex_with_empty_queue():
    in_q = Queue()
    out_queues = multiplex(in_q, count=2)
    for q in out_queues:
        assert q.empty(), "Output queues should be empty since the input queue is empty"
