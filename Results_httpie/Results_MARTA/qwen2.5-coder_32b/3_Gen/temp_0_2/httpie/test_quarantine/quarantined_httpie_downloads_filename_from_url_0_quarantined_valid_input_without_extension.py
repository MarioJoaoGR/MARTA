
import os
from urllib.parse import urlsplit
import mimetypes
from typing import Optional

def filename_from_url(url: str, content_type: Optional[str]) -> str:
    fn = urlsplit(url).path.rstrip('/')
    fn = os.path.basename(fn) if fn else 'index'
    if '.' not in fn and content_type:
        content_type = content_type.split(';')[0]
        ext = mimetypes.guess_extension(content_type) or ''
        if ext == '.htm':
            ext = '.html'
        if ext:
            fn += ext
    return fn

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
report saved to: pytest_report_qwen2.5-coder_32b.json
============================ no tests ran in 0.11s =============================
"""