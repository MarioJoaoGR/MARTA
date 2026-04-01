
from pathlib import Path
from unittest.mock import patch
import pytest
from isort.api import find_imports_in_paths, Config, DEFAULT_CONFIG

@pytest.mark.parametrize("unique", [False, True])
def test_find_imports_in_paths(unique):
    with patch('isort.api.identify') as mock_identify:
        paths = [Path('test_directory')]
        for imp in find_imports_in_paths(paths, unique=unique):
            assert isinstance(imp, mock_identify.Import)
