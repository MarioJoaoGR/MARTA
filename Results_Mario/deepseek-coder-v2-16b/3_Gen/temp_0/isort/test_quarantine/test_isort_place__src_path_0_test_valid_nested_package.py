
import pytest
from isort.place import _src_path
from isort.config import Config
from pathlib import Path
from unittest.mock import Mock

@pytest.fixture
def config():
    cfg = Mock()
    cfg.src_paths = [Path("/myproject/src")]
    cfg.namespace_packages = set()
    cfg.auto_identify_namespace_packages = False
    cfg.supported_extensions = ('.py', '.pyi')
    return cfg

def test_valid_nested_package(config):
    result = _src_path("subpackage.mymodule", config, src_paths=[Path("/myproject/src")])
    assert result == ('FIRSTPARTY', 'Found in one of the configured src_paths: /myproject/src.')

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_place__src_path_0_test_valid_nested_package
isort/Test4DT_tests/test_isort_place__src_path_0_test_valid_nested_package.py:4:0: E0401: Unable to import 'isort.config' (import-error)
isort/Test4DT_tests/test_isort_place__src_path_0_test_valid_nested_package.py:4:0: E0611: No name 'config' in module 'isort' (no-name-in-module)


"""