
import pytest
from dataclasses import dataclass, fields
from typing import Any, Optional

@pytest.fixture(autouse=True)
def setup():
    @dataclass
    class ExampleDataclass:
        field_name: str = "default_field"

    def override_(_, _field_name: Optional[str] = None):
        return _field_name if _field_name is not None else _.field_name

    yield {"override_": override_, "ExampleDataclass": ExampleDataclass}

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/dataclasses-json
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 0 items

--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
============================ no tests ran in 0.01s =============================
"""