
import pytest
from httpie.downloads import DownloadStatus

def test_invalid_input():
    with pytest.raises(AssertionError):
        status = DownloadStatus(env='error')
        status.started(output_file=None)

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

httpie/Test4DT_tests_codestral/test_httpie_downloads_DownloadStatus_started_1_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        with pytest.raises(AssertionError):
            status = DownloadStatus(env='error')
>           status.started(output_file=None)

httpie/Test4DT_tests_codestral/test_httpie_downloads_DownloadStatus_started_1_test_invalid_input.py:8: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
httpie/httpie/downloads.py:323: in started
    self.start_display(output_file=output_file)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <httpie.downloads.DownloadStatus object at 0x7f68f0e1f310>
output_file = None

    def start_display(self, output_file):
        from httpie.output.ui.rich_progress import (
            DummyDisplay,
            StatusDisplay,
            ProgressDisplay
        )
    
>       message = f'Downloading to {output_file.name}'
E       AttributeError: 'NoneType' object has no attribute 'name'

httpie/httpie/downloads.py:332: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_codestral.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_codestral/test_httpie_downloads_DownloadStatus_started_1_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.18s ===============================
"""