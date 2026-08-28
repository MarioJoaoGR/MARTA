# Module: sanic.headers
import pytest
from typing import Optional

class Options:
    pass  # Placeholder for actual Options class definition

def parse_xforwarded(headers, config) -> Optional[Options]:
    """Parse traditional proxy headers."""
    real_ip_header = config.REAL_IP_HEADER
    proxies_count = config.PROXIES_COUNT
    addr = real_ip_header and headers.get(real_ip_header)
    if not addr and proxies_count:
        assert proxies_count > 0
        try:
            # Combine, split and filter multiple headers' entries
            forwarded_for = headers.getall(config.FORWARDED_FOR_HEADER)
            proxies = [
                p
                for p in (
                    p.strip() for h in forwarded_for for p in h.split(",")
                )
                if p
            ]
            addr = proxies[-proxies_count]
        except (KeyError, IndexError):
            pass
    # No processing of other headers if no address is found
    if not addr:
        return None

    def options():
        yield "for", addr
        for key, header in (
            ("proto", "x-scheme"),
            ("proto", "x-forwarded-proto"),  # Overrides X-Scheme if present
            ("host", "x-forwarded-host"),
            ("port", "x-forwarded-port"),
            ("path", "x-forwarded-path"),
        ):
            yield key, headers.get(header)

    return fwd_normalize(options())

# Test cases for parse_xforwarded function
def test_parse_xforwarded_full_config():
    headers = {'X-Real-IP': '192.168.1.1', 'X-Forwarded-For': 'client1, 172.16.0.1, client3'}
    config = {
        'REAL_IP_HEADER': 'X-Real-IP',
        'FORWARDED_FOR_HEADER': 'X-Forwarded-For',
        'PROXIES_COUNT': 2
    }
    result = parse_xforwarded(headers, config)
    assert result == {'by': '192.168.1.1', 'for': '172.16.0.1', 'host': None, 'proto': 'http', 'port': 80, 'path': None}

def test_parse_xforwarded_default_config():
    headers = {'X-Forwarded-For': 'client1, client2, client3'}
    # Assuming default config is set up to handle this scenario
    result = parse_xforwarded(headers)
    assert result == {'by': None, 'for': 'client1', 'host': None, 'proto': None, 'port': 80, 'path': None}

def test_parse_xforwarded_no_config():
    headers = {}
    config = {
        'REAL_IP_HEADER': '',
        'FORWARDED_FOR_HEADER': 'X-Forwarded-For',
        'PROXIES_COUNT': 2
    }
    result = parse_xforwarded(headers, config)
    assert result is None

def test_parse_xforwarded_no_real_ip():
    headers = {'X-Forwarded-For': 'client1, client2, client3'}
    config = {
        'REAL_IP_HEADER': '',
        'FORWARDED_FOR_HEADER': 'X-Forwarded-For',
        'PROXIES_COUNT': 2
    }
    result = parse_xforwarded(headers, config)
    assert result == {'by': None, 'for': 'client1', 'host': None, 'proto': None, 'port': 80, 'path': None}

def test_parse_xforwarded_invalid_config():
    headers = {'X-Real-IP': '192.168.1.1', 'X-Forwarded-For': 'client1, 172.16.0.1, client3'}
    config = {
        'REAL_IP_HEADER': 'X-Real-IP',
        'FORWARDED_FOR_HEADER': 'X-Forwarded-For',
        'PROXIES_COUNT': -1  # Invalid value for PROXIES_COUNT
    }
    with pytest.raises(AssertionError):
        parse_xforwarded(headers, config)
