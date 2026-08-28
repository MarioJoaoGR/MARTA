
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
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b/test_thonny_roughparse_RoughParser_get_last_open_bracket_pos_0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
________________________ test_get_last_open_bracket_pos ________________________

    def test_get_last_open_bracket_pos():
        parser = RoughParser(indent_width=4, tabwidth=4)
        with pytest.raises(ValueError):
>           assert parser.get_last_open_bracket_pos() is None

/opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b/test_thonny_roughparse_RoughParser_get_last_open_bracket_pos_0.py:8: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/thonny/thonny/roughparse.py:646: in get_last_open_bracket_pos
    self._study2()
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <thonny.roughparse.RoughParser object at 0x7fb9f96272e0>

    def _study2(self):
        # pylint: disable=redefined-builtin
    
>       if self.study_level >= 2:
E       AttributeError: 'RoughParser' object has no attribute 'study_level'

/opt/marta/baselines/codamosa/replication/test-apps/thonny/thonny/roughparse.py:416: AttributeError
_________________ test_get_last_open_bracket_pos_with_brackets _________________

    def test_get_last_open_bracket_pos_with_brackets():
        code = "if True:\n    print('Hello, World!')"
        parser = RoughParser(indent_width=4, tabwidth=4)
>       parser._study2()  # Manually trigger the study to set lastopenbracketpos

/opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b/test_thonny_roughparse_RoughParser_get_last_open_bracket_pos_0.py:13: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <thonny.roughparse.RoughParser object at 0x7fb9f9f0ee60>

    def _study2(self):
        # pylint: disable=redefined-builtin
    
>       if self.study_level >= 2:
E       AttributeError: 'RoughParser' object has no attribute 'study_level'

/opt/marta/baselines/codamosa/replication/test-apps/thonny/thonny/roughparse.py:416: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b/test_thonny_roughparse_RoughParser_get_last_open_bracket_pos_0.py::test_get_last_open_bracket_pos
FAILED ../../../../../opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b/test_thonny_roughparse_RoughParser_get_last_open_bracket_pos_0.py::test_get_last_open_bracket_pos_with_brackets
============================== 2 failed in 0.07s ===============================
"""