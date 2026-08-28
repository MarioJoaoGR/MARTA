
import pytest
from tornado import locks
import asyncio
from unittest.mock import patch, MagicMock

@pytest.mark.asyncio
async def test_lock_repr():
    lock = locks.Lock()
    assert repr(lock) == "<Lock _block=1>"

@pytest.mark.asyncio
async def test_lock_acquire_release():
    lock = locks.Lock()
    async with lock:
        # Do something holding the lock.
        pass
    # Now the lock is released.

@pytest.mark.asyncio
async def test_lock_invalid_usage():
    lock = locks.Lock()
    with pytest.raises(RuntimeError):
        async with lock:
            raise RuntimeError("Expected error")
