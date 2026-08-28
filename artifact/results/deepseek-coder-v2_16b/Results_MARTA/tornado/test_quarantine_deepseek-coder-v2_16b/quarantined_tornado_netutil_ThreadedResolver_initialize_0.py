
import pytest
from tornado.netutil import ThreadedResolver


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b/test_tornado_netutil_ThreadedResolver_initialize_0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
___________________ test_invalid_input_negative_num_threads ____________________

    def test_invalid_input_negative_num_threads():
        with pytest.raises(ValueError) as excinfo:
            resolver = ThreadedResolver(num_threads=-1)
>       assert str(excinfo.value) == "num_threads must be greater than 0"
E       AssertionError: assert 'max_workers ...reater than 0' == 'num_threads ...reater than 0'
E         
E         - num_threads must be greater than 0
E         ? --  ^^  ^^
E         + max_workers must be greater than 0
E         ?  ++ ^^ + ^

/opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b/test_tornado_netutil_ThreadedResolver_initialize_0.py:8: AssertionError
_____________________ test_invalid_input_zero_num_threads ______________________

    def test_invalid_input_zero_num_threads():
        with pytest.raises(ValueError) as excinfo:
            resolver = ThreadedResolver(num_threads=0)
>       assert str(excinfo.value) == "num_threads must be greater than 0"
E       AssertionError: assert 'max_workers ...reater than 0' == 'num_threads ...reater than 0'
E         
E         - num_threads must be greater than 0
E         ? --  ^^  ^^
E         + max_workers must be greater than 0
E         ?  ++ ^^ + ^

/opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b/test_tornado_netutil_ThreadedResolver_initialize_0.py:13: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b/test_tornado_netutil_ThreadedResolver_initialize_0.py::test_invalid_input_negative_num_threads
FAILED ../../../../../opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b/test_tornado_netutil_ThreadedResolver_initialize_0.py::test_invalid_input_zero_num_threads
============================== 2 failed in 0.10s ===============================
"""