
import pytest
from ansible.executor.interpreter_discovery import LooseVersion
import bisect

def _version_fuzzy_match(version, version_map):
    if not version or not version_map:
        raise ValueError('Invalid version or version map')
    
    # try exact match first
    res = version_map.get(version)
    if res:
        return res

    sorted_looseversions = sorted([LooseVersion(v) for v in version_map.keys()])

    find_looseversion = LooseVersion(version)

    # slot match; return nearest previous version we're newer than
    kpos = bisect.bisect(sorted_looseversions, find_looseversion)

    if kpos == 0:
        # older than everything in the list, return the oldest version
        # TODO: warning-worthy?
        return version_map.get(sorted_looseversions[0].vstring)

    # TODO: is "past the end of the list" warning-worthy too (at least if it's not a major version match)?

    # return the next-oldest entry that we're newer than...
    return version_map.get(sorted_looseversions[kpos - 1].vstring)

# Test cases
def test_valid_case_exact_match():
    version_map = {'1.0': 'metadata1', '2.0': 'metadata2', '3.0': 'metadata3'}
    result = _version_fuzzy_match('1.0', version_map)
    assert result == 'metadata1'

def test_valid_case_fuzzy_match():
    version_map = {'1.0': 'metadata1', '2.0': 'metadata2', '3.0': 'metadata3'}
    result = _version_fuzzy_match('2.5', version_map)
    assert result == 'metadata2'

def test_valid_case_no_exact_match():
    version_map = {'1.0': 'metadata1', '2.0': 'metadata2', '3.0': 'metadata3'}
    result = _version_fuzzy_match('4.0', version_map)
    assert result == 'metadata3'

def test_error_case_invalid_input():
    with pytest.raises(ValueError) as e:
        _version_fuzzy_match(None, None)
    assert str(e.value) == 'Invalid version or version map'

def test_error_case_empty_input():
    with pytest.raises(ValueError) as e:
        _version_fuzzy_match('', {})
    assert str(e.value) == 'Invalid version or version map'
