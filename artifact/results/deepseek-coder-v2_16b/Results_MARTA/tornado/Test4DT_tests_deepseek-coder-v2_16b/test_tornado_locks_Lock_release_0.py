
import pytest
from tornado import locks
import asyncio

@pytest.mark.asyncio
async def test_valid_input():
    lock = locks.Lock()
    assert not lock._block.locked()  # Check if the lock is initially unlocked
    
    await lock.acquire()
    assert lock._block.locked()  # Check if the lock is locked after acquire
    
    lock.release()
    assert not lock._block.locked()  # Check if the lock is released after release

@pytest.mark.asyncio
async def test_edge_case():
    lock = locks.Lock()
    with pytest.raises(RuntimeError):
        lock.release()  # Attempt to release an unlocked lock should raise RuntimeError

@pytest.mark.asyncio
async def test_invalid_input():
    lock = locks.Lock()
    with pytest.raises(RuntimeError):
        lock.release()  # Attempt to release an unlocked lock should raise RuntimeError
