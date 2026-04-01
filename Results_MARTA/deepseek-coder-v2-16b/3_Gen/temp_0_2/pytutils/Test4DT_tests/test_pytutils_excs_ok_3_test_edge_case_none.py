
import pytest
from pytutils.excs import ok
from unittest import TestCase

class TestOk(TestCase):
    def test_ok(self):
        with self.assertRaises(TypeError):
            with ok(None):  # None is not an exception, so this should raise TypeError immediately
                raise TypeError('This is a test error')
