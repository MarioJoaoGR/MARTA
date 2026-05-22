
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
        return metadata.get('name')

def test_error_case():
    with patch('importlib_metadata.metadata', side_effect=importlib_metadata.PackageNotFoundError):
        ep = MagicMock()
        ep.pattern = MagicMock()
        ep.value = 'invalid_module'

        result = get_dist_name(ep)
        assert result is None

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_qwen2.5-coder_32b.test_httpie_compat_get_dist_name_2_test_error_case
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_compat_get_dist_name_2_test_error_case.py:6:65: E0602: Undefined variable 'Optional' (undefined-variable)


"""