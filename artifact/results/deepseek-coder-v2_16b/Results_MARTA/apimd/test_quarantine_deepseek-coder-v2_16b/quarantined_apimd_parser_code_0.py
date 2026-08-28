
import pytest
from apimd.parser import code


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b/test_apimd_parser_code_0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_________________________ test_valid_input_hello_world _________________________

    def test_valid_input_hello_world():
        doc = "Hello | World"
        expected_output = "`Hello &#124; World`"
>       assert code(doc) == expected_output
E       AssertionError: assert '<code>Hello ... World</code>' == '`Hello &#124; World`'
E         
E         - `Hello &#124; World`
E         + <code>Hello &#124; World</code>

/opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b/test_apimd_parser_code_0.py:8: AssertionError
_____________________________ test_ampersand_input _____________________________

    def test_ampersand_input():
        doc = "This & That"
        expected_output = "<code>This &amp; That</code>"
>       assert code(doc) == expected_output
E       AssertionError: assert '<code>This & That</code>' == '<code>This &amp; That</code>'
E         
E         - <code>This &amp; That</code>
E         ?             ----
E         + <code>This & That</code>

/opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b/test_apimd_parser_code_0.py:13: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b/test_apimd_parser_code_0.py::test_valid_input_hello_world
FAILED ../../../../../opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b/test_apimd_parser_code_0.py::test_ampersand_input
============================== 2 failed in 0.06s ===============================
"""