# Module: tornado.queues
# test_queue.py
from tornado.queues import Queue
import pytest
from tornado import gen
from tornado.ioloop import IOLoop

@pytest.fixture(scope="module")
def queue():
    return Queue(maxsize=2)

@gen.coroutine
def producer(q):
    for item in range(5):
        yield q.put(item)  # Put an item into the queue
        print('Put', item)

@gen.coroutine
def consumer(q):
    while True:
        item = yield q.get()  # Get an item from the queue
        try:
            print('Doing work on', item)  # Simulate some work with a sleep
            yield gen.sleep(0.01)
        finally:
            q.task_done()  # Mark the task as done

@gen.coroutine
def main():
    q = Queue(maxsize=2)  # Create a queue with a maximum size of 2
    IOLoop.current().spawn_callback(consumer, q)  # Start the consumer without waiting
    yield producer(q)  # Wait for producer to put all tasks
    yield q.join()     # Wait for consumer to finish all tasks
    print('Done')

def test_queue():
    IOLoop.current().run_sync(main)  # Run the main coroutine in the event loop
    assert True
