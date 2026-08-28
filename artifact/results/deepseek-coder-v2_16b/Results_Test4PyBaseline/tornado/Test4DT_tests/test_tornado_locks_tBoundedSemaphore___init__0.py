# Module: tornado.locks
import pytest
from tornado.locks import BoundedSemaphore

# Test creating a BoundedSemaphore with an initial value of 2
def test_bounded_semaphore_initial_value():
    sem = BoundedSemaphore(value=2)
    assert sem._initial_value == 2

# Test releasing more times than the initial value allows, should raise ValueError
def test_release_too_many_times():
    with pytest.raises(ValueError):
        sem = BoundedSemaphore(value=2)
        sem.release()  # First release
        sem.release()  # Second release
        sem.release()  # This would raise ValueError

# Test creating a BoundedSemaphore with the default initial value of 1
def test_bounded_semaphore_default_value():
    sem = BoundedSemaphore()
    assert sem._initial_value == 1

# Test using BoundedSemaphore in an asynchronous context
@pytest.mark.gen_test
async def test_bounded_semaphore_in_async_context():
    from tornado import gen
    from tornado.ioloop import IOLoop
    from tornado.locks import BoundedSemaphore

    sem = BoundedSemaphore(value=2)

    async def worker():
        await sem.acquire()  # Acquire the semaphore
        try:
            assert sem._value == 1  # Check that the semaphore value is as expected after acquire
            print("Worker is working")
            await gen.sleep(1)  # Simulate work with a sleep-like operation
        finally:
            print("Worker is done")
            sem.release()  # Release the semaphore

    async def runner():
        await gen.multi([worker() for _ in range(3)])

    IOLoop.current().run_sync(runner)  # Run the async tasks
