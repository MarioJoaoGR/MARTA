
import os
import pytest
from semantic_release.ci_checks import jenkins

@pytest.fixture(autouse=True)
def setup_env():
    """Setup environment variables for the tests"""
    os.environ["BRANCH_NAME"] = "main"
    os.environ["JENKINS_URL"] = "<some_url>"
    os.environ["CHANGE_ID"] = None

@pytest.mark.parametrize("branch", ["main"])
def test_valid_input_main_branch(branch):
    jenkins(branch)
    assert os.environ.get("BRANCH_NAME") == branch
    assert os.environ.get("JENKINS_URL") is not None
    assert not os.environ.get("CHANGE_ID")  # pull request id

@pytest.mark.parametrize("branch", ["develop"])
def test_valid_input_develop_branch(branch):
    jenkins(branch)
    assert os.environ.get("BRANCH_NAME") == branch
    assert os.environ.get("JENKINS_URL") is not None
    assert not os.environ.get("CHANGE_ID")  # pull request id






"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 8 items

../../../../../opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_ci_checks_jenkins_0.py E [ 12%]
EEEEEEE                                                                  [100%]

==================================== ERRORS ====================================
_____________ ERROR at setup of test_valid_input_main_branch[main] _____________

    @pytest.fixture(autouse=True)
    def setup_env():
        """Setup environment variables for the tests"""
        os.environ["BRANCH_NAME"] = "main"
        os.environ["JENKINS_URL"] = "<some_url>"
>       os.environ["CHANGE_ID"] = None

/opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_ci_checks_jenkins_0.py:11: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/conda/envs/test4py_env/lib/python3.10/os.py:685: in __setitem__
    value = self.encodevalue(value)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

value = None

    def encode(value):
        if not isinstance(value, str):
>           raise TypeError("str expected, not %s" % type(value).__name__)
E           TypeError: str expected, not NoneType

/opt/conda/envs/test4py_env/lib/python3.10/os.py:757: TypeError
__________ ERROR at setup of test_valid_input_develop_branch[develop] __________

    @pytest.fixture(autouse=True)
    def setup_env():
        """Setup environment variables for the tests"""
        os.environ["BRANCH_NAME"] = "main"
        os.environ["JENKINS_URL"] = "<some_url>"
>       os.environ["CHANGE_ID"] = None

/opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_ci_checks_jenkins_0.py:11: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/conda/envs/test4py_env/lib/python3.10/os.py:685: in __setitem__
    value = self.encodevalue(value)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

value = None

    def encode(value):
        if not isinstance(value, str):
>           raise TypeError("str expected, not %s" % type(value).__name__)
E           TypeError: str expected, not NoneType

/opt/conda/envs/test4py_env/lib/python3.10/os.py:757: TypeError
__________________ ERROR at setup of test_missing_jenkins_url __________________

    @pytest.fixture(autouse=True)
    def setup_env():
        """Setup environment variables for the tests"""
        os.environ["BRANCH_NAME"] = "main"
        os.environ["JENKINS_URL"] = "<some_url>"
>       os.environ["CHANGE_ID"] = None

/opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_ci_checks_jenkins_0.py:11: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/conda/envs/test4py_env/lib/python3.10/os.py:685: in __setitem__
    value = self.encodevalue(value)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

value = None

    def encode(value):
        if not isinstance(value, str):
>           raise TypeError("str expected, not %s" % type(value).__name__)
E           TypeError: str expected, not NoneType

/opt/conda/envs/test4py_env/lib/python3.10/os.py:757: TypeError
_________________ ERROR at setup of test_missing_branch_in_env _________________

    @pytest.fixture(autouse=True)
    def setup_env():
        """Setup environment variables for the tests"""
        os.environ["BRANCH_NAME"] = "main"
        os.environ["JENKINS_URL"] = "<some_url>"
>       os.environ["CHANGE_ID"] = None

/opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_ci_checks_jenkins_0.py:11: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/conda/envs/test4py_env/lib/python3.10/os.py:685: in __setitem__
    value = self.encodevalue(value)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

value = None

    def encode(value):
        if not isinstance(value, str):
>           raise TypeError("str expected, not %s" % type(value).__name__)
E           TypeError: str expected, not NoneType

/opt/conda/envs/test4py_env/lib/python3.10/os.py:757: TypeError
________________ ERROR at setup of test_pull_request_id_present ________________

    @pytest.fixture(autouse=True)
    def setup_env():
        """Setup environment variables for the tests"""
        os.environ["BRANCH_NAME"] = "main"
        os.environ["JENKINS_URL"] = "<some_url>"
>       os.environ["CHANGE_ID"] = None

/opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_ci_checks_jenkins_0.py:11: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/conda/envs/test4py_env/lib/python3.10/os.py:685: in __setitem__
    value = self.encodevalue(value)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

value = None

    def encode(value):
        if not isinstance(value, str):
>           raise TypeError("str expected, not %s" % type(value).__name__)
E           TypeError: str expected, not NoneType

/opt/conda/envs/test4py_env/lib/python3.10/os.py:757: TypeError
__________________ ERROR at setup of test_empty_branch_in_env __________________

    @pytest.fixture(autouse=True)
    def setup_env():
        """Setup environment variables for the tests"""
        os.environ["BRANCH_NAME"] = "main"
        os.environ["JENKINS_URL"] = "<some_url>"
>       os.environ["CHANGE_ID"] = None

/opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_ci_checks_jenkins_0.py:11: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/conda/envs/test4py_env/lib/python3.10/os.py:685: in __setitem__
    value = self.encodevalue(value)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

value = None

    def encode(value):
        if not isinstance(value, str):
>           raise TypeError("str expected, not %s" % type(value).__name__)
E           TypeError: str expected, not NoneType

/opt/conda/envs/test4py_env/lib/python3.10/os.py:757: TypeError
_________________ ERROR at setup of test_invalid_branch_input __________________

    @pytest.fixture(autouse=True)
    def setup_env():
        """Setup environment variables for the tests"""
        os.environ["BRANCH_NAME"] = "main"
        os.environ["JENKINS_URL"] = "<some_url>"
>       os.environ["CHANGE_ID"] = None

/opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_ci_checks_jenkins_0.py:11: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/conda/envs/test4py_env/lib/python3.10/os.py:685: in __setitem__
    value = self.encodevalue(value)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

value = None

    def encode(value):
        if not isinstance(value, str):
>           raise TypeError("str expected, not %s" % type(value).__name__)
E           TypeError: str expected, not NoneType

/opt/conda/envs/test4py_env/lib/python3.10/os.py:757: TypeError
___________________ ERROR at setup of test_none_branch_input ___________________

    @pytest.fixture(autouse=True)
    def setup_env():
        """Setup environment variables for the tests"""
        os.environ["BRANCH_NAME"] = "main"
        os.environ["JENKINS_URL"] = "<some_url>"
>       os.environ["CHANGE_ID"] = None

/opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_ci_checks_jenkins_0.py:11: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
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
ERROR ../../../../../opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_ci_checks_jenkins_0.py::test_valid_input_main_branch[main]
ERROR ../../../../../opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_ci_checks_jenkins_0.py::test_valid_input_develop_branch[develop]
ERROR ../../../../../opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_ci_checks_jenkins_0.py::test_missing_jenkins_url
ERROR ../../../../../opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_ci_checks_jenkins_0.py::test_missing_branch_in_env
ERROR ../../../../../opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_ci_checks_jenkins_0.py::test_pull_request_id_present
ERROR ../../../../../opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_ci_checks_jenkins_0.py::test_empty_branch_in_env
ERROR ../../../../../opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_ci_checks_jenkins_0.py::test_invalid_branch_input
ERROR ../../../../../opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_ci_checks_jenkins_0.py::test_none_branch_input
============================== 8 errors in 0.17s ===============================
"""