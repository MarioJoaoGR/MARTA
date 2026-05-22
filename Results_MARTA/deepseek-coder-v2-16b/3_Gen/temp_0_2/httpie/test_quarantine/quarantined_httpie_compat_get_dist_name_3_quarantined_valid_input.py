
import pytest
from unittest.mock import patch, MagicMock
import importlib.metadata as importlib_metadata
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

@pytest.mark.parametrize("entry_point, expected", [
    (importlib_metadata.EntryPoint('some_name', 'some_module'), 'some_name'),
    (importlib_metadata.EntryPoint('another_name', 'another_module.submodule'), 'another_name')
])
def test_valid_input(entry_point, expected):
    with patch('importlib.metadata.metadata', return_value=MagicMock(get='some_name')):
        assert get_dist_name(entry_point) == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_deepseek-coder-v2_16b.test_httpie_compat_get_dist_name_3_test_valid_input
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_compat_get_dist_name_3_test_valid_input.py:25:5: E1120: No value for argument 'group' in constructor call (no-value-for-parameter)
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_compat_get_dist_name_3_test_valid_input.py:26:5: E1120: No value for argument 'group' in constructor call (no-value-for-parameter)


"""