
import pytest
from io import StringIO
from isort.api import check_stream, Config

@pytest.mark.parametrize("input_str", [
    "import os\nimport sys"
])
def test_valid_input(input_str):
    input_stream = StringIO(input_str)
    config = Config()
    assert check_stream(input_stream, show_diff=False, config=config) is True
