
import pytest
from unittest.mock import patch
from thonny.jedi_utils import get_script_completions





def test_get_script_completions_without_row_column():
    source = "def main():\n    pass"
    filename = "script.py"
    with patch('thonny.jedi_utils._using_older_jedi', return_value=False):
        completions = get_script_completions(source, row=None, column=None, filename=filename)
        assert len(completions) > 0, "Expected at least one completion"