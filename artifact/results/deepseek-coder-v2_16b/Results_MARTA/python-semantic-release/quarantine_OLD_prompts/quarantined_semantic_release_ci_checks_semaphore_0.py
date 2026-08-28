
import pytest
import os
from unittest.mock import patch

def semaphore(branch: str):
    """
    Performs necessary checks to ensure that the semaphore build is successful,
    on the correct branch and not a pull-request.

    :param branch:  The branch the environment should be running against.
    """
    assert os.environ.get("BRANCH_NAME") == branch
    assert os.environ.get("PULL_REQUEST_NUMBER") is None
    assert os.environ.get("SEMAPHORE_THREAD_RESULT") != "failed"

@pytest.fixture(autouse=True)
def setup_env():
    # Save original environment variables
    original_branch = os.environ.get('BRANCH_NAME')
    original_pull_request = os.environ.get('PULL_REQUEST_NUMBER')
    original_thread_result = os.environ.get('SEMAPHORE_THREAD_RESULT')
    
    yield  # This is where the test runs
    
    # Teardown: Restore original environment variables
    if 'BRANCH_NAME' not in os.environ:
        del os.environ['BRANCH_NAME']
    if 'PULL_REQUEST_NUMBER' not in os.environ:
        del os.environ['PULL_REQUEST_NUMBER']
    if 'SEMAPHORE_THREAD_RESULT' not in os.environ:
        del os.environ['SEMAPHORE_THREAD_RESULT']

@pytest.fixture(autouse=True)
def setup_env_missing():
    # Save original environment variables
    original_branch = os.environ.get('BRANCH_NAME')
    original_pull_request = os.environ.get('PULL_REQUEST_NUMBER')
    original_thread_result = os.environ.get('SEMAPHORE_THREAD_RESULT')
    
    # Remove environment variables
    del os.environ['BRANCH_NAME']
    del os.environ['PULL_REQUEST_NUMBER']
    del os.environ['SEMAPHORE_THREAD_RESULT']
    
    yield  # This is where the test runs
    
    # Teardown: Restore original environment variables if they were removed
    if not original_branch:
        del os.environ['BRANCH_NAME']
    if not original_pull_request:
        del os.environ['PULL_REQUEST_NUMBER']
    if not original_thread_result:
        del os.environ['SEMAPHORE_THREAD_RESULT']

@pytest.mark.parametrize("branch", ["main"])
def test_valid_branch_match(branch):
    with patch.dict(os.environ, {"BRANCH_NAME": branch}):
        semaphore(branch)

@pytest.mark.parametrize("branch", ["develop"])
def test_invalid_branch(branch):
    with patch.dict(os.environ, {"BRANCH_NAME": branch, "PULL_REQUEST_NUMBER": "123"}):
        with pytest.raises(AssertionError):
            semaphore(branch)

@pytest.mark.parametrize("branch", ["staging"])
def test_missing_environment_variables(branch):
    with patch.dict(os.environ, {"BRANCH_NAME": branch}):
        with pytest.raises(AssertionError):
            semaphore(branch)
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_ci_checks_semaphore_0.py E [ 33%]
EEEEE                                                                    [100%]

==================================== ERRORS ====================================
_______________ ERROR at setup of test_valid_branch_match[main] ________________

    @pytest.fixture(autouse=True)
    def setup_env_missing():
        # Save original environment variables
        original_branch = os.environ.get('BRANCH_NAME')
        original_pull_request = os.environ.get('PULL_REQUEST_NUMBER')
        original_thread_result = os.environ.get('SEMAPHORE_THREAD_RESULT')
    
        # Remove environment variables
>       del os.environ['BRANCH_NAME']

/opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_ci_checks_semaphore_0.py:42: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = environ({'SHELL': '/bin/bash', 'NV_LIBCUBLAS_VERSION': '12.4.5.8-1', 'NVIDIA_VISIBLE_DEVICES': 'all', 'WARP_IS_SSH': '....3.2', 'PYTEST_CURRENT_TEST': 'test_semantic_release_ci_checks_semaphore_0.py::test_valid_branch_match[main] (setup)'})
key = 'BRANCH_NAME'

    def __delitem__(self, key):
        encodedkey = self.encodekey(key)
        unsetenv(encodedkey)
        try:
            del self._data[encodedkey]
        except KeyError:
            # raise KeyError with the original key value
