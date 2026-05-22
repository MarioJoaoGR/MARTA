
import pytest
from importlib import metadata as importlib_metadata
from unittest.mock import patch, MagicMock
from typing import Optional

def get_dist_name(entry_point: importlib_metadata.EntryPoint) -> Optional[str]:
    dist = getattr(entry_point, "dist", None)
    if dist is not None:  # Python 3.10+
        return dist.name

    match = entry_point.pattern.match(entry_point.value)
    if not (match and match.group('module')):
        return None

    package = match.group('module').split('.')[0]
    try:
        metadata = importlib_metadata.metadata(package)
    except importlib_metadata.PackageNotFoundError:
        return None
    else:
        return metadata.get('name')

def test_invalid_entry_point():
    ep = importlib_metadata.EntryPoint('invalid', 'invalid_module')
    
    with patch('importlib_metadata.metadata', side_effect=importlib_metadata.PackageNotFoundError):
        assert get_dist_name(ep) is None

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_deepseek-coder-v2_16b.test_httpie_compat_get_dist_name_5_test_invalid_entry_point
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_compat_get_dist_name_5_test_invalid_entry_point.py:25:9: E1120: No value for argument 'group' in constructor call (no-value-for-parameter)


"""