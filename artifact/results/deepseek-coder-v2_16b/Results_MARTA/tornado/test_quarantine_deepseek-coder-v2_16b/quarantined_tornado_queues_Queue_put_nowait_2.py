
import pytest
from tornado.queues import Queue
from concurrent.futures import Future


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b/test_tornado_queues_Queue_put_nowait_2.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
____________________________ test_error_put_nowait _____________________________

    def test_error_put_nowait():
        q = Queue(maxsize=2)
        q.put_nowait(0)
        q.put_nowait(1)
>       with pytest.raises(QueueFull):
E       NameError: name 'QueueFull' is not defined

/opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b/test_tornado_queues_Queue_put_nowait_2.py:10: NameError
__________________________ test_error_put_nowait_none __________________________

    def test_error_put_nowait_none():
        q = Queue()
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

/opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b/test_tornado_queues_Queue_put_nowait_2.py:15: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b/test_tornado_queues_Queue_put_nowait_2.py::test_error_put_nowait
FAILED ../../../../../opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b/test_tornado_queues_Queue_put_nowait_2.py::test_error_put_nowait_none
============================== 2 failed in 0.10s ===============================
"""