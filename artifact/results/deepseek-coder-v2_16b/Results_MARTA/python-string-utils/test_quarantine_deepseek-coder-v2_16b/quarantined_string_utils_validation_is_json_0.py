
import pytest
from string_utils.validation import is_json
import json

def is_full_string(input_string: str) -> bool:
    return isinstance(input_string, str) and len(input_string.strip()) > 0

# Define the regular expression for JSON wrapper check
JSON_WRAPPER_RE = re.compile(r'^\s*\{.*\}\s*$|^\s*\[\s*.*\s*\]\s*$')

@pytest.mark.parametrize("input_string, expected", [
    ('{"name": "Peter"}', True),
    ('[1, 2, 3]', True),
    ('{nope}', False),
    ('invalid json', False),
    (None, False)
])
def test_is_json(input_string, expected):
    if input_string is None:
        with pytest.raises(TypeError):
            is_json(input_string)
    elif not isinstance(input_string, str):
        assert not is_json(input_string)
    else:
        result = is_json(input_string) if is_full_string(input_string) and JSON_WRAPPER_RE.match(input_string) is not None else False
        assert result == expected

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
__________ ERROR collecting test_string_utils_validation_is_json_0.py __________
/opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_deepseek-coder-v2_16b/test_string_utils_validation_is_json_0.py:10: in <module>
    JSON_WRAPPER_RE = re.compile(r'^\s*\{.*\}\s*$|^\s*\[\s*.*\s*\]\s*$')
E   NameError: name 're' is not defined
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_deepseek-coder-v2_16b/test_string_utils_validation_is_json_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.13s ===============================
"""