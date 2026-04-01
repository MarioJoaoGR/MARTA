
# Import the necessary module and any exceptions it might raise
from isort.literal import assignments, AssignmentsFormatMismatch
import pytest

def test_valid_input():
    # Define a sample input string with valid variable assignments
    code = "var1 = value1\nvar2 = value2"
    
    # Call the function and store the result
    result = assignments(code)
    
    # Assert that the result matches the expected output
    assert result == "var1 = value1\nvar2 = value2"

# Add a test for invalid input to ensure the exception is raised correctly
def test_invalid_input():
    # Define an invalid input string without '=' sign
    code = "var1 value1\nvar2 = value2"
    
    # Use pytest.raises to check if the function raises AssignmentsFormatMismatch
    with pytest.raises(AssignmentsFormatMismatch):
        assignments(code)
