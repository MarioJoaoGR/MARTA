
import os
from pathlib import Path
from isort.deprecated.finders import parse_requirements, RequirementsFinder
from pytest import fixture
from unittest.mock import patch
from contextlib import chdir

@fixture
def mock_requirements_file():
    return '/tmp/pytest-of-joaovitorino/pytest-1/test_get_names_cached0/requirements.txt'

def test_get_names_cached(mock_requirements_file):
    with patch('isort.deprecated.finders.parse_requirements', autospec=True) as mock_parse:
        # Mock the parse_requirements to return a list of requirements
        mock_parse.return_value = {'package1': None, 'package2': None}
        
        with chdir(os.path.dirname(mock_requirements_file)):
            names = RequirementsFinder._get_names_cached(mock_requirements_file)
            
            assert set(names) == {'package1', 'package2'}

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

isort/Test4DT_tests/test_isort_deprecated_finders_RequirementsFinder__get_names_cached_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
____________________________ test_get_names_cached _____________________________

mock_requirements_file = '/tmp/pytest-of-joaovitorino/pytest-1/test_get_names_cached0/requirements.txt'

    def test_get_names_cached(mock_requirements_file):
        with patch('isort.deprecated.finders.parse_requirements', autospec=True) as mock_parse:
            # Mock the parse_requirements to return a list of requirements
            mock_parse.return_value = {'package1': None, 'package2': None}
    
            with chdir(os.path.dirname(mock_requirements_file)):
>               names = RequirementsFinder._get_names_cached(mock_requirements_file)

isort/Test4DT_tests/test_isort_deprecated_finders_RequirementsFinder__get_names_cached_0_test_valid_input.py:19: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

cls = <class 'isort.deprecated.finders.RequirementsFinder'>
path = '/tmp/pytest-of-joaovitorino/pytest-1/test_get_names_cached0/requirements.txt'

    @classmethod
    @lru_cache(maxsize=16)
    def _get_names_cached(cls, path: str) -> list[str]:
        result: list[str] = []
    
        with chdir(os.path.dirname(path)):
>           requirements = parse_requirements(Path(path))
E           TypeError: 'NonCallableMagicMock' object is not callable

isort/isort/deprecated/finders.py:337: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_deprecated_finders_RequirementsFinder__get_names_cached_0_test_valid_input.py::test_get_names_cached
============================== 1 failed in 0.11s ===============================
"""