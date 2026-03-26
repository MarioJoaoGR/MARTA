
import pytest
from isort.place import Config, _known_pattern

@pytest.fixture
def config():
    config = Config()
    config.known_patterns = [("os.path", "placement1"), ("sys.modules", "placement2")]
    return config

def test__known_pattern_basic(config):
    result = _known_pattern("os.path", config)
    assert result == ('placement1', 'Matched configured known pattern os.path')

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

isort/Test4DT_tests/test_isort_place__known_pattern_0_test__known_pattern_basic.py E [100%]

==================================== ERRORS ====================================
_________________ ERROR at setup of test__known_pattern_basic __________________

    @pytest.fixture
    def config():
        config = Config()
>       config.known_patterns = [("os.path", "placement1"), ("sys.modules", "placement2")]

isort/Test4DT_tests/test_isort_place__known_pattern_0_test__known_pattern_basic.py:8: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = Config(py_version='py3', force_to_top=frozenset(), skip=frozenset({'.direnv', '.hg', '.tox', 'node_modules', '.svn', '...ge}', format_success='{success}: {message}', sort_order='natural', sort_reexports=False, split_on_trailing_comma=False)
name = 'known_patterns'
value = [('os.path', 'placement1'), ('sys.modules', 'placement2')]

>   ???
E   AttributeError: property 'known_patterns' of 'Config' object has no setter

<string>:5: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR isort/Test4DT_tests/test_isort_place__known_pattern_0_test__known_pattern_basic.py::test__known_pattern_basic
=============================== 1 error in 0.10s ===============================
"""