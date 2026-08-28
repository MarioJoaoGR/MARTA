
import pytest
import jedi
from thonny.jedi_utils import _using_older_jedi


def test_using_older_jedi_mocked_old_version():
    # Mock a version that is in the list of older versions
    mocked_jedi = type('MockJedi', (object,), {'__version__': '0.13'})()
    assert _using_older_jedi(mocked_jedi), "The mocked old version should be considered older"

def test_using_older_jedi_mocked_new_version():
    # Mock a version that is not in the list of older versions
    mocked_jedi = type('MockJedi', (object,), {'__version__': '0.18'})()
    assert not _using_older_jedi(mocked_jedi), "The mocked new version should not be considered older"