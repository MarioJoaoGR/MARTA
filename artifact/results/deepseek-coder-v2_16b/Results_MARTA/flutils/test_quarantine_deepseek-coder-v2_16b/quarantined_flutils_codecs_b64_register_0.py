
import pytest
import codecs
from flutils.codecs.b64 import register, _get_codec_info

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 1 item

../../../../../opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b/test_flutils_codecs_b64_register_0.py F [100%]

=================================== FAILURES ===================================
________________________ test_register_raises_typeerror ________________________

    def test_register_raises_typeerror():
        """Test that calling `register` raises a TypeError if codecs.getdecoder fails to find 'b64' codec."""
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

/opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b/test_flutils_codecs_b64_register_0.py:8: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b/test_flutils_codecs_b64_register_0.py::test_register_raises_typeerror
============================== 1 failed in 0.06s ===============================
"""