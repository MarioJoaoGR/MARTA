
import pytest
from apimd.parser import doctest  # Assuming the module is named 'apimd.parser'




def test_doctest_empty():
    doc = ""
    expected_output = ""
    assert doctest(doc) == expected_output, f"Expected: {expected_output}, Got: {doctest(doc)}"

def test_doctest_plaintext():
    doc = "line1\nline2\nline3"
    expected_output = "line1\nline2\nline3"
    assert doctest(doc) == expected_output, f"Expected: {expected_output}, Got: {doctest(doc)}"