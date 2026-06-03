
import unittest
from codetiming import Timer
from unittest.mock import patch, MagicMock

class TestTimersClear(unittest.TestCase):
    @patch('codetiming._timers.Timers')
    def test_clear(self, MockTimers):
        # Arrange
        timers = MockTimers()
        timers._timings['example_timer'] = [1.0, 2.0, 3.0]
        
        # Act
        timers.clear()
        
        # Assert
        self.assertEqual(len(timers._timings['example_timer']), 0)
