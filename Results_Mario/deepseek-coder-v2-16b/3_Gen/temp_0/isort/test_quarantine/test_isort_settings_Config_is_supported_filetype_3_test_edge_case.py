
import pytest
from isort.settings import Config

def test_is_supported_filetype():
    config = Config()
    
    # Test with None as file name
    assert not config.is_supported_filetype(None)

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

isort/Test4DT_tests/test_isort_settings_Config_is_supported_filetype_3_test_edge_case.py F [100%]

=================================== FAILURES ===================================
__________________________ test_is_supported_filetype __________________________

    def test_is_supported_filetype():
        config = Config()
    
        # Test with None as file name
>       assert not config.is_supported_filetype(None)

isort/Test4DT_tests/test_isort_settings_Config_is_supported_filetype_3_test_edge_case.py:9: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
isort/isort/settings.py:519: in is_supported_filetype
    _root, ext = os.path.splitext(file_name)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

p = None

>   ???
E   TypeError: expected str, bytes or os.PathLike object, not NoneType

<frozen posixpath>:118: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_settings_Config_is_supported_filetype_3_test_edge_case.py::test_is_supported_filetype
============================== 1 failed in 0.15s ===============================
"""