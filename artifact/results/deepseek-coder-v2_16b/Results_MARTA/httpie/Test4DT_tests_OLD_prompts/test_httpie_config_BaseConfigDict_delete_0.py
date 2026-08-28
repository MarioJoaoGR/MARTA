
import pytest
from pathlib import Path
from unittest.mock import patch, MagicMock
import errno
from httpie.config import BaseConfigDict



def test_invalid_delete_with_exception():
    with patch('os.unlink', side_effect=OSError(errno.EACCES, 'Permission denied')):
        config = BaseConfigDict(path=Path('/some/directory/config.json'))

        # Simulate saving the file to make it exist before deletion
        with pytest.raises(OSError):
            config.save()