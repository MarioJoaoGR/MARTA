
import unittest.mock as mock
from httpie.utils import _max_age_to_expires

def test_valid_input():
    cookies = [{'name': 'session', 'max-age': '3600'}, {'name': 'user_token', 'expires': 1672502400}]
    now = time.time()
    
    with mock.patch('httpie.utils._max_age_to_expires') as mock_func:
        _max_age_to_expires(cookies, now)
        assert cookies == [{'name': 'session', 'max-age': '3600', 'expires': now + 3600}, {'name': 'user_token', 'expires': 1672502400}]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_codestral.test_httpie_utils__max_age_to_expires_1_test_valid_input
httpie/Test4DT_tests_codestral/test_httpie_utils__max_age_to_expires_1_test_valid_input.py:7:10: E0602: Undefined variable 'time' (undefined-variable)


"""