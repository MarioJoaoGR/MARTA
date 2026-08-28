
import pytest
from sanic.helpers import is_hop_by_hop_header

# Define a private variable for testing purposes
_HOP_BY_HOP_HEADERS = {'connection', 'keep-alive'}

def test_valid_case_1():
    header = "Connection"
    result = is_hop_by_hop_header(header)
    assert result == True, f"Expected True for header '{header}', but got {result}"

def test_valid_case_2():
    header = "Keep-Alive"
    result = is_hop_by_hop_header(header)
    assert result == True, f"Expected True for header '{header}', but got {result}"

def test_invalid_case():
    header = "Content-Length"
    result = is_hop_by_hop_header(header)
    assert result == False, f"Expected False for header '{header}', but got {result}"
