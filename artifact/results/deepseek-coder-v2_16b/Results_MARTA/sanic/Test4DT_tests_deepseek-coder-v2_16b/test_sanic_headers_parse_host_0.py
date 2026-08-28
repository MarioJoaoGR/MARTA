
import re
from typing import Optional, Tuple
import pytest

# Define the regex pattern for matching host and port
_host_re = re.compile(r"^([^:]+)(?::(\d+))?$")

def parse_host(host: str) -> Tuple[Optional[str], Optional[int]]:
    """Split a string in the format of 'host:port' into its hostname and port components."""
    m = _host_re.fullmatch(host)
    if not m:
        return None, None
    host, port = m.groups()
    return (host.lower(), int(port)) if port is not None else (host.lower(), None)

# Test cases for parse_host function
def test_parse_host_valid():
    assert parse_host("example.com:8080") == ('example.com', 8080)
    assert parse_host("192.168.1.1:3306") == ('192.168.1.1', 3306)

def test_parse_host_no_port():
    assert parse_host("example.com") == ('example.com', None)



# Run the tests with pytest
if __name__ == "__main__":
    pytest.main()