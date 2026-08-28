# Module: tornado.locks
import pytest
from threading import BoundedSemaphore

# Test creating a BoundedSemaphore with an initial value of 2
def test_bounded_semaphore_initial_value():
    sem = BoundedSemaphore(value=2)
    assert sem._initial_value == 2

# Test releasing the semaphore more times than its initial value raises ValueError
def test_release_too_many_times():
    sem = BoundedSemaphore(value=2)
    with pytest.raises(ValueError):
        sem.release()
        sem.release()
        sem.release()  # This should raise ValueError

# Test creating a BoundedSemaphore with the default initial value of 1
def test_bounded_semaphore_default_value():
    sem = BoundedSemaphore()
    assert sem._initial_value == 1

# Test using a BoundedSemaphore in a multi-threaded environment
import threading

def worker(sem):
    for _ in range(2):  # Attempt to release the semaphore twice
        try:
            sem.release()
        except ValueError as e:
            print(e)  # This should raise ValueError on the third attempt

def test_bounded_semaphore_multithreaded():
    sem = BoundedSemaphore(value=2)
    threads = [threading.Thread(target=worker, args=(sem,)) for _ in range(3)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    with pytest.raises(ValueError):
        sem.release()  # This should raise ValueError after the second release in a different thread

# Test using a BoundedSemaphore with asyncio to limit the number of concurrent tasks
import asyncio

async def task(sem):
    await sem.acquire()  # Acquire the semaphore
    try:
        print("Task is running.")
        await asyncio.sleep(1)  # Simulate a task taking some time
    finally:
        print("Task is done, releasing the semaphore.")
        sem.release()

async def test_bounded_semaphore_asyncio():
    sem = BoundedSemaphore(value=2)
    tasks = [task(sem) for _ in range(4)]
    await asyncio.gather(*tasks)
    with pytest.raises(ValueError):
        sem.release()  # This should raise ValueError after the second release in an async task
