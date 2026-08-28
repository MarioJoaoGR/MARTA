
import pytest
from unittest.mock import patch
from subprocess import run
import logging

# Configure logger for testing
logger = logging.getLogger('test_logger')

def build_dists():
    command = config.get("build_command")
    logger.info(f"Running {command}")
    run(command)

@pytest.mark.parametrize("config, expected", [
    ({}, "echo 'Build command'"),
    ({"build_command": "echo 'Custom build command'"}, "echo 'Custom build command'")
])
def test_valid_case(config, expected):
    with patch('builtins.print', new=lambda x: logger.info(x)):
        config["build_command"] = expected
        build_dists()

@pytest.mark.parametrize("config", [None, {}])
def test_edge_case(config):
    with patch('builtins.print', new=lambda x: logger.info(x)):
        if config is not None:
            config["build_command"] = None
        build_dists()

@pytest.mark.parametrize("config", [{}])
def test_error_handling(config):
    with patch('builtins.print', new=lambda x: logger.info(x)):
        config["build_command"] = None
        with pytest.raises(NameError):
            build_dists()
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 5 items

../../../../../opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_dist_build_dists_0.py F [ 20%]
FFF.                                                                     [100%]

=================================== FAILURES ===================================
________________ test_valid_case[config0-echo 'Build command'] _________________

config = {'build_command': "echo 'Build command'"}
expected = "echo 'Build command'"

    @pytest.mark.parametrize("config, expected", [
        ({}, "echo 'Build command'"),
        ({"build_command": "echo 'Custom build command'"}, "echo 'Custom build command'")
    ])
    def test_valid_case(config, expected):
        with patch('builtins.print', new=lambda x: logger.info(x)):
            config["build_command"] = expected
>           build_dists()

/opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_dist_build_dists_0.py:22: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

    def build_dists():
>       command = config.get("build_command")
E       NameError: name 'config' is not defined

/opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_dist_build_dists_0.py:11: NameError
_____________ test_valid_case[config1-echo 'Custom build command'] _____________

config = {'build_command': "echo 'Custom build command'"}
expected = "echo 'Custom build command'"

    @pytest.mark.parametrize("config, expected", [
        ({}, "echo 'Build command'"),
        ({"build_command": "echo 'Custom build command'"}, "echo 'Custom build command'")
    ])
    def test_valid_case(config, expected):
        with patch('builtins.print', new=lambda x: logger.info(x)):
            config["build_command"] = expected
>           build_dists()

/opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_dist_build_dists_0.py:22: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

    def build_dists():
>       command = config.get("build_command")
E       NameError: name 'config' is not defined

/opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_dist_build_dists_0.py:11: NameError
_____________________________ test_edge_case[None] _____________________________

config = None

    @pytest.mark.parametrize("config", [None, {}])
    def test_edge_case(config):
        with patch('builtins.print', new=lambda x: logger.info(x)):
            if config is not None:
                config["build_command"] = None
>           build_dists()

/opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_dist_build_dists_0.py:29: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

    def build_dists():
>       command = config.get("build_command")
E       NameError: name 'config' is not defined

/opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_dist_build_dists_0.py:11: NameError
___________________________ test_edge_case[config1] ____________________________

config = {'build_command': None}

    @pytest.mark.parametrize("config", [None, {}])
    def test_edge_case(config):
        with patch('builtins.print', new=lambda x: logger.info(x)):
            if config is not None:
                config["build_command"] = None
>           build_dists()

/opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_dist_build_dists_0.py:29: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

    def build_dists():
>       command = config.get("build_command")
E       NameError: name 'config' is not defined

/opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_dist_build_dists_0.py:11: NameError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_dist_build_dists_0.py::test_valid_case[config0-echo 'Build command']
FAILED ../../../../../opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_dist_build_dists_0.py::test_valid_case[config1-echo 'Custom build command']
FAILED ../../../../../opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_dist_build_dists_0.py::test_edge_case[None]
FAILED ../../../../../opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_dist_build_dists_0.py::test_edge_case[config1]
========================= 4 failed, 1 passed in 0.06s ==========================
"""