
import pytest
from tornado.queues import Queue
from tornado.ioloop import IOLoop
import asyncio

@pytest.mark.asyncio
async def test_queue_task_done():
    q = Queue(maxsize=2)

    # Start consumer without waiting (since it never finishes).
    async def consumer():
        async for item in q:
            try:
                print('Doing work on %s' % item)
                await asyncio.sleep(0.01)  # Use asyncio sleep instead of Tornado's gen.sleep
            finally:
                q.task_done()

    async def producer():
        for item in range(5):
            await q.put(item)
            print('Put %s' % item)

    async def main():
        IOLoop.current().spawn_callback(consumer)
        await producer()  # Wait for producer to put all tasks.
        await q.join()    # Wait for consumer to finish all tasks.
        print('Done')

    await main()
    assert q._unfinished_tasks == 0, "All tasks should be done"

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
