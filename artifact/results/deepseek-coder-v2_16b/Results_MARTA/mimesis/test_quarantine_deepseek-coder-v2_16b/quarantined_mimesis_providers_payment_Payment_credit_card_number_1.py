
import pytest
from mimesis.providers.payment import Payment
from mimesis.enums import CardType

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 1 item

../../../../../opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_payment_Payment_credit_card_number_1.py F [100%]

=================================== FAILURES ===================================
______________________ test_invalid_input_none_card_type _______________________

    def test_invalid_input_none_card_type():
        payment_instance = Payment()
>       with pytest.raises(NotImplementedError):
E       Failed: DID NOT RAISE <class 'NotImplementedError'>

/opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_payment_Payment_credit_card_number_1.py:8: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_payment_Payment_credit_card_number_1.py::test_invalid_input_none_card_type
============================== 1 failed in 0.13s ===============================
"""