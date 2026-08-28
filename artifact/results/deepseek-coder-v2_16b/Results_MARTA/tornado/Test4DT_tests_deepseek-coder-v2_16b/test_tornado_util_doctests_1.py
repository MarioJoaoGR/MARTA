
import pytest
import unittest
import doctest
from tornado.util import doctests

def test_doctests():
    suite = doctests()
    result = unittest.TestResult()
    suite.run(result)
    assert len(result.errors) == 0, "Some errors occurred during the doctests."
    assert len(result.failures) == 0, "Some failures occurred during the doctests."

if __name__ == "__main__":
    pytest.main()
