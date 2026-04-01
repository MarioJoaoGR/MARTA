
import os
from isort.settings import Config
import pytest

@pytest.fixture
def config_instance():
    return Config(py_version='py3', force_to_top=frozenset(), skip=frozenset({'.pants.d', '.direnv', '.hg', '.svn', '.git', '.myp...ge}', format_success='{success}: {message}', sort_order='natural', sort_reexports=False, split_on_trailing_comma=False)

def test_parse_known_pattern(config_instance):
    assert config_instance._parse_known_pattern("some/directory") == ["some/directory"]
    assert config_instance._parse_known_pattern("some/directory/") == []  # Empty list for directories without files

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_settings_Config__parse_known_pattern_1_test_edge_cases
isort/Test4DT_tests/test_isort_settings_Config__parse_known_pattern_1_test_edge_cases.py:8:251: E0001: Parsing failed: 'closing parenthesis ')' does not match opening parenthesis '{' (Test4DT_tests.test_isort_settings_Config__parse_known_pattern_1_test_edge_cases, line 8)' (syntax-error)


"""