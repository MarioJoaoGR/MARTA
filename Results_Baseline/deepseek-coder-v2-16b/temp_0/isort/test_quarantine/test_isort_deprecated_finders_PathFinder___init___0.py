
# Module: isort.deprecated.finders
# test_pathfinder.py
from your_module import Config, PathFinder
import os
import glob
import pytest

@pytest.fixture
def config():
    return Config()

@pytest.fixture
def path_finder(config):
    return PathFinder(config=config, path="your/project/root")

# Test initialization with default path
def test_init_default_path(config):
    pf = PathFinder(config=config)
    assert pf.paths == ['.', 'src']

# Test initialization with custom path
def test_init_custom_path(config):
    pf = PathFinder(config=config, path="/custom/project/root")
    assert pf.paths == ['/custom/project/root', '/custom/project/root/src']

# Test virtual environment paths are added correctly
def test_virtual_env_paths(config):
    os.environ['VIRTUAL_ENV'] = "/path/to/venv"
    pf = PathFinder(config=config, path="your/project/root")
    assert rf"/path/to/venv/lib/python*/site-packages" in pf.paths
    assert f"/path/to/venv/src" in pf.paths

# Test conda environment paths are added correctly
def test_conda_env_paths(config):
    os.environ['CONDA_PREFIX'] = "/path/to/conda_env"
    pf = PathFinder(config=config, path="your/project/root")
    assert rf"/path/to/conda_env/lib/python*/site-packages" in pf.paths
    assert f"/path/to/conda_env/src" in pf.paths

# Test standard library paths are added correctly
def test_stdlib_paths(config):
    import sys
    sys.path.append("/system/path")
    pf = PathFinder(config=config, path="your/project/root")
    assert "/system/path" in pf.paths

# Test case-insensitive paths on Windows are handled correctly
def test_case_insensitive_paths():
    if os.name == 'nt':  # Only run this test on Windows
        import sysconfig
        sysconfig.get_paths = lambda: {'stdlib': r'C:\Python\Lib'}
        pf = PathFinder(config=Config(), path="your/project/root")
        assert os.path.normcase(sysconfig.get_paths()["stdlib"]) in pf.paths

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_deprecated_finders_PathFinder___init___0
isort/Test4DT_tests/test_isort_deprecated_finders_PathFinder___init___0.py:4:0: E0401: Unable to import 'your_module' (import-error)


"""