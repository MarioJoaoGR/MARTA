
import unittest
from httpie.compat import cached_property

class TestCachedPropertyInit(unittest.TestCase):
    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            # Attempt to create an instance of cached_property without passing a function
            cp = cached_property()  # This should raise a TypeError because func is not provided
