
import pytest
from pypara.monetary import Currency, Date, NonePrice, Price




"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 4 items

../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_monetary_NonePrice_convert_0.py F [ 25%]
FFF                                                                      [100%]

=================================== FAILURES ===================================
________________________ test_convert_to_same_currency _________________________

    def test_convert_to_same_currency():
        price = NonePrice()
>       converted_price = price.convert(Currency('USD'))
E       TypeError: Currency.__init__() missing 5 required positional arguments: 'name', 'decimals', 'type', 'quantizer', and 'hashcache'

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_monetary_NonePrice_convert_0.py:7: TypeError
______________________ test_convert_to_different_currency ______________________

    def test_convert_to_different_currency():
        price = NonePrice()
>       converted_price = price.convert(Currency('EUR'))
E       TypeError: Currency.__init__() missing 5 required positional arguments: 'name', 'decimals', 'type', 'quantizer', and 'hashcache'

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_monetary_NonePrice_convert_0.py:12: TypeError
_______________________ test_convert_with_specific_date ________________________

    def test_convert_with_specific_date():
        price = NonePrice()
>       converted_price = price.convert(Currency('GBP'), asof=Date(2023, 5, 1))
E       TypeError: Currency.__init__() missing 5 required positional arguments: 'name', 'decimals', 'type', 'quantizer', and 'hashcache'

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_monetary_NonePrice_convert_0.py:17: TypeError
________________________ test_convert_with_strict_mode _________________________

    def test_convert_with_strict_mode():
        price = NonePrice()
        with pytest.raises(NotImplementedError):
>           converted_price = price.convert(Currency('JPY'), strict=True)
E           TypeError: Currency.__init__() missing 5 required positional arguments: 'name', 'decimals', 'type', 'quantizer', and 'hashcache'

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_monetary_NonePrice_convert_0.py:23: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_monetary_NonePrice_convert_0.py::test_convert_to_same_currency
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_monetary_NonePrice_convert_0.py::test_convert_to_different_currency
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_monetary_NonePrice_convert_0.py::test_convert_with_specific_date
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_monetary_NonePrice_convert_0.py::test_convert_with_strict_mode
============================== 4 failed in 0.07s ===============================
"""