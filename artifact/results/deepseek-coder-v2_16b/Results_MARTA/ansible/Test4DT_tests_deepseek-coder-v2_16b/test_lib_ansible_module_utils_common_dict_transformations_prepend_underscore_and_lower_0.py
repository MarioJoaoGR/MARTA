
import re
import pytest
from prepend_underscore import prepend_underscore_and_lower  # Assuming the function is in a module named prepend_underscore

# Test Scenario 1: Valid Case
def test_valid_case():
    pattern = r'[A-Z]+'
    text = 'Hello World!'
    match = re.search(pattern, text)
    assert match is not None
    modified_match = prepend_underscore_and_lower(match)
    assert modified_match == '_hello'

# Test Scenario 2: Edge Case with None Input
def test_edge_case():
    m = None
    with pytest.raises(AttributeError):
        prepend_underscore_and_lower(m)

# Test Scenario 3: Error Case with Non-String Input
def test_error_case():
    m = 12345
    with pytest.raises(TypeError):
        prepend_underscore_and_lower(m)
