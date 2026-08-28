
import re
import pytest
from unittest.mock import patch

# Define a regular expression pattern for VCS URL validation
_VCS_RE = r'^(svn\+http|git\+http|hg\+http|bzr\+http|file://)'

def _is_vcs_url(name):
    """Test whether a name is a vcs url or not."""
    return re.match(_VCS_RE, name)

# Test cases for valid VCS URL inputs
@pytest.mark.parametrize("name", ["https://github.com/user/repo.git"])
def test_valid_vcs_url_happy_path(name):
    assert _is_vcs_url(name) is True

# Test case for invalid VCS URL inputs
@pytest.mark.parametrize("name", ["invalid-url"])
def test_invalid_vcs_url(name):
    assert _is_vcs_url(name) is False

# Test case for handling None input
@pytest.mark.parametrize("name", [None])
def test_none_input(name):
    assert _is_vcs_url(name) is False
