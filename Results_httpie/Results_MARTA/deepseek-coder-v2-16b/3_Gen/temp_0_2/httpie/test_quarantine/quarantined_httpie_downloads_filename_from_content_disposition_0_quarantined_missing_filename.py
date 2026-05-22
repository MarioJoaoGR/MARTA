
from httpie.downloads import os, Message
from unittest.mock import patch
from typing import Optional

def filename_from_content_disposition(content_disposition: str) -> Optional[str]:
    """
    Extract and validate filename from a Content-Disposition header.

    :param content_disposition: Content-Disposition value
    :return: the filename if present and valid, otherwise `None`

    """
    msg = Message(f'Content-Disposition: {content_disposition}')
    with patch('httpie.downloads.os') as mock_os:
        filename = msg.get_filename()
        if filename:
            # Basic sanitation.
            mock_os.path.basename.return_value = os.path.basename(filename).lstrip('.').strip()
            return mock_os.path.basename.return_value

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/httpie
configfile: pytest.ini
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 0 items

--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
============================ no tests ran in 0.17s =============================
"""