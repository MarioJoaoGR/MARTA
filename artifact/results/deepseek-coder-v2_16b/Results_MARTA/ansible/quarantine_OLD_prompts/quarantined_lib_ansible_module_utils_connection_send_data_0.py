
import pytest
from unittest.mock import MagicMock, patch
import struct
from ansible.module_utils.connection import send_data

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 1 item

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_connection_send_data_0.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_send_data_basic _____________________________

    def test_send_data_basic():
        mock_socket = MagicMock()
        with patch('struct.pack', return_value=b'fake_packed_len'):
            data = b"Hello, World!"
            result = send_data(mock_socket, data)
            mock_socket.sendall.assert_called_with(b'fake_packed_len' + data)
>           assert result == len(data)
E           AssertionError: assert <MagicMock name='mock.sendall()' id='140216901130880'> == 13
E            +  where 13 = len(b'Hello, World!')

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_connection_send_data_0.py:13: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_connection_send_data_0.py::test_send_data_basic
============================== 1 failed in 0.32s ===============================
"""