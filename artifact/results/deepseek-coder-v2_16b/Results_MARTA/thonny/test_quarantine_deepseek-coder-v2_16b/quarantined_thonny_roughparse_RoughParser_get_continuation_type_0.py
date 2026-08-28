
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

../../../../../opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b/test_thonny_roughparse_RoughParser_get_continuation_type_0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        parser = RoughParser(indent_width=4, tabwidth=4)
        parser.set_str("def example():\n\tprint('Hello, World!')\n")
        expected_tran1 = {ord('{'): ord('('), ord('['): ord('('), ord('}'): ord(')'), ord(']'): ord(')'), ord('"'): ord('"'), ord("'"): ord("'"), ord('\\'): ord('\\'), ord('\n'): ord('\n'), ord('#'): ord('#')}
>       assert parser._tran1 == expected_tran1
E       assert {10: 10, 34: ..., 39: 39, ...} == {10: 10, 34: ..., 39: 39, ...}
E         
E         Omitting 9 identical items, use -vv to show
E         Left contains 2 more items:
E         {40: 40, 41: 41}
E         Use -v to get more diff

/opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b/test_thonny_roughparse_RoughParser_get_continuation_type_0.py:9: AssertionError
________________________________ test_edge_case ________________________________

    def test_edge_case():
        parser = RoughParser(indent_width=4, tabwidth=4)
        parser.set_str("")
        expected_tran1 = {ord('{'): ord('('), ord('['): ord('('), ord('}'): ord(')'), ord(']'): ord(')'), ord('"'): ord('"'), ord("'"): ord("'"), ord('\\'): ord('\\'), ord('\n'): ord('\n'), ord('#'): ord('#')}
>       assert parser._tran1 == expected_tran1
E       assert {10: 10, 34: ..., 39: 39, ...} == {10: 10, 34: ..., 39: 39, ...}
E         
E         Omitting 9 identical items, use -vv to show
E         Left contains 2 more items:
E         {40: 40, 41: 41}
E         Use -v to get more diff

/opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b/test_thonny_roughparse_RoughParser_get_continuation_type_0.py:15: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b/test_thonny_roughparse_RoughParser_get_continuation_type_0.py::test_valid_input
FAILED ../../../../../opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b/test_thonny_roughparse_RoughParser_get_continuation_type_0.py::test_edge_case
============================== 2 failed in 0.05s ===============================
"""