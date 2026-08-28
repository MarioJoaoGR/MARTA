
import pytest
from pypara.dcc import DCCRegistryMachinery, DCC



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_DCCRegistryMachinery_register_0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
__________________________ test_invalid_registration ___________________________

    def test_invalid_registration():
        dcc_registry = DCCRegistryMachinery()
        new_dcc = None
    
        with pytest.raises(TypeError):
>           dcc_registry.register(new_dcc)

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_DCCRegistryMachinery_register_0.py:10: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <pypara.dcc.DCCRegistryMachinery object at 0x7fb6ccdf9ab0>, dcc = None

    def register(self, dcc: DCC) -> None:
        """
        Attempts to register the given day count convention.
        """
        ## Check if the main name is ever registered before:
>       if self._is_registered(dcc.name):
E       AttributeError: 'NoneType' object has no attribute 'name'

/opt/marta/baselines/codamosa/replication/test-apps/pypara/pypara/dcc.py:315: AttributeError
______________________ test_already_registered_main_name _______________________

    def test_already_registered_main_name():
        dcc_registry = DCCRegistryMachinery()
>       dcc1 = DCC(name="Act/Act", altnames=["act_act"])
E       TypeError: DCC.__new__() missing 2 required positional arguments: 'currencies' and 'calculate_fraction_method'

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_DCCRegistryMachinery_register_0.py:14: TypeError
_______________________ test_already_registered_altname ________________________

    def test_already_registered_altname():
        dcc_registry = DCCRegistryMachinery()
>       dcc1 = DCC(name="Act/Act", altnames=["act_act"])
E       TypeError: DCC.__new__() missing 2 required positional arguments: 'currencies' and 'calculate_fraction_method'

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_DCCRegistryMachinery_register_0.py:25: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_DCCRegistryMachinery_register_0.py::test_invalid_registration
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_DCCRegistryMachinery_register_0.py::test_already_registered_main_name
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_DCCRegistryMachinery_register_0.py::test_already_registered_altname
============================== 3 failed in 0.08s ===============================
"""