>           raise KeyError(key) from None
E           KeyError: 'BRANCH_NAME'

/opt/conda/envs/test4py_env/lib/python3.10/os.py:696: KeyError
______________ ERROR at teardown of test_valid_branch_match[main] ______________

    @pytest.fixture(autouse=True)
    def setup_env():
        # Save original environment variables
        original_branch = os.environ.get('BRANCH_NAME')
        original_pull_request = os.environ.get('PULL_REQUEST_NUMBER')
        original_thread_result = os.environ.get('SEMAPHORE_THREAD_RESULT')
    
        yield  # This is where the test runs
    
        # Teardown: Restore original environment variables
        if 'BRANCH_NAME' not in os.environ:
>           del os.environ['BRANCH_NAME']

/opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_ci_checks_semaphore_0.py:28: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = environ({'SHELL': '/bin/bash', 'NV_LIBCUBLAS_VERSION': '12.4.5.8-1', 'NVIDIA_VISIBLE_DEVICES': 'all', 'WARP_IS_SSH': '...2', 'PYTEST_CURRENT_TEST': 'test_semantic_release_ci_checks_semaphore_0.py::test_valid_branch_match[main] (teardown)'})
key = 'BRANCH_NAME'

    def __delitem__(self, key):
        encodedkey = self.encodekey(key)
        unsetenv(encodedkey)
        try:
            del self._data[encodedkey]
        except KeyError:
            # raise KeyError with the original key value
>           raise KeyError(key) from None
E           KeyError: 'BRANCH_NAME'

/opt/conda/envs/test4py_env/lib/python3.10/os.py:696: KeyError
________________ ERROR at setup of test_invalid_branch[develop] ________________

    @pytest.fixture(autouse=True)
    def setup_env_missing():
        # Save original environment variables
        original_branch = os.environ.get('BRANCH_NAME')
        original_pull_request = os.environ.get('PULL_REQUEST_NUMBER')
        original_thread_result = os.environ.get('SEMAPHORE_THREAD_RESULT')
    
        # Remove environment variables
>       del os.environ['BRANCH_NAME']

/opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_ci_checks_semaphore_0.py:42: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = environ({'SHELL': '/bin/bash', 'NV_LIBCUBLAS_VERSION': '12.4.5.8-1', 'NVIDIA_VISIBLE_DEVICES': 'all', 'WARP_IS_SSH': '...8.3.2', 'PYTEST_CURRENT_TEST': 'test_semantic_release_ci_checks_semaphore_0.py::test_invalid_branch[develop] (setup)'})
key = 'BRANCH_NAME'

    def __delitem__(self, key):
        encodedkey = self.encodekey(key)
        unsetenv(encodedkey)
        try:
            del self._data[encodedkey]
        except KeyError:
            # raise KeyError with the original key value
>           raise KeyError(key) from None
E           KeyError: 'BRANCH_NAME'

/opt/conda/envs/test4py_env/lib/python3.10/os.py:696: KeyError
______________ ERROR at teardown of test_invalid_branch[develop] _______________

    @pytest.fixture(autouse=True)
    def setup_env():
        # Save original environment variables
        original_branch = os.environ.get('BRANCH_NAME')
        original_pull_request = os.environ.get('PULL_REQUEST_NUMBER')
        original_thread_result = os.environ.get('SEMAPHORE_THREAD_RESULT')
    
        yield  # This is where the test runs
    
        # Teardown: Restore original environment variables
        if 'BRANCH_NAME' not in os.environ:
>           del os.environ['BRANCH_NAME']

/opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_ci_checks_semaphore_0.py:28: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = environ({'SHELL': '/bin/bash', 'NV_LIBCUBLAS_VERSION': '12.4.5.8-1', 'NVIDIA_VISIBLE_DEVICES': 'all', 'WARP_IS_SSH': '....2', 'PYTEST_CURRENT_TEST': 'test_semantic_release_ci_checks_semaphore_0.py::test_invalid_branch[develop] (teardown)'})
key = 'BRANCH_NAME'

    def __delitem__(self, key):
        encodedkey = self.encodekey(key)
        unsetenv(encodedkey)
        try:
            del self._data[encodedkey]
        except KeyError:
            # raise KeyError with the original key value
>           raise KeyError(key) from None
E           KeyError: 'BRANCH_NAME'

/opt/conda/envs/test4py_env/lib/python3.10/os.py:696: KeyError
________ ERROR at setup of test_missing_environment_variables[staging] _________

    @pytest.fixture(autouse=True)
    def setup_env_missing():
        # Save original environment variables
        original_branch = os.environ.get('BRANCH_NAME')
        original_pull_request = os.environ.get('PULL_REQUEST_NUMBER')
        original_thread_result = os.environ.get('SEMAPHORE_THREAD_RESULT')
    
        # Remove environment variables
>       del os.environ['BRANCH_NAME']

/opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_ci_checks_semaphore_0.py:42: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = environ({'SHELL': '/bin/bash', 'NV_LIBCUBLAS_VERSION': '12.4.5.8-1', 'NVIDIA_VISIBLE_DEVICES': 'all', 'WARP_IS_SSH': '..._CURRENT_TEST': 'test_semantic_release_ci_checks_semaphore_0.py::test_missing_environment_variables[staging] (setup)'})
key = 'BRANCH_NAME'

    def __delitem__(self, key):
        encodedkey = self.encodekey(key)
        unsetenv(encodedkey)
        try:
            del self._data[encodedkey]
        except KeyError:
            # raise KeyError with the original key value
>           raise KeyError(key) from None
E           KeyError: 'BRANCH_NAME'

/opt/conda/envs/test4py_env/lib/python3.10/os.py:696: KeyError
_______ ERROR at teardown of test_missing_environment_variables[staging] _______

    @pytest.fixture(autouse=True)
    def setup_env():
        # Save original environment variables
        original_branch = os.environ.get('BRANCH_NAME')
        original_pull_request = os.environ.get('PULL_REQUEST_NUMBER')
        original_thread_result = os.environ.get('SEMAPHORE_THREAD_RESULT')
    
        yield  # This is where the test runs
    
        # Teardown: Restore original environment variables
        if 'BRANCH_NAME' not in os.environ:
>           del os.environ['BRANCH_NAME']

/opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_ci_checks_semaphore_0.py:28: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = environ({'SHELL': '/bin/bash', 'NV_LIBCUBLAS_VERSION': '12.4.5.8-1', 'NVIDIA_VISIBLE_DEVICES': 'all', 'WARP_IS_SSH': '...RRENT_TEST': 'test_semantic_release_ci_checks_semaphore_0.py::test_missing_environment_variables[staging] (teardown)'})
key = 'BRANCH_NAME'

    def __delitem__(self, key):
        encodedkey = self.encodekey(key)
        unsetenv(encodedkey)
        try:
            del self._data[encodedkey]
        except KeyError:
            # raise KeyError with the original key value
>           raise KeyError(key) from None
E           KeyError: 'BRANCH_NAME'

/opt/conda/envs/test4py_env/lib/python3.10/os.py:696: KeyError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_ci_checks_semaphore_0.py::test_valid_branch_match[main]
ERROR ../../../../../opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_ci_checks_semaphore_0.py::test_valid_branch_match[main]
ERROR ../../../../../opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_ci_checks_semaphore_0.py::test_invalid_branch[develop]
ERROR ../../../../../opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_ci_checks_semaphore_0.py::test_invalid_branch[develop]
ERROR ../../../../../opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_ci_checks_semaphore_0.py::test_missing_environment_variables[staging]
ERROR ../../../../../opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_ci_checks_semaphore_0.py::test_missing_environment_variables[staging]
============================== 6 errors in 0.14s ===============================
"""