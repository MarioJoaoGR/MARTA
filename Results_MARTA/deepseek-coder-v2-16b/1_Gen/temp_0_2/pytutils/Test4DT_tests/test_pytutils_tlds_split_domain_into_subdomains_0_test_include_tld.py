
import pytest
from pytutils.tlds import split_domain_into_subdomains

@pytest.mark.parametrize("domain, expected", [
    ('example.com', ['example.com', 'com']),
    ('sub.example.com', ['sub.example.com', 'example.com', 'com']),
    ('a.b.c.example.com', ['a.b.c.example.com', 'b.c.example.com', 'c.example.com', 'example.com', 'com'])
])
def test_include_tld(domain, expected):
    result = split_domain_into_subdomains(domain, True)
    assert result == expected
