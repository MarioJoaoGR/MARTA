
import pytest
from unittest.mock import patch, MagicMock
from httpie.downloads import DownloadStatus
from datetime import datetime

def test_finished():
    with patch('httpie.downloads.DownloadStatus.monotonic', return_value=datetime.now()):
        status = DownloadStatus(env="test_env")
        status.time_started = datetime.now()
        
        # Ensure time_finished is initially None
        assert status.time_finished is None
        
        # Call the finished method
        status.finished()
        
        # Check that time_finished has been set to the mocked monotonic value
        assert isinstance(status.time_finished, datetime)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/httpie
configfile: pytest.ini
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_downloads_DownloadStatus_finished_2_edge_cases.py F [100%]

=================================== FAILURES ===================================
________________________________ test_finished _________________________________

    def test_finished():
>       with patch('httpie.downloads.DownloadStatus.monotonic', return_value=datetime.now()):

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_downloads_DownloadStatus_finished_2_edge_cases.py:8: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/usr/local/lib/python3.11/unittest/mock.py:1446: in __enter__
    original, local = self.get_original()
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <unittest.mock._patch object at 0x7f992a4a1fd0>

    def get_original(self):
        target = self.getter()
        name = self.attribute
    
        original = DEFAULT
        local = False
    
        try:
            original = target.__dict__[name]
        except (AttributeError, KeyError):
            original = getattr(target, name, DEFAULT)
        else:
            local = True
    
        if name in _builtins and isinstance(target, ModuleType):
            self.create = True
    
        if not self.create and original is DEFAULT:
>           raise AttributeError(
                "%s does not have the attribute %r" % (target, name)
            )
E           AttributeError: <class 'httpie.downloads.DownloadStatus'> does not have the attribute 'monotonic'

/usr/local/lib/python3.11/unittest/mock.py:1419: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_downloads_DownloadStatus_finished_2_edge_cases.py::test_finished
============================== 1 failed in 0.29s ===============================
"""