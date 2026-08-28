
from pathlib import Path
from typing import Iterable, Optional
from py_backwards.files import get_input_output_paths, InputOutput, InvalidInputOutput, InputDoesntExists
import pytest

# Test case 1: Basic call with absolute paths

# Test case 2: Using a root directory with relative input path

# Test case 3: Handling input as directory and output as file

# Test case 4: Handling input as file and output as directory

# Test case 5: InvalidInputOutput raised when input ends with '.py' but output does not

# Test case 6: InputDoesntExists raised when input path does not exist
def test_get_input_output_paths_input_doesnt_exist():
    input_path = Path('non_existent/input')
    output_path = Path('D:/outputs/results.txt')
    with pytest.raises(InputDoesntExists):
        list(get_input_output_paths(str(input_path), str(output_path), None))