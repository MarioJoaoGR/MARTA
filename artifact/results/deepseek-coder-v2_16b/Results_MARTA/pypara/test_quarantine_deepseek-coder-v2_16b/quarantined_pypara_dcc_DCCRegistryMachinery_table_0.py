
import pytest
from pypara.dcc import DCCRegistryMachinery, DCC, Money, Currencies
import datetime
from decimal import Decimal


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_DCCRegistryMachinery_table_0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_case ________________________________

    def test_valid_case():
        dcc_registry = DCCRegistryMachinery()
>       principal = Money(Currencies["USD"], Decimal(1000000), datetime.date.today())
E       TypeError: Money() takes no arguments

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_DCCRegistryMachinery_table_0.py:9: TypeError
________________________________ test_edge_case ________________________________

    def test_edge_case():
        dcc_registry = DCCRegistryMachinery()
        with pytest.raises(ValueError):
>           dcc_registry.find(None)

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_DCCRegistryMachinery_table_0.py:21: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <pypara.dcc.DCCRegistryMachinery object at 0x7f9d5079bdc0>, name = None

    def find(self, name: str) -> Optional[DCC]:
        """
        Attempts to find the day count convention by the given name.
    
        Note that all day count conventions are registered under stripped, uppercased names. Therefore,
        the implementation will first attempt to find by given name as is. If it can not find it, it will
        strip and uppercase the name and try to find it as such as a last resort.
        """
>       return self._find_strict(name) or self._find_strict(name.strip().upper())
E       AttributeError: 'NoneType' object has no attribute 'strip'

/opt/marta/baselines/codamosa/replication/test-apps/pypara/pypara/dcc.py:346: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_DCCRegistryMachinery_table_0.py::test_valid_case
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_DCCRegistryMachinery_table_0.py::test_edge_case
============================== 2 failed in 0.07s ===============================
"""