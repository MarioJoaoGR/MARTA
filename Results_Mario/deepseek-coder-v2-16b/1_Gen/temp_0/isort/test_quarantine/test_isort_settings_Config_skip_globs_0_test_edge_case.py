
import pytest
from isort.settings import Config

@pytest.fixture
def config():
    return Config()

def test_skip_globs(config):
    # Test that skip_globs returns the union of skip_glob and extend_skip_glob as a frozenset
    assert isinstance(config.skip_globs(), frozenset)
    assert len(config.skip_globs()) == 0  # Initially, no globs should be set

    # Mocking some extend_skip_glob patterns
    config.extend_skip_glob = frozenset(["*.py", "!test_*.py"])

    result = config.skip_globs()
    assert isinstance(result, frozenset)
    assert len(result) == 2  # Now there should be two globs in the set
    assert "*.py" in result
    assert "!test_*.py" in result

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

isort/Test4DT_tests/test_isort_settings_Config_skip_globs_0_test_edge_case.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_skip_globs ________________________________

config = Config(py_version='py3', force_to_top=frozenset(), skip=frozenset({'.mypy_cache', 'build', '.direnv', 'buck-out', 'nod...ge}', format_success='{success}: {message}', sort_order='natural', sort_reexports=False, split_on_trailing_comma=False)

    def test_skip_globs(config):
        # Test that skip_globs returns the union of skip_glob and extend_skip_glob as a frozenset
>       assert isinstance(config.skip_globs(), frozenset)
E       TypeError: 'frozenset' object is not callable

isort/Test4DT_tests/test_isort_settings_Config_skip_globs_0_test_edge_case.py:11: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_settings_Config_skip_globs_0_test_edge_case.py::test_skip_globs
============================== 1 failed in 0.10s ===============================
"""