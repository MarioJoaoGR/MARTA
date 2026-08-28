
import pytest
from tornado.locks import Event
from unittest.mock import patch, MagicMock
from tornado.ioloop import IOLoop
from tornado import gen

# Test 1: Basic event setting and waiting
@pytest.mark.asyncio
async def test_valid_input():
    event = Event()

    async def waiter():
        print("Waiting for event")
        await event.wait()
        print("Not waiting this time")
        await event.wait()
        print("Done")

    async def setter():
        print("About to set the event")
        event.set()

    async def runner():
        await gen.multi([waiter(), setter()])

    with patch('tornado.ioloop.IOLoop.current') as mock_current:
        mock_loop = MagicMock()
        mock_current.return_value = mock_loop
        mock_loop.run_sync.side_effect = lambda coro: IOLoop().run_sync(coro)

        with patch('tornado.ioloop.IOLoop.run_sync') as mock_run_sync:
            mock_run_sync.return_value = None
            await runner()

    assert event._value == True

# Test 2: Edge case where the event is set immediately
@pytest.mark.asyncio
async def test_edge_case():
    event = Event()

    async def waiter():
        print("Waiting for event")
        await event.wait()
        print("Not waiting this time")
        await event.wait()
        print("Done")

    async def setter():
        print("About to set the event")
        event.set()

    async def runner():
        await gen.multi([waiter(), setter()])

    with patch('tornado.ioloop.IOLoop.current') as mock_current:
        mock_loop = MagicMock()
        mock_current.return_value = mock_loop
        mock_loop.run_sync.side_effect = lambda coro: IOLoop().run_sync(coro)

        with patch('tornado.ioloop.IOLoop.run_sync') as mock_run_sync:
            mock_run_sync.return_value = None
            await runner()

    assert event._value == True
