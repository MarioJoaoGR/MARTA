
import pytest
from unittest.mock import patch

def is_quoted(data):
    return len(data) > 0 and (data[0] == '"' and data[-1] == '"' or data[0] == "'" and data[-1] == "'")

@pytest.mark.parametrize("input_string, expected", [
    ("Hello, World!", True),
    ('Hello, World!', True),
    ("", False),
    ('', False)
])
def test_is_quoted(input_string, expected):
    assert is_quoted(input_string) == expected
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 4 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_splitter_is_quoted_0.py F [ 25%]
F..                                                                      [100%]

=================================== FAILURES ===================================
_____________________ test_is_quoted[Hello, World!-True0] ______________________

input_string = 'Hello, World!', expected = True

    @pytest.mark.parametrize("input_string, expected", [
        ("Hello, World!", True),
        ('Hello, World!', True),
        ("", False),
        ('', False)
    ])
    def test_is_quoted(input_string, expected):
>       assert is_quoted(input_string) == expected
E       AssertionError: assert False == True
E        +  where False = is_quoted('Hello, World!')

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_splitter_is_quoted_0.py:15: AssertionError
_____________________ test_is_quoted[Hello, World!-True1] ______________________

input_string = 'Hello, World!', expected = True

    @pytest.mark.parametrize("input_string, expected", [
        ("Hello, World!", True),
        ('Hello, World!', True),
        ("", False),
        ('', False)
    ])
    def test_is_quoted(input_string, expected):
>       assert is_quoted(input_string) == expected
E       AssertionError: assert False == True
E        +  where False = is_quoted('Hello, World!')

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_splitter_is_quoted_0.py:15: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_splitter_is_quoted_0.py::test_is_quoted[Hello, World!-True0]
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_splitter_is_quoted_0.py::test_is_quoted[Hello, World!-True1]
========================= 2 failed, 2 passed in 0.23s ==========================
"""