
import os
from unittest.mock import patch

import pytest

from isort.exceptions import InvalidSettingsPath


def test_invalid_input():
    invalid_path = 'non_existent_file.cfg'
    with pytest.raises(InvalidSettingsPath):
        raise InvalidSettingsPath(invalid_path)
