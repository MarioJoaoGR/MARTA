
import pytest
from sty.lib import FgRegister, BgRegister

class Register:
    def __init__(self):
        self.muted = False

    def mute(self):
        self.muted = True

    def unmute(self):
        self.muted = False

class RsRegister(Register):
    pass

def unmute(*objects: Register) -> None:
    """
    Use this function to unmute multiple register-objects at once.

    :param objects: Pass multiple register-objects to the function.
    """
    err = ValueError(
        "The unmute() method can only be used with objects that inherit "
        "from the 'Register class'."
    )
    for obj in objects:
        if not isinstance(obj, Register):
            raise err
        obj.unmute()

def test_unmute_fg_register():
    fg_reg = FgRegister()
    fg_reg.mute()
    unmute(fg_reg)
    assert not fg_reg.muted

def test_unmute_bg_register():
    bg_reg = BgRegister()
    bg_reg.mute()
    unmute(bg_reg)
    assert not bg_reg.muted

def test_unmute_rs_register():
    rs_reg = RsRegister()
    rs_reg.mute()
    unmute(rs_reg)
    assert not rs_reg.muted

def test_unmute_multiple_registers():
    fg_reg = FgRegister()
    bg_reg = BgRegister()
    rs_reg = RsRegister()

    fg_reg.mute()
    bg_reg.mute()
    rs_reg.mute()

    unmute(fg_reg, bg_reg, rs_reg)

    assert not fg_reg.muted
    assert not bg_reg.muted
    assert not rs_reg.muted

def test_unmute_invalid_object():
    class InvalidRegister:
        def __init__(self):
            self.muted = False

        def mute(self):
            self.muted = True

        def unmute(self):
            self.muted = False

    invalid_reg = InvalidRegister()
    invalid_reg.mute()

    with pytest.raises(ValueError) as excinfo:
        unmute(invalid_reg)

    assert str(excinfo.value) == "The unmute() method can only be used with objects that inherit from the 'Register class'."

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/sty/Test4DT_tests_qwen2.5-coder_32b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 0 items / 1 error

==================================== ERRORS ====================================
__________________ ERROR collecting test_sty_lib_unmute_0.py ___________________
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/sty/Test4DT_tests_qwen2.5-coder_32b/test_sty_lib_unmute_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/sty/Test4DT_tests_qwen2.5-coder_32b/test_sty_lib_unmute_0.py:3: in <module>
    from sty.lib import FgRegister, BgRegister
E   ImportError: cannot import name 'FgRegister' from 'sty.lib' (/opt/marta/baselines/codamosa/replication/test-apps/sty/sty/lib.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/sty/Test4DT_tests_qwen2.5-coder_32b/test_sty_lib_unmute_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.12s ===============================
"""