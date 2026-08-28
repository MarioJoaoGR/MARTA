
import pytest
from unittest.mock import patch, MagicMock
from tornado.locks import Condition
from tornado.ioloop import IOLoop
import asyncio

@pytest.mark.asyncio
async def test_valid_input():
    condition = Condition()
    with patch('tornado.ioloop.IOLoop.current', return_value=MagicMock(name='io_loop')):
        async def waiter():
            print("I'll wait right here")
            await condition.wait()
            print("I'm done waiting")

        async def notifier():
            print("About to notify")
            condition.notify()
            print("Done notifying")

        async def runner():
            # Wait for waiter() and notifier() in parallel
            await asyncio.gather(waiter(), notifier())

        IOLoop.current().run_sync(runner)
    assert len(condition._Condition__waiters) == 1, "Expected one waiter to be waiting"
