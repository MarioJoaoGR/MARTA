
import pytest
from distutils.version import StrictVersion
from flutils.packages import _build_version_info, _VersionInfo, _each_version_part



def test_invalid_input():
    version = "invalid_version"
    with pytest.raises(ValueError):
        ver_info = _build_version_info(version)