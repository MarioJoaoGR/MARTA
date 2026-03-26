
from io import StringIO
from typing import TextIO

import pytest

from isort.core import DEFAULT_CONFIG, Config, process


# Test Case 3: Handling # isort: off comment
def test_process_with_isort_off():
    input_stream = StringIO("# isort: off\nimport os\nimport sys\n")
    output_stream = StringIO()
    result = process(input_stream, output_stream)
    assert not result, "Expected no changes when # isort: off is present"