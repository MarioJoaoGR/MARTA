
import pytest
from unittest.mock import patch, MagicMock
import importlib_metadata

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
        return metadata.get('Name')  # Corrected to 'Name' as per the documentation example

@patch('httpie.compat.importlib_metadata')
def test_valid_input(mock_importlib_metadata):
    entry_point = MagicMock()
    dist = MagicMock()
    dist.name = 'some_dist_name'
    entry_point.dist = dist

    result = get_dist_name(entry_point)
    assert result == 'some_dist_name'

    # Test when the package is not found
    mock_importlib_metadata.metadata.side_effect = importlib_metadata.PackageNotFoundError
    entry_point.dist = None
    result = get_dist_name(entry_point)
    assert result is None

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_deepseek-coder-v2_16b.test_httpie_compat_get_dist_name_5_test_valid_input
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_compat_get_dist_name_5_test_valid_input.py:6:65: E0602: Undefined variable 'Optional' (undefined-variable)


"""