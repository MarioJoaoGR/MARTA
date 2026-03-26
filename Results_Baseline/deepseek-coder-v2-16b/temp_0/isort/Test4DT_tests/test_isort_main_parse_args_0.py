
import sys
from typing import Any, Sequence

import pytest

from isort.main import parse_args

# Assuming DEPRECATED_SINGLE_DASH_ARGS and _build_arg_parser are defined elsewhere in the module

def test_parse_args_basic():
    argv = ["--order-by-type", "--trailing-comma", "file1.py", "file2.py"]
    args = parse_args(argv)
    assert isinstance(args, dict), "Expected a dictionary"
    assert "order_by_type" in args, "Expected 'order_by_type' key to be present"