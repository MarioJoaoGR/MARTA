
import pytest
from pytutils.iters import consume

def test_invalid_input_none_type():
    lst = [1, 2, 3, 4]
    it = iter(lst)
    
    with pytest.raises(TypeError):
        consume(it, None)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pytutils
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

pytutils/Test4DT_tests/test_pytutils_iters_consume_1_test_invalid_input_none_type.py F [100%]

=================================== FAILURES ===================================
_________________________ test_invalid_input_none_type _________________________

    def test_invalid_input_none_type():
        lst = [1, 2, 3, 4]
        it = iter(lst)
    
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

pytutils/Test4DT_tests/test_pytutils_iters_consume_1_test_invalid_input_none_type.py:9: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_iters_consume_1_test_invalid_input_none_type.py::test_invalid_input_none_type
============================== 1 failed in 0.05s ===============================
"""