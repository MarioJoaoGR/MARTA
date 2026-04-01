
import pytest
from isort.settings import Config

@pytest.fixture
def config():
    return Config()

def test_is_supported_filetype(config):
    # Test valid file extensions
    assert config.is_supported_filetype("test.py") == True
    assert config.is_supported_filetype("test.PY") == True
    
    # Test blocked file extensions
    assert config.is_supported_filetype("test.java") == False
    
    # Test editor backup files
    assert config.is_supported_filetype("test.py~") == False
    
    # Test special file types (FIFO)
    with pytest.raises(OSError):  # Mocking the OSError for a FIFO file
        config.is_supported_filetype("test.fifo")

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

isort/Test4DT_tests/test_isort_settings_Config_is_supported_filetype_3_test_valid_case.py F [100%]

=================================== FAILURES ===================================
__________________________ test_is_supported_filetype __________________________

config = Config(py_version='py3', force_to_top=frozenset(), skip=frozenset({'.eggs', '.venv', '.svn', '.mypy_cache', 'venv', '_...ge}', format_success='{success}: {message}', sort_order='natural', sort_reexports=False, split_on_trailing_comma=False)

    def test_is_supported_filetype(config):
        # Test valid file extensions
        assert config.is_supported_filetype("test.py") == True
>       assert config.is_supported_filetype("test.PY") == True
E       AssertionError: assert False == True
E        +  where False = is_supported_filetype('test.PY')
E        +    where is_supported_filetype = Config(py_version='py3', force_to_top=frozenset(), skip=frozenset({'.eggs', '.venv', '.svn', '.mypy_cache', 'venv', '_...ge}', format_success='{success}: {message}', sort_order='natural', sort_reexports=False, split_on_trailing_comma=False).is_supported_filetype

isort/Test4DT_tests/test_isort_settings_Config_is_supported_filetype_3_test_valid_case.py:12: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_settings_Config_is_supported_filetype_3_test_valid_case.py::test_is_supported_filetype
============================== 1 failed in 0.13s ===============================
"""