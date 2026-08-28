
import pytest
from unittest.mock import patch
from ansible.executor.interpreter_discovery import LooseVersion
import bisect

def _version_fuzzy_match(version, version_map):
    """
    Matches a given software version to the nearest available version in a provided version map.
    
    The function first attempts an exact match with the versions in `version_map`. If no exact match is found, it performs a fuzzy matching by comparing the given version with sorted LooseVersion objects of the keys in `version_map`. It returns the closest previous version that is newer than the specified version.
    
    Parameters:
        version (str): The software version to be matched against the versions in `version_map`.
        version_map (dict): A dictionary where keys are strings representing software versions and values are corresponding metadata or identifiers.
        
    Returns:
        str: The closest available version in `version_map` that is newer than the specified `version`, based on LooseVersion comparison. If no such version exists, it returns the oldest version in `version_map`.
    
    Example:
        >>> version_map = {'1.0': 'metadata1', '2.0': 'metadata2', '3.0': 'metadata3'}
        >>> _version_fuzzy_match('1.5', version_map)
        '1.0'  # This is because '1.0' is the closest version that is newer than '1.5'.
        
        >>> _version_fuzzy_match('2.5', version_map)
        '2.0'  # This is because '2.0' is the nearest previous version to '2.5' in the map.
        
        >>> _version_fuzzy_match('4.0', version_map)
        '3.0'  # This is because '3.0' is the oldest version available and newer than '4.0'.
    """
    sorted_looseversions = sorted([LooseVersion(v) for v in version_map.keys()])
    find_looseversion = LooseVersion(version)

    # slot match; return nearest previous version we're newer than
    kpos = bisect.bisect(sorted_looseversions, find_looseversion)

    if kpos == 0:
        # older than everything in the list, return the oldest version
        return version_map[str(sorted_looseversions[0])]

    return version_map[str(sorted_looseversions[kpos - 1])]

def test_version_fuzzy_match_exact_match():
    version_map = {'1.0': 'metadata1', '2.0': 'metadata2', '3.0': 'metadata3'}
    with patch('ansible.executor.interpreter_discovery.LooseVersion', return_value=None):
        assert _version_fuzzy_match('1.0', version_map) == 'metadata1'

def test_version_fuzzy_match_nearest_previous():
    version_map = {'1.0': 'metadata1', '2.0': 'metadata2', '3.0': 'metadata3'}
    with patch('ansible.executor.interpreter_discovery.LooseVersion', return_value=None):
        assert _version_fuzzy_match('2.5', version_map) == 'metadata2'

def test_version_fuzzy_match_older_than_everything():
    version_map = {'1.0': 'metadata1', '2.0': 'metadata2', '3.0': 'metadata3'}
    with patch('ansible.executor.interpreter_discovery.LooseVersion', return_value=None):
        assert _version_fuzzy_match('4.0', version_map) == 'metadata3'
