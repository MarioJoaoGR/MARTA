
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
collected 4 items

../../../../../opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b/test_thonny_roughparse_StringTranslatePseudoMapping___iter___0.py F [ 25%]
FFF                                                                      [100%]

=================================== FAILURES ===================================
_____________________ test_string_translate_pseudo_mapping _____________________

    def test_string_translate_pseudo_mapping():
        non_defaults = {'a': 'z', 'b': 'y'}
        mapping = StringTranslatePseudoMapping(non_defaults, ord('*'))
    
        text = "ab"
        translated_text = text.translate(mapping)
>       assert translated_text == '*y'
E       AssertionError: assert '**' == '*y'
E         
E         - *y
E         + **

/opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b/test_thonny_roughparse_StringTranslatePseudoMapping___iter___0.py:11: AssertionError
_______________ test_string_translate_pseudo_mapping_with_lambda _______________

    def test_string_translate_pseudo_mapping_with_lambda():
        non_defaults = {'a': 'z', 'b': 'y'}
        mapping = StringTranslatePseudoMapping(non_defaults, lambda x: ord('*'))
    
        text = "ab"
>       translated_text = text.translate(mapping)
E       TypeError: character mapping must return integer, None or str

/opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b/test_thonny_roughparse_StringTranslatePseudoMapping___iter___0.py:18: TypeError
______________ test_string_translate_pseudo_mapping_with_unicode _______________

    def test_string_translate_pseudo_mapping_with_unicode():
        non_defaults = {ord('a'): ord('z'), ord('b'): ord('y')}
        mapping = StringTranslatePseudoMapping(non_defaults, ord('*'))
    
        text = "ab"
        translated_text = text.translate(mapping)
>       assert translated_text == '*y'
E       AssertionError: assert 'zy' == '*y'
E         
E         - *y
E         + zy

/opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b/test_thonny_roughparse_StringTranslatePseudoMapping___iter___0.py:27: AssertionError
__________________ test_string_translate_pseudo_mapping_iter ___________________

    def test_string_translate_pseudo_mapping_iter():
        non_defaults = {'a': 'z', 'b': 'y'}
        mapping = StringTranslatePseudoMapping(non_defaults, ord('*'))
    
        iterator = iter(mapping)
>       assert next(iterator) == ('a', 'z')
E       AssertionError: assert 'a' == ('a', 'z')
E        +  where 'a' = next(<dict_keyiterator object at 0x7f4bea5b81d0>)

/opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b/test_thonny_roughparse_StringTranslatePseudoMapping___iter___0.py:34: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b/test_thonny_roughparse_StringTranslatePseudoMapping___iter___0.py::test_string_translate_pseudo_mapping
FAILED ../../../../../opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b/test_thonny_roughparse_StringTranslatePseudoMapping___iter___0.py::test_string_translate_pseudo_mapping_with_lambda
FAILED ../../../../../opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b/test_thonny_roughparse_StringTranslatePseudoMapping___iter___0.py::test_string_translate_pseudo_mapping_with_unicode
FAILED ../../../../../opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b/test_thonny_roughparse_StringTranslatePseudoMapping___iter___0.py::test_string_translate_pseudo_mapping_iter
============================== 4 failed in 0.10s ===============================
"""