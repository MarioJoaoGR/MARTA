
import pytest
from typesystem.tokenize.tokenize_json import _TokenizingDecoder

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/typesystem/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 1 item

../../../../../opt/marta/baselines/Results_MARTA/typesystem/Test4DT_tests_deepseek-coder-v2_16b/test_typesystem_tokenize_tokenize_json__TokenizingDecoder___init___0.py F [100%]

=================================== FAILURES ===================================
_____________________ test_init_without_content_parameter ______________________

    def test_init_without_content_parameter():
        with pytest.raises(TypeError):
>           decoder = _TokenizingDecoder()

/opt/marta/baselines/Results_MARTA/typesystem/Test4DT_tests_deepseek-coder-v2_16b/test_typesystem_tokenize_tokenize_json__TokenizingDecoder___init___0.py:7: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <typesystem.tokenize.tokenize_json._TokenizingDecoder object at 0x7f6bd4f24d30>
args = (), kwargs = {}

    def __init__(self, *args: typing.Any, **kwargs: typing.Any) -> None:
>       content = kwargs.pop("content")
E       KeyError: 'content'

/opt/marta/baselines/codamosa/replication/test-apps/typesystem/typesystem/tokenize/tokenize_json.py:160: KeyError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/typesystem/Test4DT_tests_deepseek-coder-v2_16b/test_typesystem_tokenize_tokenize_json__TokenizingDecoder___init___0.py::test_init_without_content_parameter
============================== 1 failed in 0.34s ===============================
"""