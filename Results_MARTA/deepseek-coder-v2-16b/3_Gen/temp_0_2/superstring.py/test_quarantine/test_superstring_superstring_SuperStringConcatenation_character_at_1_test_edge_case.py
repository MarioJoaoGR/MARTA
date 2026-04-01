
import pytest
from unittest import mock
from superstring.superstring import SuperStringConcatenation

class TestSuperStringConcatenation:
    @mock.patch('superstring.superstring.SuperStringBase')  # Assuming SuperStringBase is the base class for left and right strings
    def test_character_at_out_of_bounds_left(self, MockSuperStringBase):
        # Arrange
        mock_left = MockSuperStringBase.return_value
        mock_right = MockSuperStringBase.return_value
        mock_left.__getitem__.side_effect = lambda index: "left"[index]  # Mocking the __getitem__ method for left string
        mock_right.__getitem__.side_effect = lambda index: "right"[index - len("left")]  # Mocking the __getitem__ method for right string
        
        ssc = SuperStringConcatenation(mock_left, mock_right)
        
        # Act & Assert
        with pytest.raises(IndexError):
            ssc.character_at(10)  # Index out of bounds for both strings combined

    @mock.patch('superstring.superstring.SuperStringBase')  # Assuming SuperStringBase is the base class for left and right strings
    def test_character_at_valid_index(self, MockSuperStringBase):
        # Arrange
        mock_left = MockSuperStringBase.return_value
        mock_right = MockSuperStringBase.return_value
        mock_left.__getitem__.side_effect = lambda index: "left"[index]  # Mocking the __getitem__ method for left string
        mock_right.__getitem__.side_effect = lambda index: "right"[index - len("left")]  # Mocking the __getitem__ method for right string
        
        ssc = SuperStringConcatenation(mock_left, mock_right)
        
        # Act
        result = ssc.character_at(5)
        assert result == "left"[5]  # Assert that the character at index 5 in left is returned

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/superstring.py
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringConcatenation_character_at_1_test_edge_case.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
______ TestSuperStringConcatenation.test_character_at_out_of_bounds_left _______

self = <Test4DT_tests.test_superstring_superstring_SuperStringConcatenation_character_at_1_test_edge_case.TestSuperStringConcatenation object at 0x7f6b1b3a29d0>
MockSuperStringBase = <MagicMock name='SuperStringBase' id='140097989613840'>

    @mock.patch('superstring.superstring.SuperStringBase')  # Assuming SuperStringBase is the base class for left and right strings
    def test_character_at_out_of_bounds_left(self, MockSuperStringBase):
        # Arrange
        mock_left = MockSuperStringBase.return_value
        mock_right = MockSuperStringBase.return_value
        mock_left.__getitem__.side_effect = lambda index: "left"[index]  # Mocking the __getitem__ method for left string
        mock_right.__getitem__.side_effect = lambda index: "right"[index - len("left")]  # Mocking the __getitem__ method for right string
    
        ssc = SuperStringConcatenation(mock_left, mock_right)
    
        # Act & Assert
        with pytest.raises(IndexError):
>           ssc.character_at(10)  # Index out of bounds for both strings combined

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringConcatenation_character_at_1_test_edge_case.py:19: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <superstring.superstring.SuperStringConcatenation object at 0x7f6b1ae7ad50>
index = 10

    def character_at(self, index):
        left_len = self._left.length()
>       if index < left_len:
E       TypeError: '<' not supported between instances of 'int' and 'MagicMock'

superstring.py/superstring/superstring.py:104: TypeError
__________ TestSuperStringConcatenation.test_character_at_valid_index __________

self = <Test4DT_tests.test_superstring_superstring_SuperStringConcatenation_character_at_1_test_edge_case.TestSuperStringConcatenation object at 0x7f6b1ae78cd0>
MockSuperStringBase = <MagicMock name='SuperStringBase' id='140097994743056'>

    @mock.patch('superstring.superstring.SuperStringBase')  # Assuming SuperStringBase is the base class for left and right strings
    def test_character_at_valid_index(self, MockSuperStringBase):
        # Arrange
        mock_left = MockSuperStringBase.return_value
        mock_right = MockSuperStringBase.return_value
        mock_left.__getitem__.side_effect = lambda index: "left"[index]  # Mocking the __getitem__ method for left string
        mock_right.__getitem__.side_effect = lambda index: "right"[index - len("left")]  # Mocking the __getitem__ method for right string
    
        ssc = SuperStringConcatenation(mock_left, mock_right)
    
        # Act
>       result = ssc.character_at(5)

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringConcatenation_character_at_1_test_edge_case.py:32: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <superstring.superstring.SuperStringConcatenation object at 0x7f6b1bde10d0>
index = 5

    def character_at(self, index):
        left_len = self._left.length()
>       if index < left_len:
E       TypeError: '<' not supported between instances of 'int' and 'MagicMock'

superstring.py/superstring/superstring.py:104: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringConcatenation_character_at_1_test_edge_case.py::TestSuperStringConcatenation::test_character_at_out_of_bounds_left
FAILED superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringConcatenation_character_at_1_test_edge_case.py::TestSuperStringConcatenation::test_character_at_valid_index
============================== 2 failed in 0.06s ===============================
"""