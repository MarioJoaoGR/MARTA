
import pytest
from isort.deprecated.finders import KnownPatternFinder
from unittest.mock import MagicMock

@pytest.fixture(autouse=True)
def mock_config():
    config = MagicMock()
    config.sections = ["section1", "section2"]
    config.directory = "/test/directory"
    config.known_other = {
        "section1": ["pattern1*"],
        "section2": ["pattern2*"]
    }
    return config

def test_invalid_input(mock_config):
    finder = KnownPatternFinder(mock_config)
    assert len(finder.known_patterns) == 4  # Assuming two sections with two patterns each expand to four total patterns

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

isort/Test4DT_tests/test_isort_deprecated_finders_KnownPatternFinder__parse_known_pattern_0_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

mock_config = <MagicMock id='140117550509328'>

    def test_invalid_input(mock_config):
        finder = KnownPatternFinder(mock_config)
>       assert len(finder.known_patterns) == 4  # Assuming two sections with two patterns each expand to four total patterns
E       assert 0 == 4
E        +  where 0 = len([])
E        +    where [] = <isort.deprecated.finders.KnownPatternFinder object at 0x7f6fa9286a10>.known_patterns

isort/Test4DT_tests/test_isort_deprecated_finders_KnownPatternFinder__parse_known_pattern_0_test_invalid_input.py:19: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_deprecated_finders_KnownPatternFinder__parse_known_pattern_0_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.12s ===============================
"""