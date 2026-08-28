
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

# Test case to cover line 118: self.__class__.__name__
@pytest.mark.asyncio
async def test_repr_basic(setup_condition):
    condition, loop = setup_condition
    assert repr(condition) == "<Condition>"

# Test case to cover line 119: if self._waiters
@pytest.mark.asyncio
async def test_repr_with_waiters(setup_condition):
    condition, loop = setup_condition
    async def waiter():
        await condition.wait()
    loop.run_until_complete(waiter())
    assert repr(condition) == "<Condition waiters[1]>"

# Test case to cover line 120: len(self._waiters)
@pytest.mark.asyncio
async def test_repr_with_multiple_waiters(setup_condition):
    condition, loop = setup_condition
    async def waiter():
        await condition.wait()
    async def waiter2():
        await condition.wait()
    loop.run_until_complete(asyncio.gather(waiter(), waiter2()))
    assert repr(condition) == "<Condition waiters[2]>"

# Test case to cover line 121: return result + ">"
@pytest.mark.asyncio
async def test_repr_empty(setup_condition):
    condition, loop = setup_condition
    assert repr(condition) == "<Condition>"

if __name__ == "__main__":
    pytest.main([__file__])
