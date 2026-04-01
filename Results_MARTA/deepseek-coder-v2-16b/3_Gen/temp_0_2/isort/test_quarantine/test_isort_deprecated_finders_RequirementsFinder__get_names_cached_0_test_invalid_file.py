
import os
from pathlib import Path
from isort.deprecated.finders import RequirementsFinder
import pytest
from unittest.mock import patch, MagicMock

@pytest.mark.parametrize("non_existent_path", ["nonexistentfile.txt", "nonexistentdir/nonexistentfile.txt"])
def test_invalid_file(non_existent_path):
    with pytest.raises(FileNotFoundError):
        RequirementsFinder._get_names_cached(non_existent_path)
