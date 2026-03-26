
from io import StringIO
from typing import TextIO

import pytest

from isort.core import DEFAULT_CONFIG, Config, process


# Test Case 1: Processing a Python file with default settings
def test_process_with_default_settings():
    input_stream = StringIO("""import os\nimport sys\nimport math\n""")
    output_stream = StringIO()
    result = process(input_stream, output_stream)
    assert result is True
    assert output_stream.getvalue().strip() == "import math\nimport os\nimport sys"

# Test Case 2: Processing a custom configuration with skip comments
def test_process_custom_config_with_skip_comments():
    input_stream = StringIO("""# isort: off\nimport os\nimport sys\nimport math\n""")
    output_stream = StringIO()
    custom_config = Config(line_ending='\n', add_imports=['from math import sin'])
    result = process(input_stream, output_stream, raise_on_skip=True, config=custom_config)