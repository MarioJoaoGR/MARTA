# Module: tornado.locks
import pytest
from tornado.locks import Semaphore
from tornado.ioloop import IOLoop
from tornado.concurrent import Future
import asyncio

# Test the initialization of Semaphore with a valid initial value
def test_semaphore_init_valid():
    sem = Semaphore(2)
    assert sem._value == 2

# Test the initialization of Semaphore with an invalid initial value (should raise ValueError)
def test_semaphore_init_invalid():
    with pytest.raises(ValueError):
        Semaphore(-1)

# Test acquiring a semaphore when it has available permits
async def test_acquire_available():
    sem = Semaphore(2)
    await sem.acquire()
    assert sem._value == 1

# Test acquiring a semaphore when it has no available permits (should block until available)
async def test_acquire_no_available():
    sem = Semaphore(0)
    with pytest.raises(asyncio.exceptions.TimeoutError):
        await asyncio.wait_for(sem.acquire(), timeout=1)

# Test releasing a semaphore when it has available permits
def test_release_available():
    sem = Semaphore(0)
    sem.release()
    assert sem._value == 1

# Test using async context manager to acquire and release the semaphore
async def test_async_context_manager():
    sem = Semaphore(2)
    async with sem:
        assert sem._value == 1

# Test compatibility with older versions of Python by using context managers
def test_compatibility_with_old_python():
    from tornado import gen
    sem = Semaphore(2)
    with pytest.raises(TypeError):
        with (yield sem.acquire()):
            pass
