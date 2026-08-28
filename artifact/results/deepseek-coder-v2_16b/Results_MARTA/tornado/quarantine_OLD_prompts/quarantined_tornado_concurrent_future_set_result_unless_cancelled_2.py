
import pytest
from unittest.mock import patch, MagicMock
from tornado.concurrent import Future
from typing import Union

def future_set_result_unless_cancelled(future: "Union[Future[_T], Future[_T]]", value: _T) -> None:
    """Set the given ``value`` as the `Future`'s result if not cancelled.

    This function checks if the future is not cancelled before attempting to set its result. If the future has been cancelled, it does nothing to avoid raising an ``asyncio.InvalidStateError``.

    Parameters:
        future (Union[Future[_T], Future[_T]]): The asynchronous future object to which the value will be set if not cancelled.
        value (_T): The value that will be set as the result of the future, if it is not cancelled.

    Returns:
        None
    """
    if not future.cancelled():
        future.set_result(value)

@pytest.mark.parametrize("future, value", [
    (Future(), "example value"),
    (Future(), 42),
])
def test_future_set_result_unless_cancelled(future, value):
    with patch('tornado.concurrent.Future') as mock_future:
        # Create a MagicMock for the future object
        mock_future = MagicMock()
        
        # Set up the mock to return itself when calling `cancelled()` and `set_result(value)`
        mock_future.cancelled.return_value = False
        mock_future.set_result.return_value = None
        
        # Call the function under test
        future_set_result_unless_cancelled(mock_future, value)
        
        # Assert that `set_result` was called with the correct value
        mock_future.set_result.assert_called_once_with(value)

if __name__ == "__main__":
    pytest.main()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 0 items / 1 error

==================================== ERRORS ====================================
_ ERROR collecting test_tornado_concurrent_future_set_result_unless_cancelled_2.py _
/opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b/test_tornado_concurrent_future_set_result_unless_cancelled_2.py:7: in <module>
    def future_set_result_unless_cancelled(future: "Union[Future[_T], Future[_T]]", value: _T) -> None:
E   NameError: name '_T' is not defined
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b/test_tornado_concurrent_future_set_result_unless_cancelled_2.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.16s ===============================
"""