
import pytest
from pytutils.tlds import split_domain_into_subdomains

def test_valid_case_1():
    domain = 'this.is.a.test.skywww.net'
    expected_output = ['this.is.a.test.skywww.net', 'is.a.test.skywww.net', 'a.test.skywww.net', 'test.skywww.net', 'skywww.net']
    
    result = split_domain_into_subdomains(domain)
    
    assert result == expected_output, f"Expected {expected_output}, but got {result}"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
ERROR: usage: __main__.py [options] [file_or_dir] [file_or_dir] [...]
__main__.py: error: unrecognized arguments: --cov=pytutils --cov-report=term --cov-branch --no-cov-on-fail
  inifile: /projects/F202407648IACDCF2/mario/pytutils/pytest.ini
  rootdir: /projects/F202407648IACDCF2/mario/pytutils
"""