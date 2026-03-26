
import pytest
from isort.place import Config, _forced_separate

def test_invalid_input():
    config = Config()
    config.forced_separate = ["*.log", "backup.*"]
    
    # Test with a valid name that matches the pattern
    result = _forced_separate("example.log", config)
    assert result == ('*.log', 'Matched forced_separate (*).log config value.')
    
    # Test with an invalid name that does not match any pattern
    result = _forced_separate("example", config)
    assert result is None

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

isort/Test4DT_tests/test_isort_place__forced_separate_0_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        config = Config()
>       config.forced_separate = ["*.log", "backup.*"]

isort/Test4DT_tests/test_isort_place__forced_separate_0_test_invalid_input.py:7: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = Config(py_version='py3', force_to_top=frozenset(), skip=frozenset({'.svn', '.nox', 'dist', '.hg', '__pypackages__', '....ge}', format_success='{success}: {message}', sort_order='natural', sort_reexports=False, split_on_trailing_comma=False)
name = 'forced_separate', value = ['*.log', 'backup.*']

>   ???
E   dataclasses.FrozenInstanceError: cannot assign to field 'forced_separate'

<string>:4: FrozenInstanceError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_place__forced_separate_0_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.11s ===============================
"""