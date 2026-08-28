
import pytest
from datetime import date
from pypara.exchange import FXRateService, Currency, FXRate

# Test for basic queries without strict mode

# Test for queries with strict mode

# Test for queries without strict mode
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_exchange_FXRateService_queries_0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
_______________________ test_FXRateService_queries_basic _______________________

    def test_FXRateService_queries_basic():
>       class ConcreteFXRateService(FXRateService):

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_exchange_FXRateService_queries_0.py:8: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

    class ConcreteFXRateService(FXRateService):
>       def queries(self, queries: Iterable[Tuple[Currency, Currency, Date]], strict: bool = False) -> Iterable[Optional[FXRate]]:
E       NameError: name 'Iterable' is not defined

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_exchange_FXRateService_queries_0.py:9: NameError
______________________ test_FXRateService_queries_strict _______________________

    def test_FXRateService_queries_strict():
>       class ConcreteFXRateService(FXRateService):

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_exchange_FXRateService_queries_0.py:31: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

    class ConcreteFXRateService(FXRateService):
>       def queries(self, queries: Iterable[Tuple[Currency, Currency, Date]], strict: bool = True) -> Iterable[Optional[FXRate]]:
E       NameError: name 'Iterable' is not defined

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_exchange_FXRateService_queries_0.py:32: NameError
____________________ test_FXRateService_queries_non_strict _____________________

    def test_FXRateService_queries_non_strict():
>       class ConcreteFXRateService(FXRateService):

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_exchange_FXRateService_queries_0.py:57: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

    class ConcreteFXRateService(FXRateService):
>       def queries(self, queries: Iterable[Tuple[Currency, Currency, Date]], strict: bool = False) -> Iterable[Optional[FXRate]]:
E       NameError: name 'Iterable' is not defined

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_exchange_FXRateService_queries_0.py:58: NameError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_exchange_FXRateService_queries_0.py::test_FXRateService_queries_basic
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_exchange_FXRateService_queries_0.py::test_FXRateService_queries_strict
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_exchange_FXRateService_queries_0.py::test_FXRateService_queries_non_strict
============================== 3 failed in 0.10s ===============================
"""