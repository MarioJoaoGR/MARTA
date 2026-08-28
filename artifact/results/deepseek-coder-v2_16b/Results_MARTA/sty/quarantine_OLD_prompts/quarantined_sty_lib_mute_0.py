
import pytest
from unittest.mock import patch
from sty.lib import Register, NonRegisterClass

def mute(*objects: Register) -> None:
    """
    Use this function to mute multiple register-objects at once. Each object must inherit from the 'Register' class.

    Parameters:
        objects (Register): Pass multiple register-objects to the function. Each object must inherit from the 'Register' class.

    Raises:
        ValueError: If any of the provided objects does not inherit from the 'Register' class, a ValueError is raised with a specific error message.

    Example:
        To mute multiple registers, you can call the function as follows:
        
        >>> register1 = Register()
        >>> register2 = Register()
        >>> mute(register1, register2)  # This will successfully mute both register objects.
    
    Note:
        The 'Register' class must be defined and imported before using this function. Ensure that all passed objects are instances of the 'Register' class or its subclasses to avoid raising a ValueError.
    """
    err = ValueError(
        "The mute() method can only be used with objects that inherit "
        "from the 'Register class'."
    )
    for obj in objects:
        if not isinstance(obj, Register):
            raise err
        obj.mute()

# Test scenario 1: Mute multiple register-objects successfully
def test_mute_multiple_registers():
    with patch('sty.lib.Register', autospec=True) as mock_register:
        register1 = mock_register.return_value
        register2 = mock_register.return_value
        
        mute(register1, register2)
        
        assert register1.mute.called
        assert register2.mute.called

# Test scenario 2: Raise ValueError when passing a non-Register object
def test_mute_non_register():
    with patch('sty.lib.Register', autospec=True) as mock_register:
        register = mock_register.return_value
        non_register = NonRegisterClass()
        
        with pytest.raises(ValueError, match="The mute\(\) method can only be used with objects that inherit from the 'Register class'."):
            mute(non_register, register)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/sty/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 0 items / 1 error

==================================== ERRORS ====================================
___________________ ERROR collecting test_sty_lib_mute_0.py ____________________
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/sty/Test4DT_tests_deepseek-coder-v2_16b/test_sty_lib_mute_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/sty/Test4DT_tests_deepseek-coder-v2_16b/test_sty_lib_mute_0.py:4: in <module>
    from sty.lib import Register, NonRegisterClass
E   ImportError: cannot import name 'NonRegisterClass' from 'sty.lib' (/opt/marta/baselines/codamosa/replication/test-apps/sty/sty/lib.py)
=============================== warnings summary ===============================
../../../../../opt/marta/baselines/Results_MARTA/sty/Test4DT_tests_deepseek-coder-v2_16b/test_sty_lib_mute_0.py:52
  /opt/marta/baselines/Results_MARTA/sty/Test4DT_tests_deepseek-coder-v2_16b/test_sty_lib_mute_0.py:52: DeprecationWarning: invalid escape sequence '\('
    with pytest.raises(ValueError, match="The mute\(\) method can only be used with objects that inherit from the 'Register class'."):

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/sty/Test4DT_tests_deepseek-coder-v2_16b/test_sty_lib_mute_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
========================= 1 warning, 1 error in 0.11s ==========================
"""