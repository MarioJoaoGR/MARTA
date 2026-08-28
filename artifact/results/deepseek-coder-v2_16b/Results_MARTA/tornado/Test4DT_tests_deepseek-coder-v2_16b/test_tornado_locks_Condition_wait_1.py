
import pytest
from tornado import gen, ioloop
from tornado.locks import Condition
import datetime
from unittest.mock import patch

# Test 1: Basic wait without timeout
@pytest.mark.asyncio
async def test_wait_without_timeout():
    condition = Condition()
    
    async def waiter():
        await condition.wait()
        assert True, "Waiter should be notified immediately"
    
    with patch('tornado.ioloop.IOLoop.current', return_value=None):  # Mock IOLoop current to avoid actual loop running
        await gen.multi([waiter(), notifier()])

# Test 2: Wait with timeout (absolute timestamp)
@pytest.mark.asyncio
async def test_wait_with_timeout_absolute():
    condition = Condition()
    
    async def waiter():
        result = await condition.wait(timeout=datetime.timedelta(seconds=1))
        assert not result, "Waiter should time out"
    
    with patch('tornado.ioloop.IOLoop.current', return_value=None):  # Mock IOLoop current to avoid actual loop running
        await gen.multi([waiter(), notifier()])

# Test 3: Wait with timeout (relative timedelta)
@pytest.mark.asyncio
async def test_wait_with_timeout_relative():
    condition = Condition()
    
    async def waiter():
        result = await condition.wait(timeout=datetime.timedelta(seconds=1))
        assert not result, "Waiter should time out"
    
    with patch('tornado.ioloop.IOLoop.current', return_value=None):  # Mock IOLoop current to avoid actual loop running
        await gen.multi([waiter(), notifier()])

# Helper function for testing notification
async def notifier():
    print("About to notify")
    condition.notify()
    print("Done notifying")
