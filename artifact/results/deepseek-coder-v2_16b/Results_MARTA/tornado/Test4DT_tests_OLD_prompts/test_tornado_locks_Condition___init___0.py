
import pytest
from tornado.locks import Condition
from tornado.ioloop import IOLoop
import asyncio

@pytest.mark.asyncio
async def test_valid_case():
    condition = Condition()

    async def waiter():
        print("I'll wait right here")
        await condition.wait()
        print("I'm done waiting")

    async def notifier():
        print("About to notify")
        condition.notify()
        print("Done notifying")

    async def runner():
        await asyncio.gather(waiter(), notifier())

    with pytest.raises(asyncio.TimeoutError):  # We expect a timeout since the notification is immediate
        await asyncio.wait_for(runner(), timeout=0.1)

@pytest.mark.asyncio
async def test_invalid_input():
    condition = Condition()

    with pytest.raises(ValueError):
        condition.notify()  # This should raise a ValueError because notify requires an argument
