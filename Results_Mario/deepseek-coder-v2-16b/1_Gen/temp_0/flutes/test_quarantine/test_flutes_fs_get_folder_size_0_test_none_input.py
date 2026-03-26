
import pytest
from flutes.fs import get_folder_size
from unittest.mock import patch

def test_none_input():
    with pytest.raises(TypeError):
        with patch('flutes.fs.subprocess.check_output', side_effect=FileNotFoundError("No such file or directory")):
            assert get_folder_size(None) == 0

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_fs_get_folder_size_0_test_none_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_none_input ________________________________

    def test_none_input():
        with pytest.raises(TypeError):
            with patch('flutes.fs.subprocess.check_output', side_effect=FileNotFoundError("No such file or directory")):
>               assert get_folder_size(None) == 0

flutes/Test4DT_tests/test_flutes_fs_get_folder_size_0_test_none_input.py:9: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
flutes/flutes/fs.py:34: in get_folder_size
    return int(subprocess.check_output(['du', '-bs', str(path)]).split()[0].decode('utf-8'))
/usr/local/lib/python3.11/unittest/mock.py:1124: in __call__
    return self._mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1128: in _mock_call
    return self._execute_mock_call(*args, **kwargs)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <MagicMock name='check_output' id='140054727656912'>
args = (['du', '-bs', 'None'],), kwargs = {}
effect = FileNotFoundError('No such file or directory')

    def _execute_mock_call(self, /, *args, **kwargs):
        # separate from _increment_mock_call so that awaited functions are
        # executed separately from their call, also AsyncMock overrides this method
    
        effect = self.side_effect
        if effect is not None:
            if _is_exception(effect):
>               raise effect
E               FileNotFoundError: No such file or directory

/usr/local/lib/python3.11/unittest/mock.py:1183: FileNotFoundError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_fs_get_folder_size_0_test_none_input.py::test_none_input
============================== 1 failed in 0.14s ===============================
"""