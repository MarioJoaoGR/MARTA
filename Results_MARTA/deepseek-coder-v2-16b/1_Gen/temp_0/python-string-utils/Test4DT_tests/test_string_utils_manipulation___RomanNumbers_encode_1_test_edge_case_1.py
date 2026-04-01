
import pytest
from string_utils.manipulation import __RomanNumbers

def test_edge_case_1():
    # Test encoding 1, which should return 'I'
    assert __RomanNumbers.encode(1) == 'I'

# Run the test with pytest:
# pytest -v path/to/your/test_file.py::test_edge_case_1
