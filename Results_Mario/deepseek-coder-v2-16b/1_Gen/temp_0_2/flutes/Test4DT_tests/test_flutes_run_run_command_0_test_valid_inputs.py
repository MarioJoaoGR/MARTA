
import pytest
from typing import List, Dict, Optional, Union
import subprocess
import tempfile
from pathlib import Path
from flutes.run import run_command, CommandResult

@pytest.mark.parametrize("args", [["ls", "-l"], "pwd"])
def test_valid_inputs(args):
    result = run_command(args)
    assert isinstance(result, CommandResult)
