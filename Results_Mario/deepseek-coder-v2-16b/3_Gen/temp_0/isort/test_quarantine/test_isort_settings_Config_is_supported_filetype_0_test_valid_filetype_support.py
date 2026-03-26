
import os
import stat
import re
from isort.settings import Config

def test_valid_filetype_support():
    config = Config()
    
    # Test a Python file
    assert config.is_supported_filetype("test_script.py") == True
    
    # Test a non-Python file with a .py extension (should be supported)
    assert config.is_supported_filetype("non_python_script.py") == True
    
    # Test an unsupported file type without .py extension
    assert config.is_supported_filetype("unsupported_file") == False
    
    # Test a Python file with a shebang line
    with open("test_script.py", "w") as f:
        f.write("#!/usr/bin/env python\nprint('Hello, World!')")
    assert config.is_supported_filetype("test_script.py") == True
    
    # Test a Python file with only whitespace in the shebang line
    with open("test_script.py", "w") as f:
        f.write("#! \nprint('Hello, World!')")
    assert config.is_supported_filetype("test_script.py") == True
    
    # Test a non-Python file with a shebang line (should be supported)
    with open("non_python_script.sh", "w") as f:
        f.write("#!/usr/bin/bash\necho 'Hello, World!'")
    assert config.is_supported_filetype("non_python_script.sh") == True
    
    # Test an empty file (should not be supported)
    with open("empty_file", "w") as f:
        pass
    assert config.is_supported_filetype("empty_file") == False
    
    # Clean up test files
    os.remove("test_script.py")
    os.remove("non_python_script.sh")
    os.remove("empty_file")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

isort/Test4DT_tests/test_isort_settings_Config_is_supported_filetype_0_test_valid_filetype_support.py F [100%]

=================================== FAILURES ===================================
_________________________ test_valid_filetype_support __________________________

    def test_valid_filetype_support():
        config = Config()
    
        # Test a Python file
        assert config.is_supported_filetype("test_script.py") == True
    
        # Test a non-Python file with a .py extension (should be supported)
        assert config.is_supported_filetype("non_python_script.py") == True
    
        # Test an unsupported file type without .py extension
        assert config.is_supported_filetype("unsupported_file") == False
    
        # Test a Python file with a shebang line
        with open("test_script.py", "w") as f:
            f.write("#!/usr/bin/env python\nprint('Hello, World!')")
        assert config.is_supported_filetype("test_script.py") == True
    
        # Test a Python file with only whitespace in the shebang line
        with open("test_script.py", "w") as f:
            f.write("#! \nprint('Hello, World!')")
        assert config.is_supported_filetype("test_script.py") == True
    
        # Test a non-Python file with a shebang line (should be supported)
        with open("non_python_script.sh", "w") as f:
            f.write("#!/usr/bin/bash\necho 'Hello, World!'")
>       assert config.is_supported_filetype("non_python_script.sh") == True
E       AssertionError: assert False == True
E        +  where False = is_supported_filetype('non_python_script.sh')
E        +    where is_supported_filetype = Config(py_version='py3', force_to_top=frozenset(), skip=frozenset({'.git', '.direnv', '.svn', '.pants.d', 'build', 'di...ge}', format_success='{success}: {message}', sort_order='natural', sort_reexports=False, split_on_trailing_comma=False).is_supported_filetype

isort/Test4DT_tests/test_isort_settings_Config_is_supported_filetype_0_test_valid_filetype_support.py:32: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_settings_Config_is_supported_filetype_0_test_valid_filetype_support.py::test_valid_filetype_support
============================== 1 failed in 0.10s ===============================
"""