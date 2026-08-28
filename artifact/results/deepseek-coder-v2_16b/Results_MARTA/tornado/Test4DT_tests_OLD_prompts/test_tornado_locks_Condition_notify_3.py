
import pytest
from tornado.locks import Condition
import asyncio

@pytest.mark.asyncio
async def test_condition_notify():
    condition = Condition()

    async def waiter():
        print("I'll wait right here")
        await condition.wait()
        print("I'm done waiting")

    async def notifier():
        print("About to notify")
        condition.notify()
        print("Done notifying")

    # Start waiter and notifier concurrently
    coros = [waiter(), notifier()]
    await asyncio.gather(*coros)

    assert True  # If the test completes without errors, it passes

@pytest.mark.asyncio
async def test_condition_notify_with_timeout():
    condition = Condition()

    async def waiter():
        timeout = 0.1  # Wait up to 0.1 seconds for a notification
        notified = await condition.wait(timeout=timeout)
        if notified:
            print("Notified within the timeout")
        else:
            print("Timed out waiting for notification")

    async def notifier():
        await asyncio.sleep(0.05)  # Wait a bit before notifying
        print("About to notify")
        condition.notify()
        print("Done notifying")

    # Start waiter and notifier concurrently
    coros = [waiter(), notifier()]
    await asyncio.gather(*coros)

    assert True  # If the test completes without errors, it passes

@pytest.mark.asyncio
async def test_condition_notify_all():
    condition = Condition()

    async def waiter1():
        print("Waiter 1 will wait right here")
        await condition.wait()
        print("Waiter 1 is done waiting")

    async def waiter2():
        print("Waiter 2 will wait right here")
        await condition.wait()
        print("Waiter 2 is done waiting")

    async def notifier():
        print("About to notify all")
        condition.notify_all()
        print("Done notifying all")

    # Start two waiters and one notifier concurrently
    coros = [waiter1(), waiter2(), notifier()]
    await asyncio.gather(*coros)

    assert True  # If the test completes without errors, it passes
