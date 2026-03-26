
import pytest
from isort.main import SortAttempt

@pytest.fixture
def sort_attempt():
    return SortAttempt(incorrectly_sorted=True, skipped=True, supported_encoding=False)

def test_init(sort_attempt):
    assert sort_attempt.incorrectly_sorted == True
    assert sort_attempt.skipped == True
    assert sort_attempt.supported_encoding == False
