
import unittest
from unittest.mock import patch
from httpie.output.ui.palette import PieColor

def boldify(color: 'PieColor') -> str:
    return f'bold {color}'

class TestHttpieOutputUiPaletteBoldify0TestValidInput(unittest.TestCase):
    
    @patch('httpie.output.ui.palette.PieColor')
    def test_valid_input(self, MockPieColor):
        # Arrange
        color = 'red'
        expected_output = 'bold red'
        
        # Act
        result = boldify(color)
        
        # Assert
        self.assertEqual(result, expected_output)
