
import pytest
from tornado.util import exec_in


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b/test_tornado_util_exec_in_0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
____________________________ test_valid_code_string ____________________________

    def test_valid_code_string():
        code_str = 'x = 5\ny = x + 3'
        global_scope = {}
        local_scope = {}
        exec_in(code_str, global_scope, local_scope)
>       assert global_scope['x'] == 5
E       KeyError: 'x'

/opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b/test_tornado_util_exec_in_0.py:10: KeyError
___________________________ test_valid_compiled_code ___________________________

    def test_valid_compiled_code():
        code_str = 'x = 5\ny = x + 3'
        global_scope = {}
        local_scope = {}
        compiled_code = compile(code_str, "<string>", "exec")
        exec_in(compiled_code, global_scope, local_scope)
>       assert global_scope['x'] == 5
E       KeyError: 'x'

/opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b/test_tornado_util_exec_in_0.py:19: KeyError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b/test_tornado_util_exec_in_0.py::test_valid_code_string
FAILED ../../../../../opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b/test_tornado_util_exec_in_0.py::test_valid_compiled_code
============================== 2 failed in 0.07s ===============================
"""