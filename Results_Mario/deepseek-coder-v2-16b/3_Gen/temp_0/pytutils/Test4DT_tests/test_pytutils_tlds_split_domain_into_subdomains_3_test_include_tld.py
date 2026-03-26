
import pytest
from tldextract import TLDExtract
from itertools import accumulate

# Mocking the ensure_decoded_text function since it's not defined in the provided code snippet
def ensure_decoded_text(domain):
    return domain

# Mocking the _tldex variable initialization
_tldex = None

# Function to be tested
def split_domain_into_subdomains(domain, split_tld=False):
    """
    Splits a domain into its subdomains by walking up the hierarchy.

    Parameters:
        domain (str): The fully qualified domain name (FQDN) to be split.
        split_tld (bool, optional): If True, includes the top-level domain in the result; otherwise, it is excluded. Default is False.

    Returns:
        list of str: A list of subdomains starting from the most specific subdomain to the root domain.
    """
    import tldextract

    # Requires unicode
    domain = ensure_decoded_text(domain)

    # Do not request latest TLS list on init == suffix_list_urls=False
    global _tldex
    if _tldex is None:
        _tldex = tldextract.TLDExtract(suffix_list_urls=False)

    tx = _tldex(domain)

    domains = []
    if tx.subdomain:
        domains.extend(tx.subdomain.split('.'))

    # tx.registered_domain returns only if domain AND suffix are not none
    # There are cases where we have domain and not suffix; ie short hostnames
    registered_domain = [tx.domain]
    if tx.suffix:
        registered_domain.append(tx.suffix)

    if split_tld:
        domains.extend(registered_domain)
    else:
        domains.append('.'.join(registered_domain))

    # Musical chairs. Change places!
    domains.reverse()

    def join_dom(a, b):
        return '.'.join([b, a])

    # Take each part and add it to the previous part, returning all results
    domains = list(accumulate(domains, func=join_dom))
    # Change places!
    domains.reverse()

    return domains

# Test function for test_include_tld
@pytest.mark.parametrize("domain, expected", [
    ('example.com', ['example.com', 'com']),
    ('sub.example.com', ['sub.example.com', 'example.com', 'com']),
    ('a.b.c.example.com', ['a.b.c.example.com', 'b.c.example.com', 'c.example.com', 'example.com', 'com'])
])
def test_include_tld(domain, expected):
    assert split_domain_into_subdomains(domain, True) == expected
