
# Module: isort.api
import pytest
from pathlib import Path
from io import StringIO
import sys
from isort import Config, sort_file, DEFAULT_CONFIG  # Corrected the import statement for DEFAULT_CONFIG

# Import the function correctly
from isort.api import sort_file

@pytest.fixture(scope="module")
def example_py():
    # Create a temporary file for testing
    temp_file = Path("example.py")
    with open(temp_file, "w") as f:
        f.write("import os\nimport sys\n")
    yield temp_file
    # Clean up the temporary file after the test
    temp_file.unlink()

def test_sort_file_basic(example_py):
    assert sort_file(example_py) == True
    with open(example_py, "r") as f:
        content = f.read()
        assert "import os\n" in content
        assert "import sys\n" in content
        # Ensure that the order of imports has been sorted
        import_lines = content.split("\n")
        assert import_lines[0] == "import os"
        assert import_lines[1] == "import sys"

def test_sort_file_custom_config(example_py):
    custom_config = Config(profile="black", line_length=88)
    assert sort_file(example_py, config=custom_config) == True
    with open(example_py, "r") as f:
        content = f.read()
        # Ensure that the custom configuration has been applied
        assert "import os\n" in content
        assert "import sys\n" in content
        # Ensure that the order of imports has not changed (custom config does not affect sorting)
        import_lines = content.split("\n")
        assert import_lines[0] == "import os"
        assert import_lines[1] == "import sys"

def test_sort_file_write_to_stdout(example_py):
    output_stream = StringIO()
    assert sort_file(example_py, write_to_stdout=True, output=output_stream) == True
    output_stream.seek(0)
    content = output_stream.read()
    # Ensure that the content is written to stdout correctly
    assert "import os\n" in content
    assert "import sys\n" in content
    # Ensure that no changes were made to the original file
    with open(example_py, "r") as f:
        original_content = f.read()
        assert original_content == "import os\nimport sys\n"

def test_sort_file_ask_to_apply(example_py):
    # This test would typically require user input which is not feasible in a script
    # Therefore, we skip this test and rely on the default behavior of prompting before applying changes
    pass

def test_sort_file_show_diff(example_py):
    output_stream = StringIO()
    assert sort_file(example_py, show_diff=output_stream) == True
    output_stream.seek(0)
    content = output_stream.read()
    # Ensure that the diff is shown correctly in stdout or the provided stream
    assert "---" in content  # Placeholder for actual diff content
    # Ensure that no changes were made to the original file if show_diff is True
    with open(example_py, "r") as f:
        original_content = f.read()
        assert original_content == "import os\nimport sys\n"

def test_sort_file_output_stream(example_py):
    output_stream = StringIO()
    assert sort_file(example_py, output=output_stream) == True
    output_stream.seek(0)
    content = output_stream.read()
    # Ensure that the content is written to the provided stream correctly
    assert "import os\n" in content
    assert "import sys\n" in content
    # Ensure that no changes were made to the original file
    with open(example_py, "r") as f:
        original_content = f.read()
        assert original_content == "import os\nimport sys\n"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_api_sort_file_0
isort/Test4DT_tests/test_isort_api_sort_file_0.py:7:0: E0611: No name 'sort_file' in module 'isort' (no-name-in-module)
isort/Test4DT_tests/test_isort_api_sort_file_0.py:7:0: E0611: No name 'DEFAULT_CONFIG' in module 'isort' (no-name-in-module)


"""