
import pytest
from tornado.locks import Semaphore
from tornado.ioloop import IOLoop
from tornado.concurrent import Future
from collections import deque
import asyncio

# Ensure reliable doctest output: resolve Futures one at a time.
futures_q = deque([Future() for _ in range(3)])

async def simulator(futures):
    for f in futures:
        await asyncio.sleep(0)
        f.set_result(None)

IOLoop.current().add_callback(simulator, list(futures_q))

@pytest.fixture
def semaphore():
    return Semaphore(2)

async def worker(sem, worker_id):
    async with sem:
        print(f"Worker {worker_id} is working")
        await use_some_resource()

async def runner():
    sem = Semaphore(2)
    await asyncio.gather(*[worker(sem, i) for i in range(3)])

def test_edge_case():
    with pytest.raises(Exception):
        with Semaphore(0):
            raise Exception("This should be raised")
