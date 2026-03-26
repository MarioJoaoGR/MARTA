
# Assuming the SortAttempt class is defined in a module named 'isort_main'
from isort.main import SortAttempt

def test_valid_inputs():
    # Test initialization with valid inputs
    attempt = SortAttempt(incorrectly_sorted=True, skipped=False, supported_encoding=True)
    
    # Assertions to check if the attributes are set correctly
    assert attempt.incorrectly_sorted is True
    assert attempt.skipped is False
    assert attempt.supported_encoding is True
