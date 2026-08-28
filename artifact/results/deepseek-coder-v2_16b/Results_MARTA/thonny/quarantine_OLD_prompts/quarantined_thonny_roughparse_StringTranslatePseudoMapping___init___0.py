
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
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b/test_thonny_roughparse_StringTranslatePseudoMapping___init___0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
_____________ test_StringTranslatePseudoMapping_replace_whitespace _____________

    def test_StringTranslatePseudoMapping_replace_whitespace():
        whitespace_chars = ' \t\n\r'
        preserve_dict = {ord(c): ord(c) for c in whitespace_chars}
        mapping = StringTranslatePseudoMapping(preserve_dict, ord('x'))
        text = "a + b\tc\nd"
        translated_text = text.translate(mapping)
>       assert translated_text == 'a + b   c  d'
E       AssertionError: assert 'x x x\tx\nx' == 'a + b   c  d'
E         
E         - a + b   c  d
E         + x x x	x
E         + x

/opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b/test_thonny_roughparse_StringTranslatePseudoMapping___init___0.py:11: AssertionError
________________ test_StringTranslatePseudoMapping_replace_all _________________

    def test_StringTranslatePseudoMapping_replace_all():
        preserve_dict = {'H': 'h', 'e': 'E', 'o': 'O'}
        mapping = StringTranslatePseudoMapping(preserve_dict, ord('x'))
        text = "Hello, World!"
        translated_text = text.translate(mapping)
>       assert translated_text == 'hellO, WorlOd!'
E       AssertionError: assert 'xxxxxxxxxxxxx' == 'hellO, WorlOd!'
E         
E         - hellO, WorlOd!
E         + xxxxxxxxxxxxx

/opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b/test_thonny_roughparse_StringTranslatePseudoMapping___init___0.py:18: AssertionError
______________ test_StringTranslatePseudoMapping_replace_specific ______________

    def test_StringTranslatePseudoMapping_replace_specific():
        preserve_dict = {'H': 'h', 'e': 'E', 'o': 'O'}
        mapping = StringTranslatePseudoMapping(preserve_dict, ord('x'))
        text = "Hello, World!"
        translated_text = text.translate(mapping)
>       assert translated_text == 'hellO, WorlOd!'
E       AssertionError: assert 'xxxxxxxxxxxxx' == 'hellO, WorlOd!'
E         
E         - hellO, WorlOd!
E         + xxxxxxxxxxxxx

/opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b/test_thonny_roughparse_StringTranslatePseudoMapping___init___0.py:25: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b/test_thonny_roughparse_StringTranslatePseudoMapping___init___0.py::test_StringTranslatePseudoMapping_replace_whitespace
FAILED ../../../../../opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b/test_thonny_roughparse_StringTranslatePseudoMapping___init___0.py::test_StringTranslatePseudoMapping_replace_all
FAILED ../../../../../opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b/test_thonny_roughparse_StringTranslatePseudoMapping___init___0.py::test_StringTranslatePseudoMapping_replace_specific
============================== 3 failed in 0.08s ===============================
"""