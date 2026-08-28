
import pytest
from tornado.concurrent import Future
from concurrent.futures import Future as CFuture

def future_add_done_callback(  # noqa: F811
    future: "Union[CFuture[_T], Future[_T]]", callback: Callable[..., None]
) -> None:
    """Arrange to call ``callback`` when ``future`` is complete.

    ``callback`` is invoked with one argument, the ``future``.

    If ``future`` is already done, ``callback`` is invoked immediately.
    This may differ from the behavior of ``Future.add_done_callback``,
    which makes no such guarantee.

    .. versionadded:: 5.0
    """
    if future.done():
        callback(future)
    else:
        future.add_done_callback(callback)

# Test for valid input
def test_valid_input():
    future = Future()
    called = False
    
    def callback(f):
        nonlocal called
        called = True
        assert f.result() is None  # Assuming the default result of an empty Future is None
    
    future_add_done_callback(future, callback)
    future.set_result(None)
    assert called

# Test for invalid input (should raise TypeError)
def test_invalid_input():
    with pytest.raises(TypeError):
        future_add_done_callback(42, lambda: None)  # Passing an int instead of a Future

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
____ ERROR collecting test_tornado_concurrent_future_add_done_callback_0.py ____
/opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b/test_tornado_concurrent_future_add_done_callback_0.py:7: in <module>
    future: "Union[CFuture[_T], Future[_T]]", callback: Callable[..., None]
E   NameError: name 'Callable' is not defined
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b/test_tornado_concurrent_future_add_done_callback_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.14s ===============================
"""