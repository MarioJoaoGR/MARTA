
import pytest
from pathlib import Path
from io import StringIO
from isort.format import show_unified_diff


def test_edge_cases_valid_input_empty_output():
    file_input = "import os\n"
    file_output = ""
    file_path = Path('example.py')
    output_stream = StringIO()

    # Create the example.py file to avoid FileNotFoundError
    with open(file_path, 'w') as f:
        f.write(file_input)

    show_unified_diff(
        file_input=file_input,
        file_output=file_output,
        file_path=file_path,
        output=output_stream,
        color_output=False
    )

    diff_output = output_stream.getvalue()
    assert "@@ -1 +0,0 @@\n-import os\n" in diff_output


def test_no_file_path():
    file_input = "import os\n"
    file_output = "import sys\n"
    output_stream = StringIO()

    show_unified_diff(
        file_input=file_input,
        file_output=file_output,
        file_path=None,
        output=output_stream,
        color_output=False
    )

    diff_output = output_stream.getvalue()
    assert "@@ -1 +1 @@\n-import os\n+import sys\n" in diff_output

def test_color_output():
    file_input = "import os\n"
    file_output = "import sys\n"
    file_path = Path('example.py')
    output_stream = StringIO()

    # Create the example.py file to avoid FileNotFoundError
    with open(file_path, 'w') as f:
        f.write(file_input)

    show_unified_diff(
        file_input=file_input,
        file_output=file_output,
        file_path=file_path,
        output=output_stream,
        color_output=True
    )

    diff_output = output_stream.getvalue()
    assert "\x1b[32m+import sys\n\x1b[0m" in diff_output
    assert "\x1b[31m-import os\n\x1b[0m" in diff_output