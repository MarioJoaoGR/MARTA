
import pytest
from unittest.mock import patch
import os

def frigg(branch: str):
    """
    Performs necessary checks to ensure that the frigg build is one
    that should create releases.

    :param branch: The branch the environment should be running against.
    """
    assert os.environ.get("FRIGG_BUILD_BRANCH") == branch
    assert not os.environ.get("FRIGG_PULL_REQUEST")

@pytest.fixture(autouse=True)
def setup_env():
    # Save original environment variables
    saved_branch = os.environ.get("FRIGG_BUILD_BRANCH", None)
    saved_pull_request = os.environ.get("FRIGG_PULL_REQUEST", None)

    yield  # This is where the test run would happen.

    # Teardown: Restore original environment variables
    if saved_branch is not None:
        os.environ["FRIGG_BUILD_BRANCH"] = saved_branch
    else:
        del os.environ["FRIGG_BUILD_BRANCH"]
    if saved_pull_request is not None:
        os.environ["FRIGG_PULL_REQUEST"] = saved_pull_request
    else:
        del os.environ["FRIGG_PULL_REQUEST"]



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_ci_checks_frigg_0.py F [ 33%]
E.E.E                                                                    [100%]

==================================== ERRORS ====================================
_______________ ERROR at teardown of test_valid_input_happy_path _______________

    @pytest.fixture(autouse=True)
    def setup_env():
        # Save original environment variables
        saved_branch = os.environ.get("FRIGG_BUILD_BRANCH", None)
        saved_pull_request = os.environ.get("FRIGG_PULL_REQUEST", None)
    
        yield  # This is where the test run would happen.
    
        # Teardown: Restore original environment variables
        if saved_branch is not None:
            os.environ["FRIGG_BUILD_BRANCH"] = saved_branch
        else:
>           del os.environ["FRIGG_BUILD_BRANCH"]

/opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_ci_checks_frigg_0.py:28: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = environ({'SHELL': '/bin/bash', 'NV_LIBCUBLAS_VERSION': '12.4.5.8-1', 'NVIDIA_VISIBLE_DEVICES': 'all', 'WARP_IS_SSH': '... '8.3.2', 'PYTEST_CURRENT_TEST': 'test_semantic_release_ci_checks_frigg_0.py::test_valid_input_happy_path (teardown)'})
key = 'FRIGG_BUILD_BRANCH'

    def __delitem__(self, key):
        encodedkey = self.encodekey(key)
        unsetenv(encodedkey)
        try:
            del self._data[encodedkey]
        except KeyError:
            # raise KeyError with the original key value
>           raise KeyError(key) from None
E           KeyError: 'FRIGG_BUILD_BRANCH'

/opt/conda/envs/test4py_env/lib/python3.10/os.py:696: KeyError
___________ ERROR at teardown of test_missing_environment_variables ____________

    @pytest.fixture(autouse=True)
    def setup_env():
        # Save original environment variables
        saved_branch = os.environ.get("FRIGG_BUILD_BRANCH", None)
        saved_pull_request = os.environ.get("FRIGG_PULL_REQUEST", None)
    
        yield  # This is where the test run would happen.
    
        # Teardown: Restore original environment variables
        if saved_branch is not None:
            os.environ["FRIGG_BUILD_BRANCH"] = saved_branch
        else:
>           del os.environ["FRIGG_BUILD_BRANCH"]

/opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_ci_checks_frigg_0.py:28: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = environ({'SHELL': '/bin/bash', 'NV_LIBCUBLAS_VERSION': '12.4.5.8-1', 'NVIDIA_VISIBLE_DEVICES': 'all', 'WARP_IS_SSH': '...', 'PYTEST_CURRENT_TEST': 'test_semantic_release_ci_checks_frigg_0.py::test_missing_environment_variables (teardown)'})
key = 'FRIGG_BUILD_BRANCH'

    def __delitem__(self, key):
        encodedkey = self.encodekey(key)
        unsetenv(encodedkey)
        try:
            del self._data[encodedkey]
        except KeyError:
            # raise KeyError with the original key value
>           raise KeyError(key) from None
E           KeyError: 'FRIGG_BUILD_BRANCH'

/opt/conda/envs/test4py_env/lib/python3.10/os.py:696: KeyError
________________ ERROR at teardown of test_invalid_branch_name _________________

    @pytest.fixture(autouse=True)
    def setup_env():
        # Save original environment variables
        saved_branch = os.environ.get("FRIGG_BUILD_BRANCH", None)
        saved_pull_request = os.environ.get("FRIGG_PULL_REQUEST", None)
    
        yield  # This is where the test run would happen.
    
        # Teardown: Restore original environment variables
        if saved_branch is not None:
            os.environ["FRIGG_BUILD_BRANCH"] = saved_branch
        else:
>           del os.environ["FRIGG_BUILD_BRANCH"]

/opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_ci_checks_frigg_0.py:28: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = environ({'SHELL': '/bin/bash', 'NV_LIBCUBLAS_VERSION': '12.4.5.8-1', 'NVIDIA_VISIBLE_DEVICES': 'all', 'WARP_IS_SSH': '...N': '8.3.2', 'PYTEST_CURRENT_TEST': 'test_semantic_release_ci_checks_frigg_0.py::test_invalid_branch_name (teardown)'})
key = 'FRIGG_BUILD_BRANCH'

    def __delitem__(self, key):
        encodedkey = self.encodekey(key)
        unsetenv(encodedkey)
        try:
            del self._data[encodedkey]
        except KeyError:
            # raise KeyError with the original key value
>           raise KeyError(key) from None
E           KeyError: 'FRIGG_BUILD_BRANCH'

/opt/conda/envs/test4py_env/lib/python3.10/os.py:696: KeyError
=================================== FAILURES ===================================
_________________________ test_valid_input_happy_path __________________________

    def test_valid_input_happy_path():
        with patch.dict(os.environ, {"FRIGG_BUILD_BRANCH": "main", "FRIGG_PULL_REQUEST": "False"}):
>           frigg("main")

/opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_ci_checks_frigg_0.py:36: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

branch = 'main'

    def frigg(branch: str):
        """
        Performs necessary checks to ensure that the frigg build is one
        that should create releases.
    
        :param branch: The branch the environment should be running against.
        """
        assert os.environ.get("FRIGG_BUILD_BRANCH") == branch
>       assert not os.environ.get("FRIGG_PULL_REQUEST")
E       AssertionError: assert not 'False'
E        +  where 'False' = get('FRIGG_PULL_REQUEST')
E        +    where get = environ({'SHELL': '/bin/bash', 'NV_LIBCUBLAS_VERSION': '12.4.5.8-1', 'NVIDIA_VISIBLE_DEVICES': 'all', 'WARP_IS_SSH': '...i_checks_frigg_0.py::test_valid_input_happy_path (call)', 'FRIGG_BUILD_BRANCH': 'main', 'FRIGG_PULL_REQUEST': 'False'}).get
E        +      where environ({'SHELL': '/bin/bash', 'NV_LIBCUBLAS_VERSION': '12.4.5.8-1', 'NVIDIA_VISIBLE_DEVICES': 'all', 'WARP_IS_SSH': '...i_checks_frigg_0.py::test_valid_input_happy_path (call)', 'FRIGG_BUILD_BRANCH': 'main', 'FRIGG_PULL_REQUEST': 'False'}) = os.environ

/opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_ci_checks_frigg_0.py:14: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_ci_checks_frigg_0.py::test_valid_input_happy_path
ERROR ../../../../../opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_ci_checks_frigg_0.py::test_valid_input_happy_path
ERROR ../../../../../opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_ci_checks_frigg_0.py::test_missing_environment_variables
ERROR ../../../../../opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_ci_checks_frigg_0.py::test_invalid_branch_name
==================== 1 failed, 2 passed, 3 errors in 0.10s =====================
"""