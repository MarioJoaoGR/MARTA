
import pytest
from isort.main import SortAttempt

def test_valid_inputs():
    # Creating an instance where the list is sorted incorrectly and some elements are skipped
    sort_attempt = SortAttempt(incorrectly_sorted=True, skipped=True, supported_encoding=False)
    
    # Asserting attributes of the instance
    assert sort_attempt.incorrectly_sorted == True
    assert sort_attempt.skipped == True
    assert sort_attempt.supported_encoding == False
