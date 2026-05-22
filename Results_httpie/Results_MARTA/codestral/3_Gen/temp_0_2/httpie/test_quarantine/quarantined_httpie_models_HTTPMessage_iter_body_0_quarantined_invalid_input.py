
import pytest
from unittest.mock import patch
from httpie.models import HTTPMessage, MyHTTPMessage

class TestHTTPMessage:
    def test_invalid_input(self):
        msg = MyHTTPMessage(orig_data="test data")
        with pytest.raises(ValueError):
            for chunk in msg.iter_body(-1):
                pass

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_codestral.test_httpie_models_HTTPMessage_iter_body_0_test_invalid_input
httpie/Test4DT_tests_codestral/test_httpie_models_HTTPMessage_iter_body_0_test_invalid_input.py:4:0: E0611: No name 'MyHTTPMessage' in module 'httpie.models' (no-name-in-module)


"""