
import pytest
from semantic_release.dist import should_build

@pytest.mark.parametrize("config, expected", [
    ({'config': {'build_command': 'make build', 'upload_to_pypi': 'true', 'upload_to_release': 'true'}}, True),
    ({'config': {'build_command': 'make build', 'upload_to_pypi': 'true', 'upload_to_release': 'false'}}, True),
    ({'config': {'build_command': 'make build', 'upload_to_pypi': 'false', 'upload_to_release': 'false'}}, False),
])
def test_should_build(config, expected):
    assert should_build(config) == expected
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_dist_should_build_0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
_______________________ test_should_build[config0-True] ________________________

config = {'config': {'build_command': 'make build', 'upload_to_pypi': 'true', 'upload_to_release': 'true'}}
expected = True

    @pytest.mark.parametrize("config, expected", [
        ({'config': {'build_command': 'make build', 'upload_to_pypi': 'true', 'upload_to_release': 'true'}}, True),
        ({'config': {'build_command': 'make build', 'upload_to_pypi': 'true', 'upload_to_release': 'false'}}, True),
        ({'config': {'build_command': 'make build', 'upload_to_pypi': 'false', 'upload_to_release': 'false'}}, False),
    ])
    def test_should_build(config, expected):
>       assert should_build(config) == expected
E       TypeError: should_build() takes 0 positional arguments but 1 was given

/opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_dist_should_build_0.py:11: TypeError
_______________________ test_should_build[config1-True] ________________________

config = {'config': {'build_command': 'make build', 'upload_to_pypi': 'true', 'upload_to_release': 'false'}}
expected = True

    @pytest.mark.parametrize("config, expected", [
        ({'config': {'build_command': 'make build', 'upload_to_pypi': 'true', 'upload_to_release': 'true'}}, True),
        ({'config': {'build_command': 'make build', 'upload_to_pypi': 'true', 'upload_to_release': 'false'}}, True),
        ({'config': {'build_command': 'make build', 'upload_to_pypi': 'false', 'upload_to_release': 'false'}}, False),
    ])
    def test_should_build(config, expected):
>       assert should_build(config) == expected
E       TypeError: should_build() takes 0 positional arguments but 1 was given

/opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_dist_should_build_0.py:11: TypeError
_______________________ test_should_build[config2-False] _______________________

config = {'config': {'build_command': 'make build', 'upload_to_pypi': 'false', 'upload_to_release': 'false'}}
expected = False

    @pytest.mark.parametrize("config, expected", [
        ({'config': {'build_command': 'make build', 'upload_to_pypi': 'true', 'upload_to_release': 'true'}}, True),
        ({'config': {'build_command': 'make build', 'upload_to_pypi': 'true', 'upload_to_release': 'false'}}, True),
        ({'config': {'build_command': 'make build', 'upload_to_pypi': 'false', 'upload_to_release': 'false'}}, False),
    ])
    def test_should_build(config, expected):
>       assert should_build(config) == expected
E       TypeError: should_build() takes 0 positional arguments but 1 was given

/opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_dist_should_build_0.py:11: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_dist_should_build_0.py::test_should_build[config0-True]
FAILED ../../../../../opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_dist_should_build_0.py::test_should_build[config1-True]
FAILED ../../../../../opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_dist_should_build_0.py::test_should_build[config2-False]
============================== 3 failed in 0.12s ===============================
"""