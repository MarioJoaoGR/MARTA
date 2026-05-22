
import unittest
from httpie.context import Environment
from unittest.mock import patch, MagicMock
import sys

class TestEnvironmentInit(unittest.TestCase):
    def test_invalid_inputs(self):
        with self.assertRaises(AssertionError):
            # Passing an invalid argument should raise an AssertionError
            Environment(invalid_arg='invalid')
