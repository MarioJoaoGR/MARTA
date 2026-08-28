
import pytest
from thonny.roughparse import StringTranslatePseudoMapping


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b/test_thonny_roughparse_StringTranslatePseudoMapping_get_1.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        whitespace_chars = ' \t\n\r'
        preserve_dict = {ord(c): ord(c) for c in whitespace_chars}
        mapping = StringTranslatePseudoMapping(preserve_dict, ord('x'))
        text = "a + b\tc\nd"
        translated_text = text.translate(mapping)
>       assert translated_text == 'a + b\tx\nx'
E       AssertionError: assert 'x x x\tx\nx' == 'a + b\tx\nx'
E         
E         - a + b	x
E         + x x x	x
E           x

/opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b/test_thonny_roughparse_StringTranslatePseudoMapping_get_1.py:11: AssertionError
_____________________________ test_edge_case_none ______________________________

    def test_edge_case_none():
>       mapping = StringTranslatePseudoMapping(None, ord('x'))

/opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b/test_thonny_roughparse_StringTranslatePseudoMapping_get_1.py:14: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <thonny.roughparse.StringTranslatePseudoMapping object at 0x7f7c5a40a080>
non_defaults = None, default_value = 120

    def __init__(self, non_defaults, default_value):
        self._non_defaults = non_defaults
        self._default_value = default_value
    
>       def _get(key, _get=non_defaults.get, _default=default_value):
E       AttributeError: 'NoneType' object has no attribute 'get'

/opt/marta/baselines/codamosa/replication/test-apps/thonny/thonny/roughparse.py:144: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b/test_thonny_roughparse_StringTranslatePseudoMapping_get_1.py::test_valid_input
FAILED ../../../../../opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b/test_thonny_roughparse_StringTranslatePseudoMapping_get_1.py::test_edge_case_none
============================== 2 failed in 0.06s ===============================
"""