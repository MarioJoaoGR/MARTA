
import pytest
from isort.place import _src_path, Config
from pathlib import Path
from typing import Iterable

# Mocking the sections and config for testing purposes
class SectionsMock:
    FIRSTPARTY = 'sections.FIRSTPARTY'

class ConfigMock(Config):
    def __init__(self):
        super().__init__()
        self.src_paths = [Path("mocked_source_path")]
        self.namespace_packages = {"mypackage"}
        self.auto_identify_namespace_packages = True
        self.supported_extensions = {".py"}

@pytest.fixture
def config():
    return ConfigMock()

@pytest.fixture
def sections():
    return SectionsMock()

def test_valid_input(config, sections):
    result = _src_path("mypackage.modulename", config)
    assert result == (sections.FIRSTPARTY, "Found in one of the configured src_paths: mocked_source_path.")

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

isort/Test4DT_tests/test_isort_place__src_path_0_test_valid_input.py E   [100%]

==================================== ERRORS ====================================
______________________ ERROR at setup of test_valid_input ______________________

    @pytest.fixture
    def config():
>       return ConfigMock()

isort/Test4DT_tests/test_isort_place__src_path_0_test_valid_input.py:21: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
isort/Test4DT_tests/test_isort_place__src_path_0_test_valid_input.py:14: in __init__
    self.src_paths = [Path("mocked_source_path")]
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = ConfigMock(py_version='py3', force_to_top=frozenset(), skip=frozenset({'__pypackages__', '.eggs', 'node_modules', '.bz...ge}', format_success='{success}: {message}', sort_order='natural', sort_reexports=False, split_on_trailing_comma=False)
name = 'src_paths', value = [PosixPath('mocked_source_path')]

>   ???
E   dataclasses.FrozenInstanceError: cannot assign to field 'src_paths'

<string>:4: FrozenInstanceError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR isort/Test4DT_tests/test_isort_place__src_path_0_test_valid_input.py::test_valid_input
=============================== 1 error in 0.10s ===============================
"""