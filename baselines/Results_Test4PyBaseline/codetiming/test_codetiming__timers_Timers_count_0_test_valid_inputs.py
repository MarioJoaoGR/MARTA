
import unittest
from unittest.mock import patch, MagicMock
from codetiming._timers import Timers

class TestTimers(unittest.TestCase):
    def setUp(self):
        self.timers = Timers()

    @patch('codetiming._timers.collections')
    def test_count_valid_inputs(self, mock_collections):
        # Mock the defaultdict to return a list
        mock_defaultdict = MagicMock()
        mock_collections.defaultdict.return_value = mock_defaultdict
        mock_defaultdict.__len__.return_value = 5

        self.timers._timings['example_timer'] = [1, 2, 3, 4, 5]

        count = self.timers.count('example_timer')
        self.assertEqual(count, 5)

    @patch('codetiming._timers.collections')
    def test_apply_valid_inputs(self, mock_collections):
        # Mock the defaultdict to return a list
        mock_defaultdict = MagicMock()
        mock_collections.defaultdict.return_value = mock_defaultdict
        mock_defaultdict.__len__.return_value = 5
        mock_defaultdict.__getitem__.return_value = [1, 2, 3, 4, 5]

        self.timers._timings['example_timer'] = [1, 2, 3, 4, 5]

        result = self.timers.apply(lambda x: sum(x) / len(x), 'example_timer')
        self.assertEqual(result, 3.0)

    @patch('codetiming._timers.collections')
    def test_count_invalid_inputs(self, mock_collections):
        # Mock the defaultdict to return a list
        mock_defaultdict = MagicMock()
        mock_collections.defaultdict.return_value = mock_defaultdict

        with self.assertRaises(KeyError):
            self.timers.count('non_existent_timer')

    @patch('codetiming._timers.collections')
    def test_apply_invalid_inputs(self, mock_collections):
        # Mock the defaultdict to return a list
        mock_defaultdict = MagicMock()
        mock_collections.defaultdict.return_value = mock_defaultdict

        with self.assertRaises(KeyError):
            self.timers.apply(lambda x: sum(x) / len(x), 'non_existent_timer')

if __name__ == '__main__':
    unittest.main()
