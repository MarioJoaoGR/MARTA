
import pytest
from thonny.roughparse import RoughParser



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b/test_thonny_roughparse_RoughParser_get_num_lines_in_stmt_1.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
__________________________ test_invalid_indent_width ___________________________

    def test_invalid_indent_width():
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

/opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b/test_thonny_roughparse_RoughParser_get_num_lines_in_stmt_1.py:6: Failed
____________________________ test_invalid_tabwidth _____________________________

    def test_invalid_tabwidth():
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

/opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b/test_thonny_roughparse_RoughParser_get_num_lines_in_stmt_1.py:10: Failed
_______________________ test_valid_get_num_lines_in_stmt _______________________

    def test_valid_get_num_lines_in_stmt():
        parser = RoughParser(indent_width=4, tabwidth=4)
>       assert parser.get_num_lines_in_stmt() == 1

/opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b/test_thonny_roughparse_RoughParser_get_num_lines_in_stmt_1.py:15: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/thonny/thonny/roughparse.py:557: in get_num_lines_in_stmt
    self._study1()
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <thonny.roughparse.RoughParser object at 0x7fe239f03b50>

    def _study1(self):
        # pylint: disable=redefined-builtin
    
>       if self.study_level >= 1:
E       AttributeError: 'RoughParser' object has no attribute 'study_level'

/opt/marta/baselines/codamosa/replication/test-apps/thonny/thonny/roughparse.py:258: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b/test_thonny_roughparse_RoughParser_get_num_lines_in_stmt_1.py::test_invalid_indent_width
FAILED ../../../../../opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b/test_thonny_roughparse_RoughParser_get_num_lines_in_stmt_1.py::test_invalid_tabwidth
FAILED ../../../../../opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b/test_thonny_roughparse_RoughParser_get_num_lines_in_stmt_1.py::test_valid_get_num_lines_in_stmt
============================== 3 failed in 0.06s ===============================
"""