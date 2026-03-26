
import pytest
from isort.wrap_modes import noqa

def test_invalid_input():
    # Invalid 'imports' type (should be list of str)
    with pytest.raises(TypeError):
        noqa(**{'imports': 123, 'statement': 'print(math.sqrt(9))', 'comments': ['# This is a comment'], 'comment_prefix': '#', 'line_length': 50})
    
    # Invalid 'statement' type (should be str)
    with pytest.raises(TypeError):
        noqa(**{'imports': ['math'], 'statement': 123, 'comments': ['# This is a comment'], 'comment_prefix': '#', 'line_length': 50})

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

isort/Test4DT_tests/test_isort_wrap_modes_noqa_0_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        # Invalid 'imports' type (should be list of str)
        with pytest.raises(TypeError):
            noqa(**{'imports': 123, 'statement': 'print(math.sqrt(9))', 'comments': ['# This is a comment'], 'comment_prefix': '#', 'line_length': 50})
    
        # Invalid 'statement' type (should be str)
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

isort/Test4DT_tests/test_isort_wrap_modes_noqa_0_test_invalid_input.py:11: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_wrap_modes_noqa_0_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.11s ===============================
"""