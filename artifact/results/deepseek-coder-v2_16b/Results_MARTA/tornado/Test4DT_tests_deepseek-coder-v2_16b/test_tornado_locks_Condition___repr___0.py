
import pytest
from tornado.locks import Condition
import asyncio

@pytest.fixture
def condition():
    return Condition()

# Test Scenario 1: Valid Case
def test_valid_case(condition):
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

    loop = asyncio.get_event_loop()
    loop.run_until_complete(runner())

# Test Scenario 2: Edge Case
def test_edge_case(condition):
    async def waiter():
        print("I'll wait right here")
        await condition.wait()
        print("I'm done waiting")

    async def runner():
        # Wait for waiter() in parallel
        with pytest.raises(asyncio.TimeoutError):
            await asyncio.wait_for(waiter(), timeout=0.1)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(runner())

# Test Scenario 3: Error Handling
def test_error_handling():
    with pytest.raises(TypeError):
        Condition("invalid input")
