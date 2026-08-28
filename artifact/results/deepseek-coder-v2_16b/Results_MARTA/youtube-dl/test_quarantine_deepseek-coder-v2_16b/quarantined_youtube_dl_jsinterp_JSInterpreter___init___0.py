
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
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_jsinterp_JSInterpreter___init___0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
_____________________ test_valid_case_basic_initialization _____________________

    def test_valid_case_basic_initialization():
        interpreter = JSInterpreter("function add(a, b) { return a + b; } var result = add(5, 3);")
>       assert "function add(a, b) { return a + b; }" in interpreter._functions.values()
E       AssertionError: assert 'function add(a, b) { return a + b; }' in dict_values([])
E        +  where dict_values([]) = <built-in method values of dict object at 0x7fb317f09340>()
E        +    where <built-in method values of dict object at 0x7fb317f09340> = {}.values
E        +      where {} = <youtube_dl.jsinterp.JSInterpreter object at 0x7fb317eda0e0>._functions

/opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_jsinterp_JSInterpreter___init___0.py:7: AssertionError
_____________________ test_valid_case_with_initial_objects _____________________

    def test_valid_case_with_initial_objects():
        initial_objects = {'a': 5, 'b': 3}
        interpreter = JSInterpreter("function add(a, b) { return a + b; } var result = add(a, b);", objects=initial_objects)
>       assert "function add(a, b) { return a + b; }" in interpreter._functions.values()
E       AssertionError: assert 'function add(a, b) { return a + b; }' in dict_values([])
E        +  where dict_values([]) = <built-in method values of dict object at 0x7fb317d72740>()
E        +    where <built-in method values of dict object at 0x7fb317d72740> = {}.values
E        +      where {} = <youtube_dl.jsinterp.JSInterpreter object at 0x7fb317edbd90>._functions

/opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_jsinterp_JSInterpreter___init___0.py:12: AssertionError
_________________________ test_error_case_invalid_code _________________________

    def test_error_case_invalid_code():
>       with pytest.raises(SyntaxError):
E       Failed: DID NOT RAISE <class 'SyntaxError'>

/opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_jsinterp_JSInterpreter___init___0.py:15: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_jsinterp_JSInterpreter___init___0.py::test_valid_case_basic_initialization
FAILED ../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_jsinterp_JSInterpreter___init___0.py::test_valid_case_with_initial_objects
FAILED ../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_jsinterp_JSInterpreter___init___0.py::test_error_case_invalid_code
============================== 3 failed in 0.56s ===============================
"""