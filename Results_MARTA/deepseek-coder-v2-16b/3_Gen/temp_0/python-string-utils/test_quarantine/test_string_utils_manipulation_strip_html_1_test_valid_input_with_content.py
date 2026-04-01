
import re
import pytest
from string_utils.manipulation import strip_html, InvalidInputError

def test_valid_input_with_content():
    assert strip_html('test: <a href="foo/bar">click here</a>') == 'test: click here'
    assert strip_html('test: <a href="foo/bar">click here</a>', keep_tag_content=True) == 'test: click here'
    with pytest.raises(InvalidInputError):
        strip_html(12345)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

python-string-utils/Test4DT_tests/test_string_utils_manipulation_strip_html_1_test_valid_input_with_content.py F [100%]

=================================== FAILURES ===================================
________________________ test_valid_input_with_content _________________________

    def test_valid_input_with_content():
>       assert strip_html('test: <a href="foo/bar">click here</a>') == 'test: click here'
E       AssertionError: assert 'test: ' == 'test: click here'
E         
E         - test: click here
E         + test:

python-string-utils/Test4DT_tests/test_string_utils_manipulation_strip_html_1_test_valid_input_with_content.py:7: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_manipulation_strip_html_1_test_valid_input_with_content.py::test_valid_input_with_content
============================== 1 failed in 0.02s ===============================
"""