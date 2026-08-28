
import pytest
from mimesis.providers.internet import Internet
from mimesis.enums import PortRange

@pytest.fixture(scope="module")
def internet_instance():
    return Internet()


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_internet_Internet_port_0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_______________________ test_valid_input_specific_range ________________________

internet_instance = <mimesis.providers.internet.Internet object at 0x7f125af8c8e0>

    def test_valid_input_specific_range(internet_instance):
        port = internet_instance.port(PortRange.WELL_KNOWN)
>       assert port in [80, 21, 25], "Port should be one of the well-known ports"
E       AssertionError: Port should be one of the well-known ports
E       assert 485 in [80, 21, 25]

/opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_internet_Internet_port_0.py:12: AssertionError
___________________________ test_invalid_input_range ___________________________

internet_instance = <mimesis.providers.internet.Internet object at 0x7f125af8c8e0>

    def test_invalid_input_range(internet_instance):
        with pytest.raises(ValueError):
>           internet_instance.port("INVALID_RANGE")

/opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_internet_Internet_port_0.py:16: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <mimesis.providers.internet.Internet object at 0x7f125af8c8e0>
port_range = 'INVALID_RANGE'

    def port(self, port_range: PortRange = PortRange.ALL) -> int:
        """Generate random port.
    
        :param port_range: PortRange enum object.
        :return: Port number.
        :raises NonEnumerableError: if port_range is not in PortRange.
    
        :Example:
            8080
        """
        if isinstance(port_range, PortRange):
            return self.random.randint(*port_range.value)
    
>       raise NonEnumerableError(PortRange)
E       mimesis.exceptions.NonEnumerableError: You should use one item of: «PortRange.ALL, PortRange.WELL_KNOWN, PortRange.EPHEMERAL, PortRange.REGISTERED» of the object mimesis.enums.PortRange

/opt/marta/baselines/codamosa/replication/test-apps/mimesis/mimesis/providers/internet.py:302: NonEnumerableError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_internet_Internet_port_0.py::test_valid_input_specific_range
FAILED ../../../../../opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_internet_Internet_port_0.py::test_invalid_input_range
============================== 2 failed in 0.11s ===============================
"""