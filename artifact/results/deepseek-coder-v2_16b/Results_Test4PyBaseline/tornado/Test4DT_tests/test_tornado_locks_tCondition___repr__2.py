
# Module: tornado.locks
import pytest
from tornado.locks import Condition
from tornado.ioloop import IOLoop
import asyncio
import datetime

@pytest.fixture
def setup_condition():
    condition = Condition()
    loop = asyncio.get_event_loop()
    return condition, loop

# Test case to cover the __repr__ method with no waiters
@pytest.mark.asyncio
async def test_repr_no_waiters(setup_condition):
    condition, loop = setup_condition
    repr_str = condition.__repr__()
    assert repr_str == f"<{Condition.__name__}>"

# Test case to cover the __repr__ method with waiters
@pytest.mark.asyncio
async def test_repr_with_waiters(setup_condition):
    condition, loop = setup_condition
    # Simulate adding a waiter
    async def waiter():
        await asyncio.sleep(0)  # Just to simulate waiting
    loop.run_until_complete(condition._wait())
    repr_str = condition.__repr__()
    assert repr_str == f"<{Condition.__name__} waiters[1]>"

# Test case to cover the __repr__ method with multiple waiters
@pytest.mark.asyncio
async def test_repr_with_multiple_waiters(setup_condition):
    condition, loop = setup_condition
    # Simulate adding multiple waiters
    async def waiter():
        await asyncio.sleep(0)  # Just to simulate waiting
    for _ in range(3):
        loop.run_until_complete(condition._wait())
    repr_str = condition.__repr__()
    assert repr_str == f"<{Condition.__name__} waiters[3]>"

if __name__ == "__main__":
    pytest.main([__file__])
