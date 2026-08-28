
import pytest
from ansible.executor.interpreter_discovery import _version_fuzzy_match
from ansible.module_utils.compat.version import LooseVersion
import bisect



def test_exact_match():
    version_map = {'1.0': 'metadata1', '2.0': 'metadata2', '3.0': 'metadata3'}
    result = _version_fuzzy_match('2.0', version_map)
    assert result == 'metadata2', f"Expected metadata2 for exact match but got {result}"

def test_no_exact_match():
    version_map = {'1.0': 'metadata1', '2.0': 'metadata2', '3.0': 'metadata3'}
    result = _version_fuzzy_match('2.5', version_map)
    assert result == 'metadata2', f"Expected metadata2 for nearest previous newer but got {result}"

def test_older_than_all():
    version_map = {'1.0': 'metadata1', '2.0': 'metadata2', '3.0': 'metadata3'}
    result = _version_fuzzy_match('4.0', version_map)
    assert result == 'metadata3', f"Expected metadata3 for older than all but got {result}"