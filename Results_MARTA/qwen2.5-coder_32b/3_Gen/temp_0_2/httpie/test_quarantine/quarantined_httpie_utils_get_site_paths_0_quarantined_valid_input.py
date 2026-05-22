
import pytest
from pathlib import Path
from httpie.utils import get_site_paths
from unittest.mock import patch

@pytest.fixture(scope="module")
def expected_site_paths():
    # Define the expected site paths for a given base installation path
    return [Path('/python/installations/site-packages-py38'), Path('/python/installations/site-packages-py39')]

@pytest.mark.parametrize("path, expected", [
    (Path('/python/installations'), expected_site_paths())
])
def test_valid_input(path, expected):
    with patch('httpie.utils.is_frozen', return_value=False):
        site_paths = list(get_site_paths(path))
        assert site_paths == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/httpie
configfile: pytest.ini
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 0 items / 1 error

==================================== ERRORS ====================================
_ ERROR collecting Test4DT_tests_qwen2.5-coder_32b/test_httpie_utils_get_site_paths_0_test_valid_input.py _
Fixture "expected_site_paths" called directly. Fixtures are not meant to be called directly,
but are created automatically when test functions request them as parameters.
See https://docs.pytest.org/en/stable/explanation/fixtures.html for more information about fixtures, and
https://docs.pytest.org/en/stable/deprecations.html#calling-fixtures-directly about how to update your code.
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
=========================== short test summary info ============================
ERROR httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_utils_get_site_paths_0_test_valid_input.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.20s ===============================
"""