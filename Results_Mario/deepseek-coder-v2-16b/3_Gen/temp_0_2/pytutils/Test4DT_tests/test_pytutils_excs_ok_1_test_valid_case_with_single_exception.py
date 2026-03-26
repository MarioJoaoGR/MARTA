
import pytest
from pytutils.excs import ok
from unittest import TestCase

class TestOk(TestCase):
    def test_ok(self):
        with self.assertRaises(ZeroDivisionError):
            with ok():
                print(1 / 0)
