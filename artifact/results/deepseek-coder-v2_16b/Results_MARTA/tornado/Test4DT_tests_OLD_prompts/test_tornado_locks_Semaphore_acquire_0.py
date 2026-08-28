
import pytest
from tornado.locks import Semaphore
from tornado.ioloop import IOLoop
from tornado.concurrent import Future
import asyncio

@pytest.mark.asyncio
async def test_semaphore_acquire():
    sem = Semaphore(2)
    
    async def worker(worker_id):
        await sem.acquire()
        try:
            print("Worker %d is working" % worker_id)
            # Simulate accessing a shared resource
            await asyncio.sleep(0)
            await asyncio.sleep(0)
        finally:
            print("Worker %d is done" % worker_id)
            sem.release()
    
    await asyncio.gather(*[worker(i) for i in range(3)])

@pytest.mark.asyncio
async def test_semaphore_acquire_timeout():
    sem = Semaphore(1)
    
    with pytest.raises(asyncio.TimeoutError):
        await sem.acquire(timeout=0.1)

@pytest.mark.asyncio
async def test_semaphore_context_manager():
    sem = Semaphore(1)
    
    async def worker(worker_id):
        async with sem:
            print("Worker %d is working" % worker_id)
            await asyncio.sleep(0)
            await asyncio.sleep(0)
    
    await asyncio.gather(*[worker(i) for i in range(3)])
