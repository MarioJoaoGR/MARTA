
import pytest
from pathlib import Path
import logging
from flutes.log import set_log_file, LOGGER, MultiprocessingFileHandler

def test_invalid_path():
    with pytest.raises(FileNotFoundError):
        set_log_file(Path('nonexistent/directory/application.log'))
