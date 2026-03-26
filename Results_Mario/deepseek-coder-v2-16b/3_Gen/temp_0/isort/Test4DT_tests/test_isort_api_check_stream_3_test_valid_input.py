
from io import StringIO

import pytest

from isort.api import Config, check_stream


@pytest.mark.parametrize("input_str", [
    "import os\nimport sys"
])
def test_valid_input(input_str):
    input_stream = StringIO(input_str)
    config = Config()
    assert check_stream(input_stream, show_diff=False, config=config) is True
