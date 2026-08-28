
import pytest
from unittest.mock import patch
from thonny.jedi_utils import get_interpreter_completions


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b/test_thonny_jedi_utils_get_interpreter_completions_0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_____________________________ test_edge_case_none ______________________________

    def test_edge_case_none():
        source = ""
        namespaces = []
        with patch('thonny.jedi_utils._using_older_jedi', return_value=False):
            completions = get_interpreter_completions(source, namespaces)
>           assert len(completions) == 0, "Expected no completions for empty source"
E           AssertionError: Expected no completions for empty source
E           assert 170 == 0
E            +  where 170 = len([<thonny.jedi_utils.ThonnyCompletion object at 0x7f4e42935fc0>, <thonny.jedi_utils.ThonnyCompletion object at 0x7f4e42...i_utils.ThonnyCompletion object at 0x7f4e42aa2ce0>, <thonny.jedi_utils.ThonnyCompletion object at 0x7f4e42aa2e30>, ...])

/opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b/test_thonny_jedi_utils_get_interpreter_completions_0.py:11: AssertionError
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        source = "invalid code"
        namespaces = [{'os': None}]
        with patch('thonny.jedi_utils._using_older_jedi', return_value=False):
>           with pytest.raises(Exception):
E           Failed: DID NOT RAISE <class 'Exception'>

/opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b/test_thonny_jedi_utils_get_interpreter_completions_0.py:17: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b/test_thonny_jedi_utils_get_interpreter_completions_0.py::test_edge_case_none
FAILED ../../../../../opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b/test_thonny_jedi_utils_get_interpreter_completions_0.py::test_invalid_input
============================== 2 failed in 0.26s ===============================
"""