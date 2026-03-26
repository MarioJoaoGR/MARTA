
import pytest
from isort.output import _with_star_comments
from isort import parse

@pytest.fixture
def parsed_content():
    return {
        'nested': {
            'module_name': {'*': 'special * comment'}
        }
    }

def test_with_star_comments(parsed_content):
    comments = ["original comment 1", "original comment 2"]
    result = _with_star_comments(parsed_content, "module_name", comments)
    assert result == ['original comment 1', 'original comment 2', 'special * comment']

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

isort/Test4DT_tests/test_isort_output__with_star_comments_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
___________________________ test_with_star_comments ____________________________

parsed_content = {'nested': {'module_name': {'*': 'special * comment'}}}

    def test_with_star_comments(parsed_content):
        comments = ["original comment 1", "original comment 2"]
>       result = _with_star_comments(parsed_content, "module_name", comments)

isort/Test4DT_tests/test_isort_output__with_star_comments_0_test_valid_input.py:16: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

parsed = {'nested': {'module_name': {'*': 'special * comment'}}}
module = 'module_name', comments = ['original comment 1', 'original comment 2']

    def _with_star_comments(parsed: parse.ParsedContent, module: str, comments: list[str]) -> list[str]:
>       star_comment = parsed.categorized_comments["nested"].get(module, {}).pop("*", None)
E       AttributeError: 'dict' object has no attribute 'categorized_comments'

isort/isort/output.py:683: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_output__with_star_comments_0_test_valid_input.py::test_with_star_comments
============================== 1 failed in 0.10s ===============================
"""