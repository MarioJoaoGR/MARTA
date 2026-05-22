
import json
from pathlib import Path
from typing import Dict, Any
from httpie.config import ConfigFileError

def read_raw_config(config_type: str, path: Path) -> Dict[str, Any]:
    try:
        with path.open(encoding='utf-8') as f:
            try:
                return json.load(f)
            except ValueError as e:
                raise ConfigFileError(
                    f'invalid {config_type} file: {e} [{path}]'
                )
    except FileNotFoundError:
        pass
    except OSError as e:
        raise ConfigFileError(f'cannot read {config_type} file: {e}')

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
============================ no tests ran in 0.12s =============================
"""