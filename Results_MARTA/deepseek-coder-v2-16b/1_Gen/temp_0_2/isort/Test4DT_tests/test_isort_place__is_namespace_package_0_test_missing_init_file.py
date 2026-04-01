
import pytest
from pathlib import Path
from unittest.mock import patch
from isort.place import _is_namespace_package

@pytest.mark.parametrize("path, src_extensions", [
    (Path('non_existent_directory'), frozenset({'py', 'pyi'}))
])
def test_missing_init_file(path, src_extensions):
    with patch('isort.place._is_package', return_value=False):
        assert not _is_namespace_package(path, src_extensions)
