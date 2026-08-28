
import pytest
from ansible.executor.interpreter_discovery import _version_fuzzy_match
from ansible.module_utils.compat.version import LooseVersion
import bisect



def test_exact_match():
    version_map = {'1.0': 'metadata1', '2.0': 'metadata2', '3.0': 'metadata3'}
    assert _version_fuzzy_match('2.0', version_map) == 'metadata2'

def test_no_exact_match():
    version_map = {'1.0': 'metadata1', '2.0': 'metadata2', '3.0': 'metadata3'}
    assert _version_fuzzy_match('2.5', version_map) == 'metadata2'

def test_no_exact_match_older_than_all():
    version_map = {'1.0': 'metadata1', '2.0': 'metadata2', '3.0': 'metadata3'}
    assert _version_fuzzy_match('4.0', version_map) == 'metadata3'