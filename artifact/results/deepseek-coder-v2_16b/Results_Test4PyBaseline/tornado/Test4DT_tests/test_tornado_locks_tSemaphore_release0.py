
# Module: tornado.locks
# test_semaphore.py
import pytest
from tornado.locks import Semaphore
from tornado.ioloop import IOLoop
from tornado.concurrent import Future
import asyncio

@pytest.fixture
def semaphore():
    return Semaphore(2)

@pytest.mark.asyncio
async def test_semaphore_allows_two_workers(semaphore):
    """Test that two workers can acquire the semaphore concurrently."""
    async def worker(worker_id):
        await semaphore.acquire()
        try:
            assert semaphore._value == 2 - worker_id, "Semaphore value is incorrect after acquisition"
            print("Worker %d is working" % worker_id)
            await asyncio.sleep(0)
        finally:
            semaphore.release()
            assert semaphore._value == 1 + worker_id, "Semaphore value is incorrect after release"
            print("Worker %d is done" % worker_id)
    
    # Run multiple workers concurrently
    await asyncio.gather(*[worker(i) for i in range(2)])

@pytest.mark.asyncio
async def test_semaphore_blocks_third_worker(semaphore):
    """Test that the third worker is blocked by the semaphore."""
    async def worker(worker_id, expected_value):
        await semaphore.acquire()
        try:
            assert semaphore._value == expected_value, "Semaphore value is incorrect after acquisition"
            print("Worker %d is working" % worker_id)
            await asyncio.sleep(0)
        finally:
            semaphore.release()
            assert semaphore._value == expected_value - 1, "Semaphore value is incorrect after release"
            print("Worker %d is done" % worker_id)
    
    # Run two workers concurrently
    await asyncio.gather(*[worker(i, 2 - i) for i in range(2)])
    
    # Try to run the third worker
    third_worker = asyncio.create_task(worker(2, 1))
    with pytest.raises(asyncio.exceptions.TimeoutError):
        await asyncio.wait([third_worker], timeout=0.1)
    third_worker.cancel()

@pytest.mark.asyncio
async def test_semaphore_as_context_manager(semaphore):
    """Test using the semaphore as an async context manager."""
    async def worker(worker_id):
        async with semaphore:
            assert semaphore._value == 2 - worker_id, "Semaphore value is incorrect inside the context"
            print("Worker %d is working" % worker_id)
            await asyncio.sleep(0)
    
    # Run multiple workers concurrently
    await asyncio.gather(*[worker(i) for i in range(2)])

@pytest.mark.asyncio
def test_semaphore_compatibility_with_context_manager(semaphore):
    """Test compatibility with older versions of Python using context manager."""
    @asyncio.coroutine
    def worker(worker_id):
        with (yield from semaphore.acquire()):
            assert semaphore._value == 2 - worker_id, "Semaphore value is incorrect inside the context"
            print("Worker %d is working" % worker_id)
            yield from asyncio.sleep(0)
    
    # Run multiple workers concurrently
    yield from asyncio.gather(*[worker(i) for i in range(2)])

if __name__ == "__main__":
    pytest.main()
