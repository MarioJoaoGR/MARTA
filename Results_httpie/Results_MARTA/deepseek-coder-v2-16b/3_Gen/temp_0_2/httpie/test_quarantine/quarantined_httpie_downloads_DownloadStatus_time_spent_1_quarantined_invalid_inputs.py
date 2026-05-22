
import pytest
from unittest.mock import patch, MagicMock
from datetime import datetime

class DownloadStatus:
    """Holds details about the download status."""
    def __init__(self, env):
        self.env = env
        self.downloaded = 0
        self.total_size = None
        self.resumed_from = 0
        self.time_started = None
        self.time_finished = None

    def time_spent(self):
        if (
            self.time_started is not None
            and self.time_finished is not None
        ):
            return self.time_finished - self.time_started
        else:
            return None

def test_invalid_inputs():
    with patch('builtins.isinstance', side_effect=TypeError):
        status = DownloadStatus(env="network_storage")
        status.downloaded = "not an int"
        status.total_size = "also not an int"
        status.resumed_from = "definitely not an int"
        status.time_started = datetime.now()
        status.time_finished = datetime.now()
        
        with pytest.raises(TypeError):
            assert status.downloaded == 0
            assert status.total_size is None
            assert status.resumed_from == 0
            assert status.time_started is not None
            assert status.time_finished is not None

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

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_downloads_DownloadStatus_time_spent_1_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        with patch('builtins.isinstance', side_effect=TypeError):
            status = DownloadStatus(env="network_storage")
            status.downloaded = "not an int"
            status.total_size = "also not an int"
            status.resumed_from = "definitely not an int"
            status.time_started = datetime.now()
            status.time_finished = datetime.now()
    
>           with pytest.raises(TypeError):

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_downloads_DownloadStatus_time_spent_1_test_invalid_inputs.py:34: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1131: in _increment_mock_call
    self.called = True
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <MagicMock name='isinstance' id='139836366576784'>, name = 'called'
value = True

    def __setattr__(self, name, value):
        if name in _allowed_names:
            # property setters go through here
>           return object.__setattr__(self, name, value)
E           RecursionError: maximum recursion depth exceeded

/usr/local/lib/python3.11/unittest/mock.py:765: RecursionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_downloads_DownloadStatus_time_spent_1_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 6.66s ===============================
"""