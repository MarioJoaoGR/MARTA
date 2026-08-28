
import pytest
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

# Test scenario 1: Mute multiple register instances
def test_mute_multiple_registers():
    register1 = Register()
    register2 = Register()
    
    mute(register1, register2)
    
    assert register1.is_muted is True
    assert register2.is_muted is True

# Test scenario 2: Raise ValueError when passing a non-Register object
def test_mute_non_register_object():
    register = Register()
    non_register = NonRegisterClass()
    
    with pytest.raises(ValueError) as excinfo:
        mute(register, non_register)
    
    assert str(excinfo.value) == "The mute() method can only be used with objects that inherit from the 'Register class'."

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
/opt/marta/baselines/Results_MARTA/sty/Test4DT_tests_deepseek-coder-v2_16b/test_sty_lib_mute_0.py:3: in <module>
    from sty.lib import Register, NonRegisterClass
E   ImportError: cannot import name 'NonRegisterClass' from 'sty.lib' (/opt/marta/baselines/codamosa/replication/test-apps/sty/sty/lib.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/sty/Test4DT_tests_deepseek-coder-v2_16b/test_sty_lib_mute_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.11s ===============================
"""