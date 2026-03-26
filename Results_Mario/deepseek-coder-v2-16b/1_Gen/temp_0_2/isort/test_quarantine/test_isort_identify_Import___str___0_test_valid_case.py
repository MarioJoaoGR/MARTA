
from pathlib import Path

class Import:
    line_number: int
    indented: bool
    module: str
    attribute: str | None = None
    alias: str | None = None
    cimport: bool = False
    file_path: Path | None = None
    
    def __str__(self) -> str:
        if self.module and not self.cimport:
            module_part = f"from {self.module} import "
            if self.attribute:
                module_part += f"{self.attribute}"
            if self.alias:
                module_part += f" as {self.alias}"
        elif not self.cimport:
            module_part = f"import {self.module}"
            if self.alias:
                module_part += f" as {self.alias}"
        else:
            module_part = f"cimport {self.module}"
        
        return (
            f"{self.file_path or ''}:{self.line_number} "
            f"{'indented ' if self.indented else ''}{module_part}"
        )

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 0 items

--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
============================ no tests ran in 0.05s =============================
"""