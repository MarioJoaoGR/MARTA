
from isort.deprecated.finders import KnownPatternFinder
from unittest.mock import MagicMock
import re

def test_valid_input():
    config = MagicMock()
    config.sections = ["section1", "section2"]
    config.known_other = {
        "section1": ["pattern1"],
        "section2": ["pattern2"]
    }
    KNOWN_SECTION_MAPPING = {"section1": "Section1", "section2": "Section2"}

    finder = KnownPatternFinder(config)

    assert len(finder.known_patterns) == 4

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

isort/Test4DT_tests/test_isort_deprecated_finders_KnownPatternFinder___init___1_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        config = MagicMock()
        config.sections = ["section1", "section2"]
        config.known_other = {
            "section1": ["pattern1"],
            "section2": ["pattern2"]
        }
        KNOWN_SECTION_MAPPING = {"section1": "Section1", "section2": "Section2"}
    
        finder = KnownPatternFinder(config)
    
>       assert len(finder.known_patterns) == 4
E       assert 0 == 4
E        +  where 0 = len([])
E        +    where [] = <isort.deprecated.finders.KnownPatternFinder object at 0x7f131bc48690>.known_patterns

isort/Test4DT_tests/test_isort_deprecated_finders_KnownPatternFinder___init___1_test_valid_input.py:17: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_deprecated_finders_KnownPatternFinder___init___1_test_valid_input.py::test_valid_input
============================== 1 failed in 0.16s ===============================
"""