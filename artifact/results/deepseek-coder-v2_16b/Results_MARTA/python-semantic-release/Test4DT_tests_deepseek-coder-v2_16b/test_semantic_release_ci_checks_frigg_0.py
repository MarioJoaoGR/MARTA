
import os
import pytest
from semantic_release.ci_checks import frigg
from semantic_release.errors import CiVerificationError

def test_frigg_with_incorrect_branch():
    # Set the environment variables to have an incorrect branch
    os.environ["FRIGG_BUILD_BRANCH"] = "staging"
    os.environ["FRIGG_PULL_REQUEST"] = ""
    
    with pytest.raises(CiVerificationError):
        frigg("main")  # Assertion error expected, should raise CiVerificationError

def test_frigg_with_pull_request():
    # Set the environment variables to have a pull request active
    os.environ["FRIGG_BUILD_BRANCH"] = "main"
    os.environ["FRIGG_PULL_REQUEST"] = "true"
    
    with pytest.raises(CiVerificationError):
        frigg("main")  # Assertion error expected, should raise CiVerificationError
