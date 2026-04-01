
import pytest
from pathlib import Path
from isort.place import Config, DEFAULT_CONFIG, module as module_with_reason

def test_valid_input_happy_path():
    config = Config(forced_separate=['*.log', 'data.*'], known_patterns=[("^abc.*", "section1"), ("^def.*", "section2")], src_paths=[Path("C:\\PythonProjects\\myproject")])
    
    assert module_with_reason("example.log", config)[0] == '*.log'
    assert module_with_reason(".hidden_module", config)[0] == 'LOCAL'
    assert module_with_reason("abc.xyz", config)[0] == 'section1'
    assert module_with_reason("mypackage.modulename", config)[0] == 'sections.FIRSTPARTY'

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

isort/Test4DT_tests/test_isort_place_module_0_test_valid_input_happy_path.py F [100%]

=================================== FAILURES ===================================
_________________________ test_valid_input_happy_path __________________________

    def test_valid_input_happy_path():
        config = Config(forced_separate=['*.log', 'data.*'], known_patterns=[("^abc.*", "section1"), ("^def.*", "section2")], src_paths=[Path("C:\\PythonProjects\\myproject")])
    
>       assert module_with_reason("example.log", config)[0] == '*.log'
E       AssertionError: assert '*' == '*.log'
E         
E         - *.log
E         + *

isort/Test4DT_tests/test_isort_place_module_0_test_valid_input_happy_path.py:9: AssertionError
=============================== warnings summary ===============================
Test4DT_tests/test_isort_place_module_0_test_valid_input_happy_path.py::test_valid_input_happy_path
  /projects/F202407648IACDCF2/mario/isort/Test4DT_tests/test_isort_place_module_0_test_valid_input_happy_path.py:7: UserWarning: `known_patterns` setting is defined, but PATTERNS is not included in `sections` config option: ('FUTURE', 'STDLIB', 'THIRDPARTY', 'FIRSTPARTY', 'LOCALFOLDER').
  
  See: https://pycqa.github.io/isort/#custom-sections-and-ordering.
    config = Config(forced_separate=['*.log', 'data.*'], known_patterns=[("^abc.*", "section1"), ("^def.*", "section2")], src_paths=[Path("C:\\PythonProjects\\myproject")])

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_place_module_0_test_valid_input_happy_path.py::test_valid_input_happy_path
========================= 1 failed, 1 warning in 0.09s =========================
"""