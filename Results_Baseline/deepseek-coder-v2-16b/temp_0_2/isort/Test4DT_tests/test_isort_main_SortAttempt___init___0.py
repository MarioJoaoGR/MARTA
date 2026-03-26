# Module: isort.main
import pytest

from isort.main import SortAttempt


# Test cases for the SortAttempt class initialization
def test_sort_attempt_default():
    sort_attempt = SortAttempt(incorrectly_sorted=False, skipped=False, supported_encoding=False)
    assert not sort_attempt.incorrectly_sorted
    assert not sort_attempt.skipped
    assert not sort_attempt.supported_encoding

def test_sort_attempt_all_true():
    sort_attempt = SortAttempt(incorrectly_sorted=True, skipped=True, supported_encoding=True)
    assert sort_attempt.incorrectly_sorted
    assert sort_attempt.skipped
    assert sort_attempt.supported_encoding

def test_sort_attempt_all_false():
    sort_attempt = SortAttempt(incorrectly_sorted=False, skipped=False, supported_encoding=False)
    assert not sort_attempt.incorrectly_sorted
    assert not sort_attempt.skipped
    assert not sort_attempt.supported_encoding

def test_sort_attempt_mixed():
    sort_attempt = SortAttempt(incorrectly_sorted=True, skipped=False, supported_encoding=True)
    assert sort_attempt.incorrectly_sorted
    assert not sort_attempt.skipped
    assert sort_attempt.supported_encoding
