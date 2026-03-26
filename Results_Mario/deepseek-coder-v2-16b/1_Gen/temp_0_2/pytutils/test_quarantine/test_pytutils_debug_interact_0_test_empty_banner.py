
import pytest
from unittest.mock import patch
import code
import inspect
from pytutils.debug import interact

@pytest.mark.parametrize("banner", [""])
def test_empty_banner(banner, capsys):
    with patch('builtins.input', side_effect=['exit']):  # Mock the input to simulate 'exit' command
        with pytest.raises(EOFError):  # Expecting EOF since no input is provided in the empty banner case
            interact(banner=banner)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pytutils
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

pytutils/Test4DT_tests/test_pytutils_debug_interact_0_test_empty_banner.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_empty_banner[] ______________________________

banner = '', capsys = <_pytest.capture.CaptureFixture object at 0x7fd812d88d50>

    @pytest.mark.parametrize("banner", [""])
    def test_empty_banner(banner, capsys):
        with patch('builtins.input', side_effect=['exit']):  # Mock the input to simulate 'exit' command
            with pytest.raises(EOFError):  # Expecting EOF since no input is provided in the empty banner case
>               interact(banner=banner)

pytutils/Test4DT_tests/test_pytutils_debug_interact_0_test_empty_banner.py:12: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
pytutils/pytutils/debug.py:18: in interact
    code.interact(local=calling_vars, banner=banner)
/usr/local/lib/python3.11/code.py:301: in interact
    console.interact(banner, exitmsg)
/usr/local/lib/python3.11/code.py:227: in interact
    line = self.raw_input(prompt)
/usr/local/lib/python3.11/code.py:274: in raw_input
    return input(prompt)
/usr/local/lib/python3.11/unittest/mock.py:1124: in __call__
    return self._mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1128: in _mock_call
    return self._execute_mock_call(*args, **kwargs)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <MagicMock name='input' id='140566005856464'>, args = ('>>> ',)
kwargs = {}, effect = <list_iterator object at 0x7fd812e485b0>

    def _execute_mock_call(self, /, *args, **kwargs):
        # separate from _increment_mock_call so that awaited functions are
        # executed separately from their call, also AsyncMock overrides this method
    
        effect = self.side_effect
        if effect is not None:
            if _is_exception(effect):
                raise effect
            elif not _callable(effect):
>               result = next(effect)
E               StopIteration

/usr/local/lib/python3.11/unittest/mock.py:1185: StopIteration
----------------------------- Captured stdout call -----------------------------
Use exit() or Ctrl-D (i.e. EOF) to exit
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_debug_interact_0_test_empty_banner.py::test_empty_banner[]
============================== 1 failed in 0.11s ===============================
"""