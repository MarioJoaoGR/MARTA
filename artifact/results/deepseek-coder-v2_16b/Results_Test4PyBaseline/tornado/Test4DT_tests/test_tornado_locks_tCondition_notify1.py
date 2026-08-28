
import pytest
from tornado.locks import Condition
from collections import deque
import asyncio  # Importing asyncio explicitly

@pytest.fixture
def setup_condition():
    condition = Condition()
    return condition

# Test for the notify method with different numbers of waiters
def test_notify_with_multiple_waiters(setup_condition):
    """Test notify with multiple waiters."""
    condition = setup_condition
    
    # Create multiple waiter coroutines
    async def waiter1():
        await condition.wait()

    async def waiter2():
        await condition.wait()
    
    # Add two waiters to the condition's waiters list
    condition._waiters = deque([asyncio.Future(), asyncio.Future()])
    
    # Notify all waiters
    condition.notify(n=2)
    
    # Check that both futures are set
    assert len(condition._waiters) == 0

# Test for the notify method with no waiters initially
def test_notify_with_no_initial_waiters(setup_condition):
    """Test notify when there are no initial waiters."""
    condition = setup_condition
    
    # Notify without any waiters
    condition.notify(n=1)
    
    # Check that the number of waiters remains unchanged
    assert len(condition._waiters) == 0

# Test for the notify method with fewer notifications than waiters
def test_notify_with_fewer_notifications(setup_condition):
    """Test notify when there are more waiters than notifications."""
    condition = setup_condition
    
    # Add multiple waiters to the condition's waiters list
    condition._waiters = deque([asyncio.Future(), asyncio.Future(), asyncio.Future()])
    
    # Notify only a few waiters
    condition.notify(n=2)
    
    # Check that only the first two futures are set
    assert len(condition._waiters) == 1

# Test for the notify method with more notifications than waiters
def test_notify_with_more_notifications(setup_condition):
    """Test notify when there are fewer waiters than notifications."""
    condition = setup_condition
    
    # Add a single waiter to the condition's waiters list
    condition._waiters = deque([asyncio.Future()])
    
    # Notify more than one waiter, but only one exists
    condition.notify(n=2)
    
    # Check that only one future is set
    assert len(condition._waiters) == 0

# Test for the notify method with notifications exceeding the number of waiters
def test_notify_with_excessive_notifications(setup_condition):
    """Test notify when there are more notifications than actual waiters."""
    condition = setup_condition
    
    # Add a single waiter to the condition's waiters list
    condition._waiters = deque([asyncio.Future()])
    
    # Notify with a number greater than the number of waiters
    condition.notify(n=2)
    
    # Check that only one future is set
    assert len(condition._waiters) == 0
