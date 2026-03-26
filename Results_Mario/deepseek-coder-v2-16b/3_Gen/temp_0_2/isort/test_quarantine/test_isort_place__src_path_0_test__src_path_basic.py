
import pytest
from pathlib import Path
from isort.place import _src_path, Config
from typing import Iterable

@pytest.fixture
def config():
    return Config(src_paths=[Path("C:\\path\\to\\project")], namespace_packages={"pkg1", "pkg2"})

def test__src_path_basic(config):
    result = _src_path("mypackage.subpackage", config)
    assert result == (sections.FIRSTPARTY, 'Found in one of the configured src_paths: Path("C:\\path\\to\\project\\mypackage")')

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_place__src_path_0_test__src_path_basic
isort/Test4DT_tests/test_isort_place__src_path_0_test__src_path_basic.py:13:22: E0602: Undefined variable 'sections' (undefined-variable)


"""