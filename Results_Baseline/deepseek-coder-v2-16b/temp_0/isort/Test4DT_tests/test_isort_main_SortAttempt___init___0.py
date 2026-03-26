# Module: isort.main
import pytest

from isort.main import SortAttempt


# Test Case 1: Default Initialization with Correctly Sorted List
def test_default_initialization():
    attempt = SortAttempt(incorrectly_sorted=False, skipped=False, supported_encoding=True)
    assert not attempt.incorrectly_sorted, "Expected incorrectly_sorted to be False"
    assert not attempt.skipped, "Expected skipped to be False"
    assert attempt.supported_encoding, "Expected supported_encoding to be True"

# Test Case 2: Initialization with Incorrect Sorting and Skipped Process
def test_initialization_with_incorrect_sorting_and_skipped():
    attempt = SortAttempt(incorrectly_sorted=True, skipped=True, supported_encoding=False)
    assert attempt.incorrectly_sorted, "Expected incorrectly_sorted to be True"
    assert attempt.skipped, "Expected skipped to be True"
    assert not attempt.supported_encoding, "Expected supported_encoding to be False"

# Test Case 3: Initialization with Unsupported Encoding
def test_initialization_with_unsupported_encoding():
    attempt = SortAttempt(incorrectly_sorted=False, skipped=False, supported_encoding=False)
    assert not attempt.incorrectly_sorted, "Expected incorrectly_sorted to be False"
    assert not attempt.skipped, "Expected skipped to be False"
    assert not attempt.supported_encoding, "Expected supported_encoding to be False"

# Test Case 4: Initialization with Unsupported Encoding and Incorrect Sorting
def test_initialization_with_unsupported_encoding_and_incorrect_sorting():
    attempt = SortAttempt(incorrectly_sorted=True, skipped=False, supported_encoding=False)
    assert attempt.incorrectly_sorted, "Expected incorrectly_sorted to be True"
    assert not attempt.skipped, "Expected skipped to be False"
    assert not attempt.supported_encoding, "Expected supported_encoding to be False"
