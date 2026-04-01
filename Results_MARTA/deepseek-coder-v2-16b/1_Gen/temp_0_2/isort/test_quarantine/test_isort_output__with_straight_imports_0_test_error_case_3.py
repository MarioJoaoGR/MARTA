
from isort.output import _with_straight_imports
from unittest.mock import MagicMock
import pytest

@pytest.fixture
def mock_parsed():
    parsed = MagicMock()
    # Mock the categorized comments for straight imports
    parsed.categorized_comments = {
        "above": {"straight": {"os": ["comment1", "comment2"], "sys": ["inline_comment1", "inline_comment2"]}},
        "straight": {"os": ["# comment1", "# comment2"], "sys": ["# inline_comment1", "# inline_comment2"]}
    }
    parsed.as_map = {"straight": {"os": [], "sys": []}}
    parsed.imports = {
        "body": {"straight": {"os": True, "sys": True}}
    }
    return parsed

@pytest.fixture
def mock_config():
    config = MagicMock()
    config.combine_straight_imports = True
    config.ignore_comments = False
    config.comment_prefix = "#"
    return config

def test_with_straight_imports_combined(mock_parsed, mock_config):
    result = _with_straight_imports(
        mock_parsed,
        mock_config,
        ["os", "sys"],
        "body",
        [],
        "from"
    )
    assert result == [
        'from os import name as os_alias; from sys import path as sys_alias  # comment1',
        'from os import name as os_alias; from sys import path as sys_alias  # comment2',
        'from os import name as os_alias; from sys import path as sys_alias  # inline_comment1',
        'from os import name as os_alias; from sys import path as sys_alias  # inline_comment2'
    ]

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

isort/Test4DT_tests/test_isort_output__with_straight_imports_0_test_error_case_3.py F [100%]

=================================== FAILURES ===================================
_____________________ test_with_straight_imports_combined ______________________

mock_parsed = <MagicMock id='140565857698704'>
mock_config = <MagicMock id='140565839300368'>

    def test_with_straight_imports_combined(mock_parsed, mock_config):
        result = _with_straight_imports(
            mock_parsed,
            mock_config,
            ["os", "sys"],
            "body",
            [],
            "from"
        )
>       assert result == [
            'from os import name as os_alias; from sys import path as sys_alias  # comment1',
            'from os import name as os_alias; from sys import path as sys_alias  # comment2',
            'from os import name as os_alias; from sys import path as sys_alias  # inline_comment1',
            'from os import name as os_alias; from sys import path as sys_alias  # inline_comment2'
        ]
E       AssertionError: assert ['comment1', ...ine_comment2'] == ['from os imp...ine_comment2']
E         
E         At index 0 diff: 'comment1' != 'from os import name as os_alias; from sys import path as sys_alias  # comment1'
E         Left contains 2 more items, first extra item: 'inline_comment2'
E         Use -v to get more diff

isort/Test4DT_tests/test_isort_output__with_straight_imports_0_test_error_case_3.py:37: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_output__with_straight_imports_0_test_error_case_3.py::test_with_straight_imports_combined
============================== 1 failed in 0.12s ===============================
"""