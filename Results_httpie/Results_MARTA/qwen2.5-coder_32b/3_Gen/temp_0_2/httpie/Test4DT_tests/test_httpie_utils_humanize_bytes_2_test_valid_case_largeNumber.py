
import unittest
from httpie.utils import humanize_bytes

class TestHumanizeBytes(unittest.TestCase):
    def test_valid_case_largeNumber(self):
        self.assertEqual(humanize_bytes(1), '1 B')
        self.assertEqual(humanize_bytes(1024, precision=1), '1.0 kB')
        self.assertEqual(humanize_bytes(1024 * 123, precision=1), '123.0 kB')
        self.assertEqual(humanize_bytes(1024 * 12342, precision=1), '12.1 MB')
        self.assertEqual(humanize_bytes(1024 * 12342, precision=2), '12.05 MB')
        self.assertEqual(humanize_bytes(1024 * 1234, precision=2), '1.21 MB')
        self.assertEqual(humanize_bytes(1024 * 1234 * 1111, precision=2), '1.31 GB')
        self.assertEqual(humanize_bytes(1024 * 1234 * 1111, precision=1), '1.3 GB')

if __name__ == '__main__':
    unittest.main()
