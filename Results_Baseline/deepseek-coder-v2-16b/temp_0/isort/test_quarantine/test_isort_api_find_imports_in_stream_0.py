
# Module: isort.api
# test_find_imports_in_stream.py
from pathlib import Path
from typing import TextIO
from your_module import find_imports_in_stream, Config, DEFAULT_CONFIG, ImportKey  # Added missing import
import pytest

@pytest.fixture
def example_file():
    return """
import sys
import os
from some_module import some_function
from another_module import AnotherClass
class SomeClass:
    def __init__(self):
        pass
"""

@pytest.fixture
def example_file_path(tmpdir, example_file):
    file_path = Path(tmpdir) / 'example.py'
    file_path.write_text(example_file)
    return file_path

def test_find_imports_in_stream_default(example_file_path, capsys):
    with open(str(example_file_path), 'r') as file:  # Changed to string conversion for compatibility
        for imp in find_imports_in_stream(file):
            print(imp)
    captured = capsys.readouterr()
    assert "import sys" in captured.out
    assert "import os" in captured.out
    assert "from some_module import some_function" in captured.out
    assert "from another_module import AnotherClass" in captured.out

def test_find_imports_in_stream_unique(example_file_path, capsys):
    with open(str(example_file_path), 'r') as file:  # Changed to string conversion for compatibility
        for imp in find_imports_in_stream(file, unique=True):
            print(imp)
    captured = capsys.readouterr()
    assert "import sys" in captured.out
    assert "from some_module import some_function" in captured.out
    assert "from another_module import AnotherClass" in captured.out
    # Ensure no duplicates are printed
    lines = captured.out.splitlines()
    unique_imports = {line for line in lines if line.startswith("import")}
    assert len(unique_imports) == 3

def test_find_imports_in_stream_top_only(example_file_path, capsys):
    with open(str(example_file_path), 'r') as file:  # Changed to string conversion for compatibility
        for imp in find_imports_in_stream(file, top_only=True):
            print(imp)
    captured = capsys.readouterr()
    assert "import sys" in captured.out
    assert "import os" not in captured.out
    assert "from some_module import some_function" in captured.out
    assert "from another_module import AnotherClass" in captured.out

def test_find_imports_in_stream_custom_config(example_file_path, capsys):
    custom_config = Config(settings_file="path/to/custom_config.ini")  # Corrected the instantiation
    with open(str(example_file_path), 'r') as file:  # Changed to string conversion for compatibility
        for imp in find_imports_in_stream(file, config=custom_config):
            print(imp)
    captured = capsys.readouterr()
    assert "import sys" in captured.out
    assert "import os" in captured.out
    assert "from some_module import some_function" in captured.out
    assert "from another_module import AnotherClass" in captured.out

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_api_find_imports_in_stream_0
isort/Test4DT_tests/test_isort_api_find_imports_in_stream_0.py:6:0: E0401: Unable to import 'your_module' (import-error)


"""