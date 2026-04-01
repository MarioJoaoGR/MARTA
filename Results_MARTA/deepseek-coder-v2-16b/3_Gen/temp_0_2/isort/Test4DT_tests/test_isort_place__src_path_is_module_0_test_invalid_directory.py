
import pytest
from pathlib import Path
from unittest.mock import patch
from isort.place import exists_case_sensitive

def _src_path_is_module(src_path: Path, module_name: str) -> bool:
    return (
        module_name == src_path.name and src_path.is_dir() and exists_case_sensitive(str(src_path))
    )

@pytest.mark.parametrize("module_name", ["tests"])
def test_invalid_directory(module_name):
    with patch('isort.place.exists_case_sensitive', return_value=False):
        src_path = Path('non_existent')
        assert not _src_path_is_module(src_path, module_name)
