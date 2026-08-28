
import pytest
from tornado import locks
import asyncio

# Test for acquiring and releasing a lock using async with
@pytest.mark.asyncio
async def test_acquire_release():
    lock = locks.Lock()
    with pytest.raises(RuntimeError):
        # Attempt to release an unlocked lock, which should raise RuntimeError
        lock._block.release()
