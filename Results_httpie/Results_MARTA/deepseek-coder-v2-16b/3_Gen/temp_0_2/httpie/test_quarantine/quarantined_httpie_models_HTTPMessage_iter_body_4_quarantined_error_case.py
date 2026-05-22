
import pytest
from unittest.mock import patch
from httpie.models import HTTPMessage

class MyHTTPMessage(HTTPMessage):
    def iter_body(self, chunk_size: int) -> Iterable[bytes]:
        if chunk_size <= 0:
            raise ValueError('chunk_size must be positive')
        # Implement your custom logic to iterate over the body here.
        pass

def test_error_case():
    with patch.object(MyHTTPMessage, 'iter_body', side_effect=ValueError):
        msg = MyHTTPMessage(orig="test")
        with pytest.raises(ValueError):
            for chunk in msg.iter_body(chunk_size=-1):
                pass

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_deepseek-coder-v2_16b.test_httpie_models_HTTPMessage_iter_body_4_test_error_case
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_models_HTTPMessage_iter_body_4_test_error_case.py:7:44: E0602: Undefined variable 'Iterable' (undefined-variable)
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_models_HTTPMessage_iter_body_4_test_error_case.py:17:25: E1133: Non-iterable value msg.iter_body(chunk_size=-1) is used in an iterating context (not-an-iterable)


"""