
from pathlib import Path
import pytest
from unittest.mock import patch
from httpie.config import BaseConfigDict

def test_error_case():
    with patch('pathlib.Path', spec=True) as mock_path:
        mock_path.return_value.exists.side_effect = FileNotFoundError("Invalid path")
        
        config = BaseConfigDict(path='invalid/path')
        
        with pytest.raises(FileNotFoundError):
            assert not config.is_new()

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

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_config_BaseConfigDict_is_new_1_test_error_case.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_error_case ________________________________

    def test_error_case():
        with patch('pathlib.Path', spec=True) as mock_path:
            mock_path.return_value.exists.side_effect = FileNotFoundError("Invalid path")
    
            config = BaseConfigDict(path='invalid/path')
    
            with pytest.raises(FileNotFoundError):
>               assert not config.is_new()

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_config_BaseConfigDict_is_new_1_test_error_case.py:14: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = {}

    def is_new(self) -> bool:
>       return not self.path.exists()
E       AttributeError: 'str' object has no attribute 'exists'

httpie/httpie/config.py:93: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_config_BaseConfigDict_is_new_1_test_error_case.py::test_error_case
============================== 1 failed in 0.09s ===============================
"""