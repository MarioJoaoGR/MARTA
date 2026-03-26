# Module: isort.api
from itertools import chain
from pathlib import Path
from typing import Any, Iterator

import pytest

from isort import identify
from isort.api import find_imports_in_paths
from isort.settings import DEFAULT_CONFIG, Config

# Assuming the following imports are available in the module:
# from isort import files, _config, find_imports_in_file

@pytest.fixture(params=[Path("dir1"), Path("dir2"), "file3.py"])
def paths_to_search(request):
    return request.param

@pytest.fixture(params=[True, False])
def unique(request):
    return request.param

@pytest.fixture(params=[True, False])
def top_only(request):
    return request.param

def test_find_imports_in_paths_default(paths_to_search, unique, top_only):
    imports = list(find_imports_in_paths([paths_to_search], unique=unique, top_only=top_only))
    assert isinstance(imports, list), "Expected a list of Import objects"
    for imp in imports:
        assert isinstance(imp, identify.Import), f"Expected {identify.Import}, got {type(imp)}"

def test_find_imports_in_paths_custom_config(paths_to_search, unique, top_only):
    custom_config = Config(force_to_top=frozenset({"os", "sys"}))
    imports = list(find_imports_in_paths([paths_to_search], config=custom_config, unique=unique, top_only=top_only))
    assert isinstance(imports, list), "Expected a list of Import objects"
    for imp in imports:
        assert isinstance(imp, identify.Import), f"Expected {identify.Import}, got {type(imp)}"

def test_find_imports_in_paths_no_duplicates(paths_to_search):
    imports = list(find_imports_in_paths([paths_to_search], unique=True))
    assert len(imports) == len(set(str(imp) for imp in imports)), "Expected only unique imports"

def test_find_imports_in_paths_top_only(paths_to_search):
    imports = list(find_imports_in_paths([paths_to_search], top_only=True))
    assert all(isinstance(imp, identify.Import) for imp in imports), "Expected only top-level imports"

def test_find_imports_in_paths_multiple_paths():
    paths = [Path("dir1"), Path("dir2"), "file3.py"]
    imports = list(find_imports_in_paths(paths))
    assert isinstance(imports, list), "Expected a list of Import objects"
    for imp in imports:
        assert isinstance(imp, identify.Import), f"Expected {identify.Import}, got {type(imp)}"
