
import pytest
import os
from unittest.mock import patch
from semantic_release.ci_checks import circle

@pytest.mark.parametrize("branch, expected", [('release', True), ('wrong_branch', False)])
def test_circle(branch, expected):
    with patch.dict(os.environ, {"CIRCLE_BRANCH": branch, "CI_PULL_REQUEST": ""}):
        if not expected:
            with pytest.raises(AssertionError):
                circle(branch)
        else:
            circle(branch)
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_ci_checks_circle_0.py . [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_______________________ test_circle[wrong_branch-False] ________________________

branch = 'wrong_branch', expected = False

    @pytest.mark.parametrize("branch, expected", [('release', True), ('wrong_branch', False)])
    def test_circle(branch, expected):
        with patch.dict(os.environ, {"CIRCLE_BRANCH": branch, "CI_PULL_REQUEST": ""}):
            if not expected:
>               with pytest.raises(AssertionError):
E               Failed: DID NOT RAISE <class 'AssertionError'>

/opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_ci_checks_circle_0.py:11: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_ci_checks_circle_0.py::test_circle[wrong_branch-False]
========================= 1 failed, 1 passed in 0.07s ==========================
"""