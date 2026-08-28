
import pytest
from tornado import locks
import asyncio

@pytest.mark.asyncio
async def test_valid_input_async_with():
    lock = locks.Lock()
    assert not lock._block.locked(), "Initial state should be unlocked"
    
    async with lock:
        assert lock._block.locked(), "After acquiring the lock, it should be locked"
        
    assert not lock._block.locked(), "After releasing the lock, it should be unlocked again"

@pytest.mark.asyncio
async def test_error_case_release_unlocked():
    lock = locks.Lock()
    with pytest.raises(RuntimeError):
        lock._block.release()
