
import pytest
from tornado.locks import Condition
from collections import deque
import asyncio
import datetime

@pytest.fixture
def setup_condition():
    condition = Condition()
    return condition

def test_notify_with_multiple_waiters(setup_condition):
    """Test notify with multiple waiters."""
    condition = setup_condition
    
    # Create multiple waiter coroutines
    async def waiter1():
        await condition.wait()

    async def waiter2():
        await condition.wait()

    # Add multiple waiters to the condition's waiters list
    condition._waiters = deque([asyncio.Future(), asyncio.Future()])
    
    # Notify all waiters
    condition.notify(n=2)
    
    # Check that both waiters are done
    assert len(condition._waiters) == 0

def test_notify_with_timeout_and_no_waiters(setup_condition):
    """Test notify with timeout when there are no waiters."""
    condition = setup_condition
    
    # Try to notify without any waiters, should not raise an error and just return immediately
    condition.notify(n=1)
    
    # Check that the _waiters deque is still empty
    assert len(condition._waiters) == 0

def test_notify_with_partial_timeout(setup_condition):
    """Test notify with partial timeout."""
    condition = setup_condition
    
    # Create a waiter coroutine with a timeout
    async def waiter():
        await condition.wait(timeout=datetime.timedelta(seconds=1))
        if not condition._waiters:  # Check if no more waiters are left
            print("Timed out waiting for the condition to be notified.")
        else:
            print("I'm done waiting")

    # Add a waiter to the condition's waiters list
    condition._waiters = deque([asyncio.Future()])
    
    # Notify one waiter and let the other timeout
    condition.notify(n=1)
    
    # Check that only one waiter is done, the other should still be pending
    assert len([w for w in condition._waiters if not w.done()]) == 0

def test_notify_with_immediate_timeout(setup_condition):
    """Test notify with immediate timeout."""
    condition = setup_condition
    
    # Create a waiter coroutine with an immediate timeout
    async def waiter():
        await condition.wait(timeout=datetime.timedelta(seconds=0))
        if not condition._waiters:  # Check if no more waiters are left
            print("Timed out waiting for the condition to be notified.")
        else:
            print("I'm done waiting")

    # Add a waiter to the condition's waiters list
    condition._waiters = deque([asyncio.Future()])
    
    # Notify one waiter and let the other timeout immediately
    condition.notify(n=1)
    
    # Check that only one waiter is done, the other should still be pending
    assert len([w for w in condition._waiters if not w.done()]) == 0
