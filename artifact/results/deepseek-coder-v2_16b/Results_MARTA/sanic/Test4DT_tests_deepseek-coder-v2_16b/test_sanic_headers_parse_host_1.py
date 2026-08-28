
import pytest
from typing import Optional, Tuple
import re

# Define the regex pattern for matching host and port
_host_re = re.compile(r'^(?:(?:[A-Za-z0-9-_]+\.)+[A-Za-z]{2,}|localhost)(?::(\d+))?$')

def parse_host(host: str) -> Tuple[Optional[str], Optional[int]]:
    """Split a string in the format of 'host:port' into its hostname and port components.
    
    This function takes a single argument, `host`, which is expected to be a string representing a host with an optional port number separated by a colon (`:`). The function will attempt to match this string against a regular expression pattern that captures the hostname and port parts. If the input string does not conform to this format, it returns `None` for both the hostname and port.
    
    Parameters:
        host (str): A string containing a hostname optionally followed by a colon and a port number.
        
    Returns:
        Tuple[Optional[str], Optional[int]]: A tuple where the first element is the lowercase hostname, and the second element is the port number if present; otherwise, it returns `None` for both elements if no valid host or port are found in the input string.
    
    Examples:
        >>> parse_host("example.com")
        ('example.com', None)
        
        >>> parse_host("example.com:8080")
        ('example.com', 8080)
        
        >>> parse_host("192.168.1.1:3306")
        ('192.168.1.1', 3306)
        
        >>> parse_host(":8080")
        (None, 8080)
        
        >>> parse_host("example.com:")
        ('example.com', None)
    """
    if host is None or not isinstance(host, str):
        return None, None
    
    m = _host_re.fullmatch(host)
    if not m:
        return None, None
    
    host, port = m.groups()
    return host.lower(), int(port) if port is not None else None

# Test cases for parse_host function



def test_parse_host_invalid_format():
    assert parse_host("notahost") == (None, None), "Expected (None, None) for invalid format"