
import pytest
from httpie.context import Environment
from pathlib import Path
import sys
from unittest.mock import patch, MagicMock

@pytest.fixture
def setup_environment():
    # Create an instance of the Environment class with default values for testing
    env = Environment()
    
    # Mock the config_dir attribute to return a fixed value for testing purposes
    with patch('httpie.context.Environment.config_dir', new=Path("test_config")):
        yield env

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