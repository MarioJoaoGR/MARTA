
import pytest
import os
from unittest.mock import patch
from semantic_release.ci_checks import travis

@pytest.fixture(autouse=True)
def setup_env():
    saved_branch = os.environ.get('TRAVIS_BRANCH')
    saved_pull_request = os.environ.get('TRAVIS_PULL_REQUEST')
    
    yield  # This is where the test runs
    
    if saved_branch is not None:
        os.environ['TRAVIS_BRANCH'] = saved_branch
    else:
        del os.environ['TRAVIS_BRANCH']
    
    if saved_pull_request is not None:
        os.environ['TRAVIS_PULL_REQUEST'] = saved_pull_request
    else:
        del os.environ['TRAVIS_PULL_REQUEST']



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_ci_checks_travis_0.py . [ 33%]
EFEFE                                                                    [100%]

==================================== ERRORS ====================================
____________________ ERROR at teardown of test_valid_input _____________________

    @pytest.fixture(autouse=True)
    def setup_env():
        saved_branch = os.environ.get('TRAVIS_BRANCH')
        saved_pull_request = os.environ.get('TRAVIS_PULL_REQUEST')
    
        yield  # This is where the test runs
    
        if saved_branch is not None:
            os.environ['TRAVIS_BRANCH'] = saved_branch
        else:
>           del os.environ['TRAVIS_BRANCH']

/opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_ci_checks_travis_0.py:17: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = environ({'SHELL': '/bin/bash', 'NV_LIBCUBLAS_VERSION': '12.4.5.8-1', 'NVIDIA_VISIBLE_DEVICES': 'all', 'WARP_IS_SSH': '..._VERSION': '8.3.2', 'PYTEST_CURRENT_TEST': 'test_semantic_release_ci_checks_travis_0.py::test_valid_input (teardown)'})
key = 'TRAVIS_BRANCH'

    def __delitem__(self, key):
        encodedkey = self.encodekey(key)
        unsetenv(encodedkey)
        try:
            del self._data[encodedkey]
        except KeyError:
            # raise KeyError with the original key value
>           raise KeyError(key) from None
E           KeyError: 'TRAVIS_BRANCH'

/opt/conda/envs/test4py_env/lib/python3.10/os.py:696: KeyError
__________________ ERROR at teardown of test_missing_env_vars __________________

    @pytest.fixture(autouse=True)
    def setup_env():
        saved_branch = os.environ.get('TRAVIS_BRANCH')
        saved_pull_request = os.environ.get('TRAVIS_PULL_REQUEST')
    
        yield  # This is where the test runs
    
        if saved_branch is not None:
            os.environ['TRAVIS_BRANCH'] = saved_branch
        else:
>           del os.environ['TRAVIS_BRANCH']

/opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_ci_checks_travis_0.py:17: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = environ({'SHELL': '/bin/bash', 'NV_LIBCUBLAS_VERSION': '12.4.5.8-1', 'NVIDIA_VISIBLE_DEVICES': 'all', 'WARP_IS_SSH': '...ION': '8.3.2', 'PYTEST_CURRENT_TEST': 'test_semantic_release_ci_checks_travis_0.py::test_missing_env_vars (teardown)'})
key = 'TRAVIS_BRANCH'

    def __delitem__(self, key):
        encodedkey = self.encodekey(key)
        unsetenv(encodedkey)
        try:
            del self._data[encodedkey]
        except KeyError:
            # raise KeyError with the original key value
>           raise KeyError(key) from None
E           KeyError: 'TRAVIS_BRANCH'

/opt/conda/envs/test4py_env/lib/python3.10/os.py:696: KeyError
___________________ ERROR at teardown of test_invalid_branch ___________________

    @pytest.fixture(autouse=True)
    def setup_env():
        saved_branch = os.environ.get('TRAVIS_BRANCH')
        saved_pull_request = os.environ.get('TRAVIS_PULL_REQUEST')
    
        yield  # This is where the test runs
    
        if saved_branch is not None:
            os.environ['TRAVIS_BRANCH'] = saved_branch
        else:
>           del os.environ['TRAVIS_BRANCH']

/opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_ci_checks_travis_0.py:17: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = environ({'SHELL': '/bin/bash', 'NV_LIBCUBLAS_VERSION': '12.4.5.8-1', 'NVIDIA_VISIBLE_DEVICES': 'all', 'WARP_IS_SSH': '...RSION': '8.3.2', 'PYTEST_CURRENT_TEST': 'test_semantic_release_ci_checks_travis_0.py::test_invalid_branch (teardown)'})
key = 'TRAVIS_BRANCH'

    def __delitem__(self, key):
        encodedkey = self.encodekey(key)
        unsetenv(encodedkey)
        try:
            del self._data[encodedkey]
        except KeyError:
            # raise KeyError with the original key value
>           raise KeyError(key) from None
E           KeyError: 'TRAVIS_BRANCH'

/opt/conda/envs/test4py_env/lib/python3.10/os.py:696: KeyError
=================================== FAILURES ===================================
____________________________ test_missing_env_vars _____________________________

    def test_missing_env_vars():
>       del os.environ['TRAVIS_BRANCH']

/opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_ci_checks_travis_0.py:29: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = environ({'SHELL': '/bin/bash', 'NV_LIBCUBLAS_VERSION': '12.4.5.8-1', 'NVIDIA_VISIBLE_DEVICES': 'all', 'WARP_IS_SSH': '...VERSION': '8.3.2', 'PYTEST_CURRENT_TEST': 'test_semantic_release_ci_checks_travis_0.py::test_missing_env_vars (call)'})
key = 'TRAVIS_BRANCH'

    def __delitem__(self, key):
        encodedkey = self.encodekey(key)
        unsetenv(encodedkey)
        try:
            del self._data[encodedkey]
        except KeyError:
            # raise KeyError with the original key value
>           raise KeyError(key) from None
E           KeyError: 'TRAVIS_BRANCH'

/opt/conda/envs/test4py_env/lib/python3.10/os.py:696: KeyError
_____________________________ test_invalid_branch ______________________________

args = ('main',), kwargs = {}

    def func_wrapper(*args, **kwargs):
        try:
>           func(*args, **kwargs)

/opt/marta/baselines/codamosa/replication/test-apps/python-semantic-release/semantic_release/ci_checks.py:20: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

branch = 'main'

    @checker
    def travis(branch: str):
        """
        Performs necessary checks to ensure that the travis build is one
        that should create releases.
    
        :param branch: The branch the environment should be running against.
        """
>       assert os.environ.get("TRAVIS_BRANCH") == branch
E       AssertionError

/opt/marta/baselines/codamosa/replication/test-apps/python-semantic-release/semantic_release/ci_checks.py:38: AssertionError

During handling of the above exception, another exception occurred:

    def test_invalid_branch():
        with patch('os.environ', {'TRAVIS_BRANCH': 'wrong_branch', 'TRAVIS_PULL_REQUEST': 'false'}):
            with pytest.raises(AssertionError):
>               travis("main")

/opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_ci_checks_travis_0.py:38: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

args = ('main',), kwargs = {}

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
FAILED ../../../../../opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_ci_checks_travis_0.py::test_missing_env_vars
FAILED ../../../../../opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_ci_checks_travis_0.py::test_invalid_branch
ERROR ../../../../../opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_ci_checks_travis_0.py::test_valid_input
ERROR ../../../../../opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_ci_checks_travis_0.py::test_missing_env_vars
ERROR ../../../../../opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_ci_checks_travis_0.py::test_invalid_branch
==================== 2 failed, 1 passed, 3 errors in 0.11s =====================
"""