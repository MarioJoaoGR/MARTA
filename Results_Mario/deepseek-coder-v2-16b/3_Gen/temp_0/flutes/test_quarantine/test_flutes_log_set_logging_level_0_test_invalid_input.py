
import pytest
from flutes.log import LEVEL_MAP, _CONSOLE_LOGGING_LEVEL, LOGGER
from typing import Any, Callable, Mapping

# Mocking the required objects and functions
class MockLevelMap(Mapping[str, int]):
    def __getitem__(self, key: str) -> int:
        return 0  # Default to no valid level
    
    def __iter__(self):
        yield from ()
    
    def __len__(self):
        return 0

LEVEL_MAP = MockLevelMap()
_CONSOLE_LOGGING_LEVEL.value = None
LOGGER.setLevel = lambda level: None

def set_logging_level(level: str, console: bool = True, file: bool = True) -> None:
    if level not in LEVEL_MAP:
        raise ValueError(f"Incorrect logging level '{level}'")
    if console:
        _CONSOLE_LOGGING_LEVEL.value = LEVEL_MAP[level]
    if file:
        LOGGER.setLevel(LEVEL_MAP[level])

def test_invalid_input():
    with pytest.raises(ValueError):
        set_logging_level('INVALID_LEVEL')

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 0 items / 1 error

==================================== ERRORS ====================================
_ ERROR collecting Test4DT_tests/test_flutes_log_set_logging_level_0_test_invalid_input.py _
flutes/Test4DT_tests/test_flutes_log_set_logging_level_0_test_invalid_input.py:18: in <module>
    _CONSOLE_LOGGING_LEVEL.value = None
E   TypeError: 'NoneType' object cannot be interpreted as an integer
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR flutes/Test4DT_tests/test_flutes_log_set_logging_level_0_test_invalid_input.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.14s ===============================

"""