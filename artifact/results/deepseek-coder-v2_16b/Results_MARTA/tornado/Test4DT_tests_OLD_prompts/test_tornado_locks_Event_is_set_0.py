
import pytest
from tornado.locks import Event
from unittest.mock import patch, MagicMock

@pytest.mark.asyncio
async def test_event_wait():
    event = Event()
    
    async def waiter():
        print("Waiting for event")
        await event.wait()  # This will block until the event is set
        print("Not waiting this time")
        await event.wait()  # Again, wait until the event is set
        print("Done")
    
    async def setter():
        print("About to set the event")
        event.set()  # Set the event to allow waiter coroutine to proceed
    
    with patch('tornado.locks.Future') as mock_future:
        mock_waiter = MagicMock()
        mock_waiter.__await__ = lambda self: ()
        mock_event = MagicMock()
        mock_event._value = False
        mock_event._waiters = {mock_waiter}
        
        with patch.object(Event, '__init__', return_value=None):
            event = Event()
            assert isinstance(event, Event)
            
            await gen.multi([waiter(), setter()])
            mock_future.assert_called_with()
            mock_waiter.set_result.assert_called_once_with(None)
