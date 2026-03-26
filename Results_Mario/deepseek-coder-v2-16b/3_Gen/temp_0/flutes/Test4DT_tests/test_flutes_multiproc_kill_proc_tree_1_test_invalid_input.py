
import pytest
from unittest.mock import patch
import os
from flutes.multiproc import kill_proc_tree

def test_kill_proc_tree_invalid_input():
    # Test with an invalid PID (e.g., negative number)
    with pytest.raises(ValueError):
        kill_proc_tree(-1)
