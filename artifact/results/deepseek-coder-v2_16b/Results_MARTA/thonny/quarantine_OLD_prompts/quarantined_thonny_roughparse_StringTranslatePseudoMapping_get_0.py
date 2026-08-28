
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

../../../../../opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b/test_thonny_roughparse_StringTranslatePseudoMapping_get_0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
________________________________ test_edge_case ________________________________

    def test_edge_case():
        non_default_dict = {}
        mapping = StringTranslatePseudoMapping(non_default_dict, ord('x'))
        text = "Hello, World!"
        translated_text = text.translate(mapping)
>       assert translated_text == 'xxxxxxxxxxxxxxx'
E       AssertionError: assert 'xxxxxxxxxxxxx' == 'xxxxxxxxxxxxxxx'
E         
E         - xxxxxxxxxxxxxxx
E         ?              --
E         + xxxxxxxxxxxxx

/opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b/test_thonny_roughparse_StringTranslatePseudoMapping_get_0.py:10: AssertionError
_______________________________ test_error_case ________________________________

    def test_error_case():
        non_default_dict = {'a': 'b'}
        mapping = StringTranslatePseudoMapping(non_default_dict, ord('x'))
        text = "Hello, World!"
        translated_text = text.translate(mapping)
>       assert translated_text == 'xxxxxxxxxxxxxxx'
E       AssertionError: assert 'xxxxxxxxxxxxx' == 'xxxxxxxxxxxxxxx'
E         
E         - xxxxxxxxxxxxxxx
E         ?              --
E         + xxxxxxxxxxxxx

/opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b/test_thonny_roughparse_StringTranslatePseudoMapping_get_0.py:17: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b/test_thonny_roughparse_StringTranslatePseudoMapping_get_0.py::test_edge_case
FAILED ../../../../../opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b/test_thonny_roughparse_StringTranslatePseudoMapping_get_0.py::test_error_case
============================== 2 failed in 0.05s ===============================
"""