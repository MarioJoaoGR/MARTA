
import pytest
from string_utils.validation import is_url

def is_full_string(input_string: str) -> bool:
    return isinstance(input_string, str) and len(input_string.strip()) > 0

URL_RE = re.compile(r'^https?://[^\s/$.?#].[^\s]*$', re.IGNORECASE)

@pytest.mark.parametrize("test_input, expected", [
    ('http://www.mysite.com', True),
    ('https://mysite.com', True),
    ('.mysite.com', False),
    ('', False),
    (None, False)
])
def test_is_url(test_input, expected):
    assert is_url(test_input) == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 0 items / 1 error

==================================== ERRORS ====================================
__________ ERROR collecting test_string_utils_validation_is_url_0.py ___________
/opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_deepseek-coder-v2_16b/test_string_utils_validation_is_url_0.py:8: in <module>
    URL_RE = re.compile(r'^https?://[^\s/$.?#].[^\s]*$', re.IGNORECASE)
E   NameError: name 're' is not defined
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_deepseek-coder-v2_16b/test_string_utils_validation_is_url_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.13s ===============================
"""