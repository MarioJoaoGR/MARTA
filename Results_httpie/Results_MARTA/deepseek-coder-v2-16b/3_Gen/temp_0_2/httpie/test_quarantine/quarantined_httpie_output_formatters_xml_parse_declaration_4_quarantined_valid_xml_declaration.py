
import re
from typing import Optional

XML_DECLARATION_OPEN = "<?xml"
XML_DECLARATION_CLOSE = "?>"

def parse_declaration(raw_body: str) -> Optional[str]:
    body = raw_body.strip()
    if body.startswith(XML_DECLARATION_OPEN):
        match = re.match(r'<?xml[^>]*>.*?', body)
        if match:
            return match.group(0)
    return None

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
============================ no tests ran in 0.12s =============================
"""