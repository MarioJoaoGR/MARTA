
import pytest
from unittest.mock import patch
from pytutils.tlds import split_domain_into_subdomains

@pytest.mark.parametrize("domain, expected", [
    ('this.is.a.test.skywww.net', ['this.is.a.test.skywww.net', 'is.a.test.skywww.net', 'a.test.skywww.net', 'test.skywww.net', 'skywww.net']),
    ('example.com', ['example.com', 'com'])
])
@patch('pytutils.tlds._tldex', autospec=True)
def test_split_domain_into_subdomains(mock_tldextract, domain, expected):
    mock_tldextract.return_value = type('TLDResult', (), {'subdomain': 'this' if 'skywww' not in domain else None, 'domain': 'example' if 'com' not in domain else 'test', 'suffix': 'net' if 'skywww' in domain else 'com'})()
    result = split_domain_into_subdomains(domain)
    assert result == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
ERROR: usage: __main__.py [options] [file_or_dir] [file_or_dir] [...]
__main__.py: error: unrecognized arguments: --cov=pytutils --cov-report=term --cov-branch --no-cov-on-fail
  inifile: /projects/F202407648IACDCF2/mario/pytutils/pytest.ini
  rootdir: /projects/F202407648IACDCF2/mario/pytutils
"""