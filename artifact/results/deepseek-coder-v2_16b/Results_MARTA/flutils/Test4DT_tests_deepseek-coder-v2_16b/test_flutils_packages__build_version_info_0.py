
import pytest
from flutils.packages import _build_version_info, _VersionInfo
from distutils.version import StrictVersion



def test_invalid_input():
    version = 'invalid_version'
    with pytest.raises(ValueError):
        _build_version_info(version)