
import os
import pytest
from semantic_release.ci_checks import check
from semantic_release.errors import CiVerificationError

# Test default branch check when no environment variables are set

# Test specific branch check when no environment variables are set
def test_check_specific_branch():
    os.environ["CIRCLECI"] = "true"
    os.environ["CIRCLE_BRANCH"] = "release"
    with pytest.raises(CiVerificationError):
        check("main")

# Test Travis CI environment with a specific branch
def test_check_travis():
    os.environ["TRAVIS"] = "true"
    os.environ["TRAVIS_BRANCH"] = "feature-branch"
    with pytest.raises(CiVerificationError):
        check("feature-branch")

# Test CircleCI environment with a specific branch
def test_check_circleci():
    os.environ["CIRCLECI"] = "true"
    os.environ["CIRCLE_BRANCH"] = "release"
    with pytest.raises(CiVerificationError):
        check("release")

# Test GitLab CI environment with a specific branch
def test_check_gitlab():
    os.environ["GITLAB_CI"] = "true"
    os.environ["CI_COMMIT_REF_NAME"] = "develop"
    with pytest.raises(CiVerificationError):
        check("develop")

# Test Jenkins environment with a specific branch
def test_check_jenkins():
    os.environ["JENKINS_URL"] = "true"
    os.environ["GIT_BRANCH"] = "feature-branch"
    with pytest.raises(CiVerificationError):
        check("feature-branch")

# Test Bitbucket environment with a specific branch
def test_check_bitbucket():
    os.environ["BITBUCKET_BUILD_NUMBER"] = "true"
    os.environ["BITBUCKET_BRANCH"] = "release"
    with pytest.raises(CiVerificationError):
        check("release")