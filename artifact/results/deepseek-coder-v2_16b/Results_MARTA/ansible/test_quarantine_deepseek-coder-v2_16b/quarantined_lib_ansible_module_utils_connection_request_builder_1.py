
import pytest
import uuid
from unittest.mock import patch
from ansible.module_utils.connection import request_builder

@pytest.mark.parametrize("method, args, kwargs, expected", [
    ('multiply', (3,), {'b': 4}, {'jsonrpc': '2.0', 'method': 'multiply', 'id': str(uuid.uuid4()), 'params': ((3,), {'b': 4})}),
    ('add', (1, 2), {}, {'jsonrpc': '2.0', 'method': 'add', 'id': str(uuid.uuid4()), 'params': ((1, 2), {})}),
    ('greet', (), {}, {'jsonrpc': '2.0', 'method': 'greet', 'id': str(uuid.uuid4()), 'params': ((), {})})
])
def test_request_builder(method, args, kwargs, expected):
    with patch('uuid.uuid4', return_value='unique-identifier'):
        request = request_builder(method, *args, **kwargs)
        assert request == expected

@pytest.mark.parametrize("method, args, kwargs, expected", [
    ('multiply', (3,), {'b': 4}, {'jsonrpc': '2.0', 'method': 'multiply', 'id': str(uuid.uuid4()), 'params': ((3,), {'b': 4})}),
    ('add', (1, 2), {}, {'jsonrpc': '2.0', 'method': 'add', 'id': str(uuid.uuid4()), 'params': ((1, 2), {})}),
    ('greet', (), {}, {'jsonrpc': '2.0', 'method': 'greet', 'id': str(uuid.uuid4()), 'params': ((), {})})
])
def test_request_builder_with_mocked_uuid(method, args, kwargs, expected):
    with patch('uuid.uuid4', return_value='unique-identifier'):
        request = request_builder(method, *args, **kwargs)
        assert request['id'] == 'unique-identifier'
        assert request['jsonrpc'] == '2.0'
        assert request['method'] == method
        assert request['params'] == ((args, kwargs))
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 6 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_connection_request_builder_1.py F [ 16%]
FF...                                                                    [100%]

=================================== FAILURES ===================================
____________ test_request_builder[multiply-args0-kwargs0-expected0] ____________

method = 'multiply', args = (3,), kwargs = {'b': 4}
expected = {'id': '5cf1fe61-ed85-4959-8b12-46112fd7bc66', 'jsonrpc': '2.0', 'method': 'multiply', 'params': ((3,), {'b': 4})}

    @pytest.mark.parametrize("method, args, kwargs, expected", [
        ('multiply', (3,), {'b': 4}, {'jsonrpc': '2.0', 'method': 'multiply', 'id': str(uuid.uuid4()), 'params': ((3,), {'b': 4})}),
        ('add', (1, 2), {}, {'jsonrpc': '2.0', 'method': 'add', 'id': str(uuid.uuid4()), 'params': ((1, 2), {})}),
        ('greet', (), {}, {'jsonrpc': '2.0', 'method': 'greet', 'id': str(uuid.uuid4()), 'params': ((), {})})
    ])
    def test_request_builder(method, args, kwargs, expected):
        with patch('uuid.uuid4', return_value='unique-identifier'):
            request = request_builder(method, *args, **kwargs)
>           assert request == expected
E           AssertionError: assert {'id': 'uniqu...,), {'b': 4})} == {'id': '5cf1f...,), {'b': 4})}
E             
E             Omitting 3 identical items, use -vv to show
E             Differing items:
E             {'id': 'unique-identifier'} != {'id': '5cf1fe61-ed85-4959-8b12-46112fd7bc66'}
E             Use -v to get more diff

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_connection_request_builder_1.py:15: AssertionError
______________ test_request_builder[add-args1-kwargs1-expected1] _______________

method = 'add', args = (1, 2), kwargs = {}
expected = {'id': '44274b3b-bcd8-44e8-9998-59994445b13f', 'jsonrpc': '2.0', 'method': 'add', 'params': ((1, 2), {})}

    @pytest.mark.parametrize("method, args, kwargs, expected", [
        ('multiply', (3,), {'b': 4}, {'jsonrpc': '2.0', 'method': 'multiply', 'id': str(uuid.uuid4()), 'params': ((3,), {'b': 4})}),
        ('add', (1, 2), {}, {'jsonrpc': '2.0', 'method': 'add', 'id': str(uuid.uuid4()), 'params': ((1, 2), {})}),
        ('greet', (), {}, {'jsonrpc': '2.0', 'method': 'greet', 'id': str(uuid.uuid4()), 'params': ((), {})})
    ])
    def test_request_builder(method, args, kwargs, expected):
        with patch('uuid.uuid4', return_value='unique-identifier'):
            request = request_builder(method, *args, **kwargs)
>           assert request == expected
E           AssertionError: assert {'id': 'uniqu... ((1, 2), {})} == {'id': '44274... ((1, 2), {})}
E             
E             Omitting 3 identical items, use -vv to show
E             Differing items:
E             {'id': 'unique-identifier'} != {'id': '44274b3b-bcd8-44e8-9998-59994445b13f'}
E             Use -v to get more diff

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_connection_request_builder_1.py:15: AssertionError
_____________ test_request_builder[greet-args2-kwargs2-expected2] ______________

method = 'greet', args = (), kwargs = {}
expected = {'id': '2448a4de-3c5b-4b0b-98bb-74c92f8aef6c', 'jsonrpc': '2.0', 'method': 'greet', 'params': ((), {})}

    @pytest.mark.parametrize("method, args, kwargs, expected", [
        ('multiply', (3,), {'b': 4}, {'jsonrpc': '2.0', 'method': 'multiply', 'id': str(uuid.uuid4()), 'params': ((3,), {'b': 4})}),
        ('add', (1, 2), {}, {'jsonrpc': '2.0', 'method': 'add', 'id': str(uuid.uuid4()), 'params': ((1, 2), {})}),
        ('greet', (), {}, {'jsonrpc': '2.0', 'method': 'greet', 'id': str(uuid.uuid4()), 'params': ((), {})})
    ])
    def test_request_builder(method, args, kwargs, expected):
        with patch('uuid.uuid4', return_value='unique-identifier'):
            request = request_builder(method, *args, **kwargs)
>           assert request == expected
E           AssertionError: assert {'id': 'uniqu...ms': ((), {})} == {'id': '2448a...ms': ((), {})}
E             
E             Omitting 3 identical items, use -vv to show
E             Differing items:
E             {'id': 'unique-identifier'} != {'id': '2448a4de-3c5b-4b0b-98bb-74c92f8aef6c'}
E             Use -v to get more diff

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_connection_request_builder_1.py:15: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_connection_request_builder_1.py::test_request_builder[multiply-args0-kwargs0-expected0]
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_connection_request_builder_1.py::test_request_builder[add-args1-kwargs1-expected1]
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_connection_request_builder_1.py::test_request_builder[greet-args2-kwargs2-expected2]
========================= 3 failed, 3 passed in 0.67s ==========================
"""