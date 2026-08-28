
import pytest
from unittest.mock import patch
import os
from semantic_release.ci_checks import bitbucket
from semantic_release.errors import CiVerificationError

def test_valid_branch_match():
    with patch('os.environ', {'BITBUCKET_BRANCH': 'release'}):
        try:
            bitbucket('release')
        except AssertionError as e:
            pytest.fail(f"Unexpected AssertionError: {e}")

