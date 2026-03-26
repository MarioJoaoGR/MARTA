
# Module: isort.main
import json
import os
import sys
from io import TextIOWrapper

import pytest

from isort.main import main


# Example 1: Running the Script with Specific Command Line Arguments
def test_main_with_specific_command_line_arguments():
    argv = ["arg1", "arg2"]
    with pytest.raises(SystemExit) as exc_info:
        main(argv)
    assert exc_info.type == SystemExit