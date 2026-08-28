
import pytest
from unittest.mock import patch, MagicMock
from datetime import date
from decimal import Decimal
from pypara.currencies import Currencies
from pypara.exchange import FXRate



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_exchange_FXRate_of_0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

    def test_valid_inputs():
        with patch('pypara.exchange.FXRate', autospec=True) as mock_fxrate:
            rate = FXRate(Currencies['EUR'], Currencies['USD'], date.today(), Decimal('2'))
            assert isinstance(rate, FXRate)
>           mock_fxrate.assert_called_once_with(Currencies['EUR'], Currencies['USD'], date.today(), Decimal('2'))

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_exchange_FXRate_of_0.py:13: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <MagicMock name='FXRate' spec='FXRate' id='140396638238224'>
args = (Currency(code='EUR', name='Euro', decimals=2, type=<CurrencyType.MONEY: 'Money'>, quantizer=Decimal('0.00'), hashcach...e.MONEY: 'Money'>, quantizer=Decimal('0.00'), hashcache=6422399235506489804), datetime.date(2026, 6, 16), Decimal('2'))
kwargs = {}, msg = "Expected 'FXRate' to be called once. Called 0 times."

    def assert_called_once_with(self, /, *args, **kwargs):
        """assert that the mock was called exactly once and that that call was
        with the specified arguments."""
        if not self.call_count == 1:
            msg = ("Expected '%s' to be called once. Called %s times.%s"
                   % (self._mock_name or 'mock',
                      self.call_count,
                      self._calls_repr()))
>           raise AssertionError(msg)
E           AssertionError: Expected 'FXRate' to be called once. Called 0 times.

/opt/conda/envs/test4py_env/lib/python3.10/unittest/mock.py:940: AssertionError
_______________________________ test_edge_cases ________________________________

    def test_edge_cases():
        with patch('pypara.exchange.FXRate', autospec=True) as mock_fxrate:
            rate = FXRate(None, None, None, Decimal('0'))
            assert isinstance(rate, FXRate)
>           mock_fxrate.assert_called_once_with(None, None, None, Decimal('0'))

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_exchange_FXRate_of_0.py:19: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <MagicMock name='FXRate' spec='FXRate' id='140396664486448'>
args = (None, None, None, Decimal('0')), kwargs = {}
msg = "Expected 'FXRate' to be called once. Called 0 times."

    def assert_called_once_with(self, /, *args, **kwargs):
        """assert that the mock was called exactly once and that that call was
        with the specified arguments."""
        if not self.call_count == 1:
            msg = ("Expected '%s' to be called once. Called %s times.%s"
                   % (self._mock_name or 'mock',
                      self.call_count,
                      self._calls_repr()))
>           raise AssertionError(msg)
E           AssertionError: Expected 'FXRate' to be called once. Called 0 times.

/opt/conda/envs/test4py_env/lib/python3.10/unittest/mock.py:940: AssertionError
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        with patch('pypara.exchange.FXRate', autospec=True) as mock_fxrate:
>           with pytest.raises(ValueError):
E           Failed: DID NOT RAISE <class 'ValueError'>

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_exchange_FXRate_of_0.py:23: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_exchange_FXRate_of_0.py::test_valid_inputs
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_exchange_FXRate_of_0.py::test_edge_cases
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_exchange_FXRate_of_0.py::test_invalid_inputs
============================== 3 failed in 0.16s ===============================
"""