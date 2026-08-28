
import pytest
from unittest.mock import patch
import os
from semantic_release.ci_checks import bitbucket
from semantic_release.errors import CiVerificationError


def test_edge_case():
    with patch.dict(os.environ, {"BITBUCKET_BRANCH": "", "BITBUCKET_PR_ID": '123'}):
        try:
            bitbucket('release')
        except CiVerificationError as e:
            assert str(e) == "The verification check for the environment did not pass."
