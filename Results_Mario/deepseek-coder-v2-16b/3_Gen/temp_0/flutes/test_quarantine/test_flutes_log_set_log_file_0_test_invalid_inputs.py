
import pytest
from pathlib import Path
from flutes.log import set_log_file, LOGGER, MultiprocessingFileHandler
import logging

@pytest.mark.parametrize("path", [None, "", "invalid_path"])
def test_set_log_file_invalid_inputs(path):
    with pytest.raises(TypeError):
        set_log_file(path)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 3 items

flutes/Test4DT_tests/test_flutes_log_set_log_file_0_test_invalid_inputs.py . [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
______________________ test_set_log_file_invalid_inputs[] ______________________

path = ''

    @pytest.mark.parametrize("path", [None, "", "invalid_path"])
    def test_set_log_file_invalid_inputs(path):
        with pytest.raises(TypeError):
>           set_log_file(path)

flutes/Test4DT_tests/test_flutes_log_set_log_file_0_test_invalid_inputs.py:10: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
flutes/flutes/log.py:146: in set_log_file
    handler = MultiprocessingFileHandler(path, mode="a")
flutes/flutes/log.py:46: in __init__
    self._handler = logging.FileHandler(path, mode=mode)
/usr/local/lib/python3.11/logging/__init__.py:1181: in __init__
    StreamHandler.__init__(self, self._open())
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <[AttributeError("'FileHandler' object has no attribute 'level'") raised in repr()] FileHandler object at 0x7f6429b95690>

    def _open(self):
        """
        Open the current base file with the (original) mode and encoding.
        Return the resulting stream.
        """
        open_func = self._builtin_open
>       return open_func(self.baseFilename, self.mode,
                         encoding=self.encoding, errors=self.errors)
E       IsADirectoryError: [Errno 21] Is a directory: '/projects/F202407648IACDCF2/mario'

/usr/local/lib/python3.11/logging/__init__.py:1213: IsADirectoryError
________________ test_set_log_file_invalid_inputs[invalid_path] ________________

path = 'invalid_path'

    @pytest.mark.parametrize("path", [None, "", "invalid_path"])
    def test_set_log_file_invalid_inputs(path):
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

flutes/Test4DT_tests/test_flutes_log_set_log_file_0_test_invalid_inputs.py:9: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_log_set_log_file_0_test_invalid_inputs.py::test_set_log_file_invalid_inputs[]
FAILED flutes/Test4DT_tests/test_flutes_log_set_log_file_0_test_invalid_inputs.py::test_set_log_file_invalid_inputs[invalid_path]
========================= 2 failed, 1 passed in 0.12s ==========================

"""