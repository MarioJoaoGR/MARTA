
import pytest
from pathlib import Path
from py_backwards.files import get_input_output_paths, InputOutput, InvalidInputOutput, InputDoesntExists




def test_error_case_3():
    with pytest.raises(InputDoesntExists):
        list(get_input_output_paths('non_existent_input', 'D:/outputs/', 'C:/root'))