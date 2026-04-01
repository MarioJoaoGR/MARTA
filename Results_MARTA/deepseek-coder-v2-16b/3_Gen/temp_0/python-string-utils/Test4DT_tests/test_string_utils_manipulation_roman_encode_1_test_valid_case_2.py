
# Import necessary modules and functions for testing
from string_utils.manipulation import roman_encode  # Correctly import from the specified module
import pytest

# Define a fixture if needed, but in this case, we are directly using the function under test
@pytest.fixture
def valid_input():
    return '2020'  # Provide an example input for testing

# Write the test case
def test_valid_case_2(valid_input):
    assert roman_encode(valid_input) == 'MMXX'  # Check if the function returns the expected output
