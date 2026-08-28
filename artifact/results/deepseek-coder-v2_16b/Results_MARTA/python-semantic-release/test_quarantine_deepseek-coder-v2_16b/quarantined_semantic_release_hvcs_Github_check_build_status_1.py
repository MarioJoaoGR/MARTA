
import pytest
from unittest.mock import patch, MagicMock
from semantic_release.hvcs import Github
from requests.exceptions import HTTPError
import logging

# Configure logger for warnings
logger = logging.getLogger('semantic_release')
logger.setLevel(logging.WARNING)




"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 4 items

../../../../../opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_hvcs_Github_check_build_status_1.py F [ 25%]
FFF                                                                      [100%]

=================================== FAILURES ===================================
_______________________ test_check_build_status_success ________________________

    def test_check_build_status_success():
        with patch('semantic_release.hvcs.Github.session') as mock_session:
            mock_response = MagicMock()
            mock_response.json.return_value = {"state": "success"}
            mock_session.get.return_value = mock_response
    
            result = Github.check_build_status('owner', 'repo', 'ref')
>           assert result is True
E           assert False is True

/opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_hvcs_Github_check_build_status_1.py:19: AssertionError
____________________ test_check_build_status_invalid_owner _____________________

    def test_check_build_status_invalid_owner():
        with patch('semantic_release.hvcs.Github.session') as mock_session:
            mock_response = MagicMock()
            mock_response.json.return_value = {"state": "failure"}
            mock_session.get.side_effect = HTTPError("Invalid owner")
    
>           with pytest.raises(HTTPError):
E           Failed: DID NOT RAISE <class 'requests.exceptions.HTTPError'>

/opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_hvcs_Github_check_build_status_1.py:27: Failed
_____________________ test_check_build_status_invalid_repo _____________________

    def test_check_build_status_invalid_repo():
        with patch('semantic_release.hvcs.Github.session') as mock_session:
            mock_response = MagicMock()
            mock_response.json.return_value = {"state": "failure"}
            mock_session.get.side_effect = HTTPError("Invalid repo")
    
>           with pytest.raises(HTTPError):
E           Failed: DID NOT RAISE <class 'requests.exceptions.HTTPError'>

/opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_hvcs_Github_check_build_status_1.py:36: Failed
_____________________ test_check_build_status_invalid_ref ______________________

    def test_check_build_status_invalid_ref():
        with patch('semantic_release.hvcs.Github.session') as mock_session:
            mock_response = MagicMock()
            mock_response.json.return_value = {"state": "failure"}
            mock_session.get.side_effect = HTTPError("Invalid ref")
    
>           with pytest.raises(HTTPError):
E           Failed: DID NOT RAISE <class 'requests.exceptions.HTTPError'>

/opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_hvcs_Github_check_build_status_1.py:45: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_hvcs_Github_check_build_status_1.py::test_check_build_status_success
FAILED ../../../../../opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_hvcs_Github_check_build_status_1.py::test_check_build_status_invalid_owner
FAILED ../../../../../opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_hvcs_Github_check_build_status_1.py::test_check_build_status_invalid_repo
FAILED ../../../../../opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_hvcs_Github_check_build_status_1.py::test_check_build_status_invalid_ref
============================== 4 failed in 0.18s ===============================
"""