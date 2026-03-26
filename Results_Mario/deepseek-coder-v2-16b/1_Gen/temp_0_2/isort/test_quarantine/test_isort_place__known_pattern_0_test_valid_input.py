
import pytest
from isort.place import _known_pattern
from unittest.mock import MagicMock

class Config:
    def __init__(self):
        self.known_patterns = [("^abc.*", "section1"), ("^def.*", "section2")]
        self.sections = ["section1", "section2"]

@pytest.fixture
def config():
    return Config()

def test_valid_input(config):
    result = _known_pattern("abc.xyz", config)
    assert result == ('section1', 'Matched configured known pattern ^abc.*')

    result = _known_pattern("ghi.jkl", config)
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

isort/Test4DT_tests/test_isort_place__known_pattern_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

config = <Test4DT_tests.test_isort_place__known_pattern_0_test_valid_input.Config object at 0x7f660424bdd0>

    def test_valid_input(config):
>       result = _known_pattern("abc.xyz", config)

isort/Test4DT_tests/test_isort_place__known_pattern_0_test_valid_input.py:16: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

name = 'abc.xyz'
config = <Test4DT_tests.test_isort_place__known_pattern_0_test_valid_input.Config object at 0x7f660424bdd0>

    def _known_pattern(name: str, config: Config) -> tuple[str, str] | None:
        parts = name.split(".")
        module_names_to_check = (".".join(parts[:first_k]) for first_k in range(len(parts), 0, -1))
        for module_name_to_check in module_names_to_check:
            for pattern, placement in config.known_patterns:
>               if placement in config.sections and pattern.match(module_name_to_check):
E               AttributeError: 'str' object has no attribute 'match'

isort/isort/place.py:58: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_place__known_pattern_0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.10s ===============================
"""