
def _extract_google_drive_file_id(url: str) -> str:
    # The ID is the first segment after `/d/`.
    start_index = url.find('/d/') + 3
    if start_index == -1 or start_index >= len(url):
        return ''
    end_index = url[start_index:].find('/')
    if end_index == -1:
        return url[start_index:]
    return url[start_index:start_index + end_index]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 0 items

--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
============================ no tests ran in 0.03s =============================

"""