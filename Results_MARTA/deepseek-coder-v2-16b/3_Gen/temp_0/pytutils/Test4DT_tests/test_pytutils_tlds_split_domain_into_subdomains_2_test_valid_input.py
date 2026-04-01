
import pytest
from pytutils.tlds import split_domain_into_subdomains

def test_valid_input():
    # Test with a valid domain
    assert split_domain_into_subdomains('this.is.a.test.skywww.net') == [
        'this.is.a.test.skywww.net', 
        'is.a.test.skywww.net', 
        'a.test.skywww.net', 
        'test.skywww.net', 
        'skywww.net'
    ]
    
    # Test with a valid domain and split_tld=True
    assert split_domain_into_subdomains('example.com', True) == [
        'example.com', 
        'com'
    ]
