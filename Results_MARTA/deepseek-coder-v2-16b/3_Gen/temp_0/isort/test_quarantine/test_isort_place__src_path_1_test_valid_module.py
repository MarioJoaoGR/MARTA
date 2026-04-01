
import pytest
from isort.place import _src_path, Config
from pathlib import Path
from typing import Iterable

@pytest.fixture
def config():
    class MockConfig(Config):
        def __init__(self):
            self.src_paths = [Path("/myproject/src")]
            self.namespace_packages = set()
            self.auto_identify_namespace_packages = False
            self.supported_extensions = {".py"}
    
    return MockConfig()

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

isort/Test4DT_tests/test_isort_place__src_path_1_test_valid_module.py E  [100%]

==================================== ERRORS ====================================
_____________________ ERROR at setup of test_valid_module ______________________

    @pytest.fixture
    def config():
        class MockConfig(Config):
            def __init__(self):
                self.src_paths = [Path("/myproject/src")]
                self.namespace_packages = set()
                self.auto_identify_namespace_packages = False
                self.supported_extensions = {".py"}
    
>       return MockConfig()

isort/Test4DT_tests/test_isort_place__src_path_1_test_valid_module.py:16: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
isort/Test4DT_tests/test_isort_place__src_path_1_test_valid_module.py:11: in __init__
    self.src_paths = [Path("/myproject/src")]
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <[AttributeError("'MockConfig' object has no attribute 'known_other'") raised in repr()] MockConfig object at 0x7fe75df2b950>
name = 'src_paths', value = [PosixPath('/myproject/src')]

>   ???
E   dataclasses.FrozenInstanceError: cannot assign to field 'src_paths'

<string>:4: FrozenInstanceError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR isort/Test4DT_tests/test_isort_place__src_path_1_test_valid_module.py::test_valid_module
=============================== 1 error in 0.13s ===============================
"""