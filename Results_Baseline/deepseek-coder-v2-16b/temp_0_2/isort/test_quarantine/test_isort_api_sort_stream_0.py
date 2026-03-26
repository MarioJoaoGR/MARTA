
# Module: isort.api
import pytest
from io import StringIO
from pathlib import Path
from isort.api import sort_stream, Config, DEFAULT_CONFIG
from isort import core
from difflib import unified_diff
from warnings import warn

# Helper function to compare file contents
def read_file(file_path):
    with open(file_path, 'r') as f:
        return f.read()

def test_sort_stream_basic():
    input_content = """import os
import sys
import math"""
    expected_output = """import math
import os
import sys"""
    
    input_stream = StringIO(input_content)
    output_stream = StringIO()
    assert sort_stream(input_stream, output_stream) == True
    assert output_stream.getvalue().strip() == expected_output.strip()

def test_sort_stream_with_file_path():
    input_content = """import sys
import os"""
    with open('temp_test_file.py', 'w') as f:
        f.write(input_content)
    
    output_stream = StringIO()
    assert sort_stream(open('temp_test_file.py'), output_stream, file_path=Path('temp_test_file.py')) == True
    with open('temp_test_file.py', 'r') as f:
        assert f.read().strip() == expected_output.strip()

def test_sort_stream_with_config():
    input_content = """import os
import sys"""
    config = Config(line_length=80)
    input_stream = StringIO(input_content)
    output_stream = StringIO()
    assert sort_stream(input_stream, output_stream, config=config) == True
    assert output_stream.getvalue().strip() == expected_output.strip()

def test_sort_stream_with_show_diff():
    input_content = """import sys
import os"""
    input_stream = StringIO(input_content)
    output_stream = StringIO()
    assert sort_stream(input_stream, output_stream, show_diff=True) == True
    expected_diff = list(unified_diff('import sys\nimport os\n', output_stream.getvalue().strip(), fromfile='original', tofile='sorted'))
    assert ''.join(expected_diff).strip() == ''

def test_sort_stream_with_disregard_skip():
    input_content = """# isort: skip_file
import os
import sys"""
    input_stream = StringIO(input_content)
    output_stream = StringIO()
    assert sort_stream(input_stream, output_stream, disregard_skip=True) == False
    assert output_stream.getvalue().strip() == input_content.strip()

def test_sort_stream_with_raise_on_skip():
    input_content = """# isort: skip_file
import os
import sys"""
    input_stream = StringIO(input_content)
    with pytest.raises(FileSkipComment):
        sort_stream(input_stream, StringIO(), raise_on_skip=True)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_api_sort_stream_0
isort/Test4DT_tests/test_isort_api_sort_stream_0.py:38:35: E0602: Undefined variable 'expected_output' (undefined-variable)
isort/Test4DT_tests/test_isort_api_sort_stream_0.py:47:47: E0602: Undefined variable 'expected_output' (undefined-variable)
isort/Test4DT_tests/test_isort_api_sort_stream_0.py:72:23: E0602: Undefined variable 'FileSkipComment' (undefined-variable)


"""