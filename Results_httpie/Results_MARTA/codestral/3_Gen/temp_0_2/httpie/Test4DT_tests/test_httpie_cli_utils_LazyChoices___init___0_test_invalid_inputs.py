
import unittest
from httpie.cli.utils import LazyChoices
from typing import Callable, Iterable, Optional

class TestLazyChoicesInit(unittest.TestCase):
    
    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            # Passing an invalid type for getter should raise a TypeError
            LazyChoices(getter=42)  # Invalid because 42 is not callable
