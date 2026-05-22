
import pytest
from unittest.mock import patch
import tempfile
from pathlib import Path

def _check_status(env):
    # This function is used only for the testing (test_update_warnings).
    # Since we don't want to trigger the fetch_updates (which would interact
    # # with real world resources), we'll only trigger this pseudo task
    # and check whether the STATUS_FILE is created or not.
    import tempfile
    from pathlib import Path

    status_file = Path(tempfile.gettempdir()) / env['STATUS_FILE']
    status_file.touch()

def test_none_input():
    with pytest.raises(TypeError):
        _check_status(None)
