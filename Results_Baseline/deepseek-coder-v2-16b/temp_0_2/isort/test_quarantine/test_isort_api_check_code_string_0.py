# Module: isort.api
import pytest
from io import StringIO
from pathlib import Path
from isort.api import check_code_string, Config, DEFAULT_CONFIG

# Test cases for check_code_string function

def test_check_code_string_default():
    code = "import os\nimport sys"
    result = check_code_string(code)
    assert result is True, "Expected imports to be correctly sorted by default settings."

def test_check_code_string_with_diff():
    code = "import os\nimport sys"
    output_stream = StringIO()
    result = check_code_string(code, show_diff=output_stream)
    assert result is True, "Expected imports to be correctly sorted even when showing diff."
    output_stream.seek(0)  # Reset the stream position for reading
    diff_content = output_stream.read()
    assert len(diff_content) == 0, "Expected no diff content as imports are already correct."

def test_check_code_string_with_custom_extension():
    code = "import os\nimport sys"
    result = check_code_string(code, extension="txt")
    assert result is True, "Expected imports to be correctly sorted regardless of file extension."

def test_check_code_string_with_config_override():
    custom_config = Config()  # Assuming this creates a valid Config instance
    code = "import os\nimport sys"
    result = check_code_string(code, config=custom_config)
    assert result is True, "Expected imports to be correctly sorted with overridden configuration."

def test_check_code_string_with_disregard_skip():
    code = "import os\nimport sys"
    result = check_code_string(code, disregard_skip=True)
    assert result is True, "Expected imports to be correctly sorted ignoring skip settings."

def test_check_code_string_with_file_path():
    code = "import os\nimport sys"
    file_path = Path("example.py")
    result = check_code_string(code, file_path=file_path)
    assert result is True, "Expected imports to be correctly sorted with a specified file path."

def test_check_code_string_with_show_diff_true():
    code = "import os\nimport sys"
    output_stream = StringIO()
    result = check_code_string(code, show_diff=True)
    assert result is True, "Expected imports to be correctly sorted when show_diff is set to True."
    output_stream.seek(0)  # Reset the stream position for reading
    diff_content = output_stream.read()
    assert len(diff_content) == 0, "Expected no diff content as imports are already correct."
