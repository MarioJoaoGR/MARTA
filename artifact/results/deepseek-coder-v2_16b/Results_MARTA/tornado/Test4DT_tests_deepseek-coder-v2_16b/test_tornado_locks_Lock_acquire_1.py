
import pytest
from tornado import locks
import asyncio

# Test scenarios
@pytest.mark.asyncio
async def test_valid_case():
    lock = locks.Lock()
    assert not lock._block.locked(), "Lock should start unlocked"
    await lock.acquire()
    assert lock._block.locked(), "Lock should be locked after acquire"
    lock.release()
    assert not lock._block.locked(), "Lock should be released after release"

@pytest.mark.asyncio
async def test_edge_case():
    lock = locks.Lock()
    with pytest.raises(RuntimeError):
        lock.release()

@pytest.mark.asyncio
async def test_error_handling():
    lock = locks.Lock()
    with pytest.raises(RuntimeError):
        lock.release()
