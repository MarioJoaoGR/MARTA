
from isort.parse import ParsedContent, DEFAULT_CONFIG  # noqa: E0401, E0611
from isort.config import Config  # noqa: E0401, E0611
import pytest  # noqa: E0401

@pytest.mark.parametrize("contents", [
    "import os\nfrom math import sqrt"
])
def test_missing_lines_critical(contents):
    from isort.parse import file_contents  # noqa: F811, E0401
    
    config = Config()
    parsed = file_contents(contents, config=config)
    
    assert isinstance(parsed, ParsedContent)
    assert len(parsed.lines_without_imports) == 2

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_parse_file_contents_2_test_missing_lines_critical
isort/Test4DT_tests/test_isort_parse_file_contents_2_test_missing_lines_critical.py:3:0: E0401: Unable to import 'isort.config' (import-error)
isort/Test4DT_tests/test_isort_parse_file_contents_2_test_missing_lines_critical.py:3:0: E0611: No name 'config' in module 'isort' (no-name-in-module)


"""