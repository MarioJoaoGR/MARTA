
import pytest
from youtube_dl.jsinterp import JSInterpreter


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_jsinterp_JSInterpreter_interpret_statement_0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        interpreter = JSInterpreter("function add(a, b) { return a + b; } var result = add(5, 3);")
>       assert 'function' in str(interpreter._functions['add'])
E       KeyError: 'add'

/opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_jsinterp_JSInterpreter_interpret_statement_0.py:7: KeyError
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
>       with pytest.raises(KeyError):
E       Failed: DID NOT RAISE <class 'KeyError'>

/opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_jsinterp_JSInterpreter_interpret_statement_0.py:11: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_jsinterp_JSInterpreter_interpret_statement_0.py::test_valid_input
FAILED ../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_jsinterp_JSInterpreter_interpret_statement_0.py::test_invalid_input
============================== 2 failed in 0.56s ===============================
"""