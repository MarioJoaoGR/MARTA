
# Module: ansible.module_utils.urls
import pytest
from ansible.module_utils.urls import _dnsname_match, CertificateError

# Test cases for _dnsname_match function

def test_wildcard_not_in_leftmost_label():
    with pytest.raises(CertificateError) as excinfo:
        _dnsname_match('*.example.org', 'host.example.org')
    assert str(excinfo.value) == "wildcard can only be present in the leftmost label: '.example.org'."

def test_multiple_wildcards():
    with pytest.raises(CertificateError) as excinfo:
        _dnsname_match('www.*.example.org', 'WWW.X.EXAMPLE.ORG')
    assert str(excinfo.value) == "too many wildcards in certificate DNS name: 'www.*.example.org'."

def test_no_wildcard():
    result = _dnsname_match('mail.example.com', 'MAIL.EXAMPLE.COM')
    assert result is True

def test_wildcard_matches_one_character():
    result = _dnsname_match('*.example.org', 'host.example.org')
    assert result is True

def test_empty_dn():
    result = _dnsname_match('', 'anyhostname')
    assert result is False

def test_wildcard_without_additional_labels():
    with pytest.raises(CertificateError) as excinfo:
        _dnsname_match('*.example.org', 'host.example.org')
    assert str(excinfo.value) == "sole wildcard without additional labels are not support: '.example.org'."

def test_partial_wildcard_in_leftmost_label():
    with pytest.raises(CertificateError) as excinfo:
        _dnsname_match('www.*.example.org', 'WWW.X.EXAMPLE.ORG')
    assert str(excinfo.value) == "partial wildcards in leftmost label are not supported: 'www.*.example.org'."
