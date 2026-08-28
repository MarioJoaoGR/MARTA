
import pytest
from tornado import concurrent
from typing import Union, TypeVar

_T = TypeVar('_T')

def future_set_result_unless_cancelled(
    future: "Union[concurrent.futures.Future[_T], Future[_T]]", value: _T
) -> None:
    """Set the given ``value`` as the `Future`'s result if not cancelled.

    This function checks if the future is not cancelled before attempting to set its result. If the future has been cancelled, it does nothing to avoid raising an ``asyncio.InvalidStateError``.

    Parameters:
        future (Union[concurrent.futures.Future[_T], Future[_T]]): The asynchronous future object to which the value will be set if not cancelled.
        value (_T): The value that will be set as the result of the future, if it is not cancelled.

    Returns:
        None
    """
    if not future.cancelled():
        future.set_result(value)

@pytest.mark.parametrize("future, value", [
    (concurrent.futures.Future(), "example value"),
    (concurrent.futures.Future(), 42),
])
def test_future_set_result_unless_cancelled(future, value):
    future_set_result_unless_cancelled(future, value)
    assert not future.cancelled()
    if isinstance(future, concurrent.futures.Future):
        assert future.result() == value
    else:
        # For asyncio Future, we don't have a direct equivalent of .result(), but we can check done status
        assert future.done()

if __name__ == "__main__":
    pytest.main()
