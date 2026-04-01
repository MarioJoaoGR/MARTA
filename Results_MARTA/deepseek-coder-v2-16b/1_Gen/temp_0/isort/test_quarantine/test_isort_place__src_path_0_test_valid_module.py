
import pytest
from isort.place import _src_path, Config
from pathlib import Path
from typing import Iterable

@pytest.fixture
def config():
    class ConfigMock(Config):
        def __init__(self):
            self.namespace_packages = set()
            self.auto_identify_namespace_packages = False
            self.supported_extensions = {'.py'}
            self.src_paths = [Path("/myproject/src")]
    return ConfigMock()

def test_valid_module(config):
    result = _src_path("mypackage", config, src_paths=[Path("/myproject/src")])
    assert result == ('FIRSTPARTY', 'Found in one of the configured src_paths: /myproject/src.')

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

isort/Test4DT_tests/test_isort_place__src_path_0_test_valid_module.py E  [100%]

==================================== ERRORS ====================================
_____________________ ERROR at setup of test_valid_module ______________________

    @pytest.fixture
    def config():
        class ConfigMock(Config):
            def __init__(self):
                self.namespace_packages = set()
                self.auto_identify_namespace_packages = False
                self.supported_extensions = {'.py'}
                self.src_paths = [Path("/myproject/src")]
>       return ConfigMock()

isort/Test4DT_tests/test_isort_place__src_path_0_test_valid_module.py:15: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
isort/Test4DT_tests/test_isort_place__src_path_0_test_valid_module.py:11: in __init__
    self.namespace_packages = set()
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <[AttributeError("'ConfigMock' object has no attribute 'known_other'") raised in repr()] ConfigMock object at 0x7ff03390ab50>
name = 'namespace_packages', value = set()

>   ???
E   dataclasses.FrozenInstanceError: cannot assign to field 'namespace_packages'

<string>:4: FrozenInstanceError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR isort/Test4DT_tests/test_isort_place__src_path_0_test_valid_module.py::test_valid_module
=============================== 1 error in 0.09s ===============================
"""