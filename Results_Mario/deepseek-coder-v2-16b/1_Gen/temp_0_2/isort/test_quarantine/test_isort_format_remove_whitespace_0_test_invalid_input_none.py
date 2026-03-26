
import pytest
from isort.format import remove_whitespace

def test_invalid_input_none():
    with pytest.raises(TypeError):
        remove_whitespace(None)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

isort/Test4DT_tests/test_isort_format_remove_whitespace_0_test_invalid_input_none.py F [100%]

=================================== FAILURES ===================================
___________________________ test_invalid_input_none ____________________________

    def test_invalid_input_none():
        with pytest.raises(TypeError):
>           remove_whitespace(None)

isort/Test4DT_tests/test_isort_format_remove_whitespace_0_test_invalid_input_none.py:7: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

content = None, line_separator = '\n'

    def remove_whitespace(content: str, line_separator: str = "\n") -> str:
>       content = content.replace(line_separator, "").replace(" ", "").replace("\x0c", "")
E       AttributeError: 'NoneType' object has no attribute 'replace'

isort/isort/format.py:89: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_format_remove_whitespace_0_test_invalid_input_none.py::test_invalid_input_none
============================== 1 failed in 0.11s ===============================
"""