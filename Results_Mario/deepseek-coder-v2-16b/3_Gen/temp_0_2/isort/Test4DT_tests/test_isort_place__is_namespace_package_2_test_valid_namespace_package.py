
import pytest
from pathlib import Path
from isort.place import _is_namespace_package

@pytest.fixture
def src_extensions():
    return frozenset({"py", "pyi"})

@pytest.mark.parametrize(
    "path, expected",
    [
        (Path("C:\\path\\to\\namespace_pkg"), True),
        (Path("C:\\path\\to\\non_namespace_pkg"), False),
        (Path("/Users/username/project/mynsdir"), True),
    ],
)
def test_is_namespace_package(tmp_path, path, expected, src_extensions):
    # Create a mock directory structure for testing
    namespace_pkg = tmp_path / "namespace_pkg"
    non_namespace_pkg = tmp_path / "non_namespace_pkg"
    mynsdir = tmp_path / "mynsdir"
    
    if not path.is_dir():
        pytest.skip("Path is not a directory")
    
    # Create the necessary files and directories for testing
    namespace_pkg.mkdir()
    (namespace_pkg / "__init__.py").touch()
    
    non_namespace_pkg.mkdir()
    (non_namespace_pkg / "setup.cfg").touch()
    
    mynsdir.mkdir()
    
    # Test the function with different paths
    assert _is_namespace_package(path, src_extensions) == expected
