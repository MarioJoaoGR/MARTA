# Module: tornado.locks
# test_locks.py
import pytest
from tornado import locks
import asyncio

@pytest.fixture(scope="module")
def lock():
    return locks.Lock()

@pytest.mark.asyncio
async def test_lock_async_context(lock):
    async with lock:
        assert isinstance(lock, locks.Lock)
        print("Doing something holding the lock.")
        # Simulate work being done with the lock held

@pytest.mark.asyncio
async def test_lock_acquire_compatibility(lock):
    with pytest.raises(RuntimeError):  # Ensure that releasing an unlocked lock raises a RuntimeError
        lock._block.release()
    
    async def acquire_and_release():
        with (yield lock.acquire()):
            print("Doing something holding the lock.")
            # Simulate work being done with the lock held

    loop = asyncio.get_event_loop()
    future = loop.run_until_complete(acquire_and_release())
    
    with pytest.raises(RuntimeError):  # Ensure that releasing an unlocked lock raises a RuntimeError after the context is exited
        lock._block.release()

if __name__ == "__main__":
    pytest.main()
