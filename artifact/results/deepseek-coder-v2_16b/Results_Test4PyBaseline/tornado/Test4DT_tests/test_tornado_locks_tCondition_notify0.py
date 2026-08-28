
# Module: tornado.locks
import pytest
from tornado.locks import Condition
from tornado.ioloop import IOLoop
import asyncio
import datetime

@pytest.fixture
def setup_condition():
    condition = Condition()
    return condition

@pytest.mark.asyncio
async def test_notify(setup_condition, capsys):
    """Test the notify method of Condition class."""
    condition = setup_condition
    
    # Create a waiter coroutine
    async def waiter():
        print("I'll wait right here")
        await condition.wait()
        print("I'm done waiting")

    # Create a notifier coroutine
    async def notifier():
        print("About to notify")
        condition.notify(n=1)
        print("Done notifying")

    # Run waiter and notifier concurrently
    await asyncio.gather(waiter(), notifier())
    
    captured = capsys.readouterr()
    assert "I'm done waiting" in captured.out

@pytest.mark.asyncio
async def test_notify_with_timeout(setup_condition, capsys):
    """Test the notify method with a timeout."""
    condition = setup_condition
    
    # Create a waiter coroutine with a timeout
    async def waiter():
        print("I'll wait right here")
        await condition.wait(timeout=datetime.timedelta(seconds=1))
        if not condition._waiters:  # Check if no more waiters are left
            print("Timed out waiting for the condition to be notified.")
        else:
            print("I'm done waiting")

    # Create a notifier coroutine
    async def notifier():
        print("About to notify")
        condition.notify(n=1)  # Notify one waiter
        print("Done notifying")

    # Run waiter and notifier concurrently
    await asyncio.gather(waiter(), notifier())
    
    captured = capsys.readouterr()
    assert "I'll wait right here" in captured.out
    assert "Timed out waiting for the condition to be notified." in captured.out
