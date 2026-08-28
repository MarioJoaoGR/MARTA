
import pytest
from unittest.mock import patch
import asyncio
from tornado.concurrent import Future

def future_set_result_unless_cancelled(future, value):
    if not future.cancelled():
        future.set_result(value)

@pytest.mark.asyncio
async def test_valid_input():
    with patch('tornado.concurrent.Future') as mock_future:
        # Mock the behavior of the Future object
        mock_future.return_value = mock_future
        mock_future.set_result_unless_cancelled = lambda value: None

        future = asyncio.Future()
        future_set_result_unless_cancelled(future, "example value")
        assert future.done(), "Future should be done after setting result"
        assert future.result() == "example value", "Result should be 'example value'"

@pytest.mark.asyncio
async def test_none_input():
    with patch('tornado.concurrent.Future') as mock_future:
        # Mock the behavior of the Future object
        mock_future.return_value = mock_future
        mock_future.set_result_unless_cancelled = lambda value: None

        future = asyncio.Future()
        future_set_result_unless_cancelled(future, None)
        assert future.done(), "Future should be done after setting result"
        assert future.result() is None, "Result should be None"

@pytest.mark.asyncio
async def test_cancelled_future():
    with patch('tornado.concurrent.Future') as mock_future:
        # Mock the behavior of the Future object
        mock_future.return_value = mock_future
        mock_future.set_result_unless_cancelled = lambda value: None

        future = asyncio.Future()
        future.cancel()
        assert future.cancelled(), "Future should be cancelled"
        
        future_set_result_unless_cancelled(future, "example value")
        assert future.done(), "Future should still be done after attempting to set result"
        with pytest.raises(asyncio.InvalidStateError):
            future.result()  # This should raise an InvalidStateError because the future is cancelled
