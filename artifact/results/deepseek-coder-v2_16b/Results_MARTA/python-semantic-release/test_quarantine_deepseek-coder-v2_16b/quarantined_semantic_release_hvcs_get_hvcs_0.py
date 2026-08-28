
import pytest
from semantic_release.hvcs import get_hvcs
from semantic_release.errors import ImproperConfigurationError


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_hvcs_get_hvcs_0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
____________________________ test_valid_hvcs_class _____________________________

    def test_valid_hvcs_class():
        config = {'hvcs': 'MyHVCSHelper'}
>       with pytest.raises(ImproperConfigurationError) as excinfo:
E       Failed: DID NOT RAISE <class 'semantic_release.errors.ImproperConfigurationError'>

/opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_hvcs_get_hvcs_0.py:8: Failed
_______________________ test_missing_hvcs_configuration ________________________

    def test_missing_hvcs_configuration():
        config = {}
>       with pytest.raises(ImproperConfigurationError) as excinfo:
E       Failed: DID NOT RAISE <class 'semantic_release.errors.ImproperConfigurationError'>

/opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_hvcs_get_hvcs_0.py:14: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_hvcs_get_hvcs_0.py::test_valid_hvcs_class
FAILED ../../../../../opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_hvcs_get_hvcs_0.py::test_missing_hvcs_configuration
============================== 2 failed in 0.15s ===============================
"""