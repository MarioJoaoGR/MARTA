
import pytest
from apimd.parser import doctest


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b/test_apimd_parser_doctest_1.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        doc = "line1\n>>> line2\nline3"
        expected = "line1\n```python\nline2\n```\nline3"
>       assert doctest(doc) == expected
E       AssertionError: assert 'line1\n```py...2\n```\nline3' == 'line1\n```py...2\n```\nline3'
E         
E           line1
E           ```python
E         - line2
E         + >>> line2
E         ? ++++
E           ```
E           line3

/opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b/test_apimd_parser_doctest_1.py:8: AssertionError
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        with pytest.raises(TypeError):
>           doctest(None)

/opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b/test_apimd_parser_doctest_1.py:12: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

doc = None

    def doctest(doc: str) -> str:
        """Wrap doctest as markdown Python code."""
        keep = False
        docs = []
>       lines = doc.splitlines()
E       AttributeError: 'NoneType' object has no attribute 'splitlines'

/opt/marta/baselines/codamosa/replication/test-apps/apimd/apimd/parser.py:113: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b/test_apimd_parser_doctest_1.py::test_valid_input
FAILED ../../../../../opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b/test_apimd_parser_doctest_1.py::test_invalid_input
============================== 2 failed in 0.07s ===============================
"""