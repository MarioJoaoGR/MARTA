
import pytest
import os
from semantic_release.ci_checks import gitlab
from semantic_release.errors import CiVerificationError

@pytest.fixture(autouse=True)
def setup_env():
    original_ci_commit_ref_name = os.environ.get("CI_COMMIT_REF_NAME", None)
    yield
    if original_ci_commit_ref_name is not None:
        os.environ["CI_COMMIT_REF_NAME"] = original_ci_commit_ref_name
    else:
        del os.environ["CI_COMMIT_REF_NAME"]


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_ci_checks_gitlab_0.py F [ 50%]
EF                                                                       [100%]

==================================== ERRORS ====================================
__________________ ERROR at teardown of test_missing_env_var ___________________

    @pytest.fixture(autouse=True)
    def setup_env():
        original_ci_commit_ref_name = os.environ.get("CI_COMMIT_REF_NAME", None)
        yield
        if original_ci_commit_ref_name is not None:
            os.environ["CI_COMMIT_REF_NAME"] = original_ci_commit_ref_name
        else:
>           del os.environ["CI_COMMIT_REF_NAME"]

/opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_ci_checks_gitlab_0.py:14: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = environ({'SHELL': '/bin/bash', 'NV_LIBCUBLAS_VERSION': '12.4.5.8-1', 'NVIDIA_VISIBLE_DEVICES': 'all', 'WARP_IS_SSH': '...SION': '8.3.2', 'PYTEST_CURRENT_TEST': 'test_semantic_release_ci_checks_gitlab_0.py::test_missing_env_var (teardown)'})
key = 'CI_COMMIT_REF_NAME'

    def __delitem__(self, key):
        encodedkey = self.encodekey(key)
        unsetenv(encodedkey)
        try:
            del self._data[encodedkey]
        except KeyError:
            # raise KeyError with the original key value
>           raise KeyError(key) from None
E           KeyError: 'CI_COMMIT_REF_NAME'

/opt/conda/envs/test4py_env/lib/python3.10/os.py:696: KeyError
=================================== FAILURES ===================================
_____________________________ test_missing_env_var _____________________________

args = ('release',), kwargs = {}

    def func_wrapper(*args, **kwargs):
        try:
>           func(*args, **kwargs)

/opt/marta/baselines/codamosa/replication/test-apps/python-semantic-release/semantic_release/ci_checks.py:20: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

branch = 'release'

    @checker
    def gitlab(branch: str):
        """
        Performs necessary checks to ensure that the gitlab build is one
        that should create releases.
    
        :param branch: The branch the environment should be running against.
        """
>       assert os.environ.get("CI_COMMIT_REF_NAME") == branch
E       AssertionError

/opt/marta/baselines/codamosa/replication/test-apps/python-semantic-release/semantic_release/ci_checks.py:87: AssertionError

During handling of the above exception, another exception occurred:

    def test_missing_env_var():
        with pytest.raises(AssertionError):
>           gitlab("release")

/opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_ci_checks_gitlab_0.py:18: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

args = ('release',), kwargs = {}

    def func_wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
            return True
        except AssertionError:
>           raise CiVerificationError(
                "The verification check for the environment did not pass."
            )
E           semantic_release.errors.CiVerificationError: The verification check for the environment did not pass.

/opt/marta/baselines/codamosa/replication/test-apps/python-semantic-release/semantic_release/ci_checks.py:23: CiVerificationError
____________________________ test_incorrect_branch _____________________________

args = ('release',), kwargs = {}

    def func_wrapper(*args, **kwargs):
        try:
>           func(*args, **kwargs)

/opt/marta/baselines/codamosa/replication/test-apps/python-semantic-release/semantic_release/ci_checks.py:20: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

branch = 'release'

    @checker
    def gitlab(branch: str):
        """
        Performs necessary checks to ensure that the gitlab build is one
        that should create releases.
    
        :param branch: The branch the environment should be running against.
        """
>       assert os.environ.get("CI_COMMIT_REF_NAME") == branch
E       AssertionError

/opt/marta/baselines/codamosa/replication/test-apps/python-semantic-release/semantic_release/ci_checks.py:87: AssertionError

During handling of the above exception, another exception occurred:

    def test_incorrect_branch():
        os.environ["CI_COMMIT_REF_NAME"] = "wrong_branch"
        with pytest.raises(AssertionError):
>           gitlab("release")

/opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_ci_checks_gitlab_0.py:23: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

args = ('release',), kwargs = {}

    def func_wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
            return True
        except AssertionError:
>           raise CiVerificationError(
                "The verification check for the environment did not pass."
            )
E           semantic_release.errors.CiVerificationError: The verification check for the environment did not pass.

/opt/marta/baselines/codamosa/replication/test-apps/python-semantic-release/semantic_release/ci_checks.py:23: CiVerificationError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_ci_checks_gitlab_0.py::test_missing_env_var
FAILED ../../../../../opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_ci_checks_gitlab_0.py::test_incorrect_branch
ERROR ../../../../../opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_ci_checks_gitlab_0.py::test_missing_env_var
========================== 2 failed, 1 error in 0.08s ==========================
"""