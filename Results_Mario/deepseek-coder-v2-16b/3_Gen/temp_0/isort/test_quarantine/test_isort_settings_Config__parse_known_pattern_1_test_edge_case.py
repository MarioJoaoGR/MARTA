
import pytest
from isort.settings import Config

@pytest.fixture
def config():
    return Config()

def test_parse_known_pattern(config):
    # Test edge case where pattern is a directory
    patterns = config._parse_known_pattern("some/directory/")
    assert isinstance(patterns, list)
    assert all(isinstance(p, str) for p in patterns)
    
    # Test normal case where pattern is not a directory
    patterns = config._parse_known_pattern("some.module")
    assert isinstance(patterns, list)
    assert len(patterns) == 1
    assert patterns[0] == "some.module"

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

isort/Test4DT_tests/test_isort_settings_Config__parse_known_pattern_1_test_edge_case.py F [100%]

=================================== FAILURES ===================================
___________________________ test_parse_known_pattern ___________________________

config = Config(py_version='py3', force_to_top=frozenset(), skip=frozenset({'_build', 'venv', 'node_modules', '.eggs', '.git', ...ge}', format_success='{success}: {message}', sort_order='natural', sort_reexports=False, split_on_trailing_comma=False)

    def test_parse_known_pattern(config):
        # Test edge case where pattern is a directory
>       patterns = config._parse_known_pattern("some/directory/")

isort/Test4DT_tests/test_isort_settings_Config__parse_known_pattern_1_test_edge_case.py:11: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = Config(py_version='py3', force_to_top=frozenset(), skip=frozenset({'_build', 'venv', 'node_modules', '.eggs', '.git', ...ge}', format_success='{success}: {message}', sort_order='natural', sort_reexports=False, split_on_trailing_comma=False)
pattern = 'some/directory/'

    def _parse_known_pattern(self, pattern: str) -> list[str]:
        """Expand pattern if identified as a directory and return found sub packages"""
        if pattern.endswith(os.path.sep):
            patterns = [
                filename
>               for filename in os.listdir(os.path.join(self.directory, pattern))
                if os.path.isdir(os.path.join(self.directory, pattern, filename))
            ]
E           FileNotFoundError: [Errno 2] No such file or directory: '/projects/F202407648IACDCF2/mario/some/directory/'

isort/isort/settings.py:719: FileNotFoundError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_settings_Config__parse_known_pattern_1_test_edge_case.py::test_parse_known_pattern
============================== 1 failed in 0.12s ===============================
"""