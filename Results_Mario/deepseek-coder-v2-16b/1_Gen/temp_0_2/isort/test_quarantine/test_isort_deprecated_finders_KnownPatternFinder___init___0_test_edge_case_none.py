
import pytest
from isort.deprecated.finders import KnownPatternFinder
from configparser import ConfigParser
import re

@pytest.fixture
def mock_config():
    config = ConfigParser()
    config['section1'] = {'known_patterns': 'pattern1,pattern2'}
    config['section2'] = {'known_patterns': 'pattern3'}
    return config

def test_edge_case_none(mock_config):
    mock_config.set('section1', 'known_patterns', None)
    with pytest.raises(TypeError):
        KnownPatternFinder(mock_config)

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

isort/Test4DT_tests/test_isort_deprecated_finders_KnownPatternFinder___init___0_test_edge_case_none.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_edge_case_none ______________________________

mock_config = <configparser.ConfigParser object at 0x7ff97f7f2150>

    def test_edge_case_none(mock_config):
>       mock_config.set('section1', 'known_patterns', None)

isort/Test4DT_tests/test_isort_deprecated_finders_KnownPatternFinder___init___0_test_edge_case_none.py:15: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/usr/local/lib/python3.11/configparser.py:1221: in set
    self._validate_value_types(option=option, value=value)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <configparser.ConfigParser object at 0x7ff97f7f2150>

    def _validate_value_types(self, *, section="", option="", value=""):
        """Raises a TypeError for non-string values.
    
        The only legal non-string value if we allow valueless
        options is None, so we need to check if the value is a
        string if:
        - we do not allow valueless options, or
        - we allow valueless options but the value is not None
    
        For compatibility reasons this method is not used in classic set()
        for RawConfigParsers. It is invoked in every case for mapping protocol
        access and in ConfigParser.set().
        """
        if not isinstance(section, str):
            raise TypeError("section names must be strings")
        if not isinstance(option, str):
            raise TypeError("option keys must be strings")
        if not self._allow_no_value or value:
            if not isinstance(value, str):
>               raise TypeError("option values must be strings")
E               TypeError: option values must be strings

/usr/local/lib/python3.11/configparser.py:1206: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_deprecated_finders_KnownPatternFinder___init___0_test_edge_case_none.py::test_edge_case_none
============================== 1 failed in 0.13s ===============================
"""