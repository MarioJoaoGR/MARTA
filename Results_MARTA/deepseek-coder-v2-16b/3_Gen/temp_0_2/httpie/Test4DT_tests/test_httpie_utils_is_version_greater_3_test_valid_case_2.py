
import unittest
from httpie.utils import is_version_greater

class TestHttpieUtilsIsVersionGreater3TestValidCase2(unittest.TestCase):
    def test_valid_case_2(self):
        self.assertTrue(is_version_greater("1.0", "0.9"))
        self.assertFalse(is_version_greater("1.1", "1.2"))
        self.assertTrue(is_version_greater("2.0.1", "2.0.0"))
        self.assertFalse(is_version_greater("1.0.beta", "1.0.1"))
