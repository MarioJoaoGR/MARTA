
import pytest
from tornado import locks
import asyncio

@pytest.mark.asyncio
async def test_lock_acquire_release():
    lock = locks.Lock()
    assert not lock._block.locked(), "Initial state should be unlocked"
    
    # Acquire the lock
    await lock.acquire()
    assert lock._block.locked(), "After acquiring, the lock should be locked"
    
    # Release the lock
    lock.release()
    assert not lock._block.locked(), "After releasing, the lock should be unlocked"

@pytest.mark.asyncio
async def test_lock_context_manager():
    lock = locks.Lock()
    async with lock:
        # Inside the context manager, the lock should be locked
        assert lock._block.locked(), "Inside the context manager, the lock should be locked"
    
    # After exiting the context manager, the lock should be unlocked
    assert not lock._block.locked(), "After exiting the context manager, the lock should be unlocked"

@pytest.mark.asyncio
async def test_lock_repr():
    lock = locks.Lock()
    expected_repr = "<Lock _block=<BoundedSemaphore 1>>"
    assert repr(lock) == expected_repr, f"Expected {expected_repr}, but got {repr(lock)}"
