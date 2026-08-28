
import pytest
import os
from unittest.mock import patch
from semantic_release.ci_checks import bitbucket

@pytest.fixture(autouse=True)
def setup_env():
    # Save original env variables
    saved_branch = os.environ.get('BITBUCKET_BRANCH')
    saved_pr_id = os.environ.get('BITBUCKET_PR_ID')
    
    yield  # This is where the test runs
    
    # Teardown: restore original env variables
    if saved_branch is not None:
        os.environ['BITBUCKET_BRANCH'] = saved_branch
    else:
        del os.environ['BITBUCKET_BRANCH']
    
    if saved_pr_id is not None:
        os.environ['BITBUCKET_PR_ID'] = saved_pr_id
    else:
        del os.environ['BITBUCKET_PR_ID']



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_ci_checks_bitbucket_0.py F [ 33%]
EFEFE                                                                    [100%]

==================================== ERRORS ====================================
_________________ ERROR at teardown of test_valid_branch_input _________________

    @pytest.fixture(autouse=True)
    def setup_env():
        # Save original env variables
        saved_branch = os.environ.get('BITBUCKET_BRANCH')
        saved_pr_id = os.environ.get('BITBUCKET_PR_ID')
    
        yield  # This is where the test runs
    
        # Teardown: restore original env variables
        if saved_branch is not None:
            os.environ['BITBUCKET_BRANCH'] = saved_branch
        else:
            del os.environ['BITBUCKET_BRANCH']
    
        if saved_pr_id is not None:
            os.environ['BITBUCKET_PR_ID'] = saved_pr_id
        else:
>           del os.environ['BITBUCKET_PR_ID']

/opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_ci_checks_bitbucket_0.py:24: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = environ({'SHELL': '/bin/bash', 'NV_LIBCUBLAS_VERSION': '12.4.5.8-1', 'NVIDIA_VISIBLE_DEVICES': 'all', 'WARP_IS_SSH': '... '8.3.2', 'PYTEST_CURRENT_TEST': 'test_semantic_release_ci_checks_bitbucket_0.py::test_valid_branch_input (teardown)'})
key = 'BITBUCKET_PR_ID'

    def __delitem__(self, key):
        encodedkey = self.encodekey(key)
        unsetenv(encodedkey)
        try:
            del self._data[encodedkey]
        except KeyError:
            # raise KeyError with the original key value
>           raise KeyError(key) from None
E           KeyError: 'BITBUCKET_PR_ID'

/opt/conda/envs/test4py_env/lib/python3.10/os.py:696: KeyError
_________________ ERROR at teardown of test_missing_branch_env _________________

    @pytest.fixture(autouse=True)
    def setup_env():
        # Save original env variables
        saved_branch = os.environ.get('BITBUCKET_BRANCH')
        saved_pr_id = os.environ.get('BITBUCKET_PR_ID')
    
        yield  # This is where the test runs
    
        # Teardown: restore original env variables
        if saved_branch is not None:
            os.environ['BITBUCKET_BRANCH'] = saved_branch
        else:
>           del os.environ['BITBUCKET_BRANCH']

/opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_ci_checks_bitbucket_0.py:19: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = environ({'SHELL': '/bin/bash', 'NV_LIBCUBLAS_VERSION': '12.4.5.8-1', 'NVIDIA_VISIBLE_DEVICES': 'all', 'WARP_IS_SSH': '... '8.3.2', 'PYTEST_CURRENT_TEST': 'test_semantic_release_ci_checks_bitbucket_0.py::test_missing_branch_env (teardown)'})
key = 'BITBUCKET_BRANCH'

    def __delitem__(self, key):
        encodedkey = self.encodekey(key)
        unsetenv(encodedkey)
        try:
            del self._data[encodedkey]
        except KeyError:
            # raise KeyError with the original key value
>           raise KeyError(key) from None
E           KeyError: 'BITBUCKET_BRANCH'

/opt/conda/envs/test4py_env/lib/python3.10/os.py:696: KeyError
________________ ERROR at teardown of test_invalid_branch_input ________________

    @pytest.fixture(autouse=True)
    def setup_env():
        # Save original env variables
        saved_branch = os.environ.get('BITBUCKET_BRANCH')
        saved_pr_id = os.environ.get('BITBUCKET_PR_ID')
    
        yield  # This is where the test runs
    
        # Teardown: restore original env variables
        if saved_branch is not None:
            os.environ['BITBUCKET_BRANCH'] = saved_branch
        else:
            del os.environ['BITBUCKET_BRANCH']
    
        if saved_pr_id is not None:
            os.environ['BITBUCKET_PR_ID'] = saved_pr_id
        else:
>           del os.environ['BITBUCKET_PR_ID']

/opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_ci_checks_bitbucket_0.py:24: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = environ({'SHELL': '/bin/bash', 'NV_LIBCUBLAS_VERSION': '12.4.5.8-1', 'NVIDIA_VISIBLE_DEVICES': 'all', 'WARP_IS_SSH': '...8.3.2', 'PYTEST_CURRENT_TEST': 'test_semantic_release_ci_checks_bitbucket_0.py::test_invalid_branch_input (teardown)'})
key = 'BITBUCKET_PR_ID'

    def __delitem__(self, key):
        encodedkey = self.encodekey(key)
        unsetenv(encodedkey)
        try:
            del self._data[encodedkey]
        except KeyError:
            # raise KeyError with the original key value
>           raise KeyError(key) from None
E           KeyError: 'BITBUCKET_PR_ID'

/opt/conda/envs/test4py_env/lib/python3.10/os.py:696: KeyError
=================================== FAILURES ===================================
___________________________ test_valid_branch_input ____________________________

    def test_valid_branch_input():
>       with patch.dict(os.environ, {"BITBUCKET_BRANCH": "release", "BITBUCKET_PR_ID": None}):

/opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_ci_checks_bitbucket_0.py:27: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/conda/envs/test4py_env/lib/python3.10/unittest/mock.py:1865: in __enter__
    self._patch_dict()
/opt/conda/envs/test4py_env/lib/python3.10/unittest/mock.py:1890: in _patch_dict
    in_dict.update(values)
/opt/conda/envs/test4py_env/lib/python3.10/_collections_abc.py:999: in update
    self[key] = other[key]
/opt/conda/envs/test4py_env/lib/python3.10/os.py:685: in __setitem__
    value = self.encodevalue(value)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

value = None

    def encode(value):
        if not isinstance(value, str):
>           raise TypeError("str expected, not %s" % type(value).__name__)
E           TypeError: str expected, not NoneType

/opt/conda/envs/test4py_env/lib/python3.10/os.py:757: TypeError
___________________________ test_missing_branch_env ____________________________

    def test_missing_branch_env():
>       del os.environ['BITBUCKET_BRANCH']

/opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_ci_checks_bitbucket_0.py:31: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = environ({'SHELL': '/bin/bash', 'NV_LIBCUBLAS_VERSION': '12.4.5.8-1', 'NVIDIA_VISIBLE_DEVICES': 'all', 'WARP_IS_SSH': '...ON': '8.3.2', 'PYTEST_CURRENT_TEST': 'test_semantic_release_ci_checks_bitbucket_0.py::test_missing_branch_env (call)'})
key = 'BITBUCKET_BRANCH'

    def __delitem__(self, key):
        encodedkey = self.encodekey(key)
        unsetenv(encodedkey)
        try:
            del self._data[encodedkey]
        except KeyError:
            # raise KeyError with the original key value
>           raise KeyError(key) from None
E           KeyError: 'BITBUCKET_BRANCH'

/opt/conda/envs/test4py_env/lib/python3.10/os.py:696: KeyError
__________________________ test_invalid_branch_input ___________________________

    def test_invalid_branch_input():
>       with patch.dict(os.environ, {"BITBUCKET_BRANCH": "invalid-branch", "BITBUCKET_PR_ID": None}):

/opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_ci_checks_bitbucket_0.py:36: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/conda/envs/test4py_env/lib/python3.10/unittest/mock.py:1865: in __enter__
    self._patch_dict()
/opt/conda/envs/test4py_env/lib/python3.10/unittest/mock.py:1890: in _patch_dict
    in_dict.update(values)
/opt/conda/envs/test4py_env/lib/python3.10/_collections_abc.py:999: in update
    self[key] = other[key]
/opt/conda/envs/test4py_env/lib/python3.10/os.py:685: in __setitem__
    value = self.encodevalue(value)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

value = None

    def encode(value):
        if not isinstance(value, str):
>           raise TypeError("str expected, not %s" % type(value).__name__)
E           TypeError: str expected, not NoneType

/opt/conda/envs/test4py_env/lib/python3.10/os.py:757: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_ci_checks_bitbucket_0.py::test_valid_branch_input
FAILED ../../../../../opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_ci_checks_bitbucket_0.py::test_missing_branch_env
FAILED ../../../../../opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_ci_checks_bitbucket_0.py::test_invalid_branch_input
ERROR ../../../../../opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_ci_checks_bitbucket_0.py::test_valid_branch_input
ERROR ../../../../../opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_ci_checks_bitbucket_0.py::test_missing_branch_env
ERROR ../../../../../opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_ci_checks_bitbucket_0.py::test_invalid_branch_input
========================= 3 failed, 3 errors in 0.22s ==========================
"""