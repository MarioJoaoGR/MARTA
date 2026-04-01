
import pytest
from unittest.mock import MagicMock
from flutes.structure import _NO_MAP_TYPES, register_no_map_class

@pytest.fixture
def mock_container_type():
    mock = MagicMock()
    yield mock

def test_register_no_map_class(mock_container_type):
    # Arrange
    container_type = type('ContainerType', (object,), {})
    
    # Act
    register_no_map_class(container_type)
    
    # Assert
    assert mock_container_type.add.called
    assert mock_container_type.add.call_count == 1
    assert mock_container_type.add.call_args == pytest.approx({container_type}, {})

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_structure_register_no_map_class_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
__________________________ test_register_no_map_class __________________________

mock_container_type = <MagicMock id='140002442381584'>

    def test_register_no_map_class(mock_container_type):
        # Arrange
        container_type = type('ContainerType', (object,), {})
    
        # Act
        register_no_map_class(container_type)
    
        # Assert
>       assert mock_container_type.add.called
E       AssertionError: assert False
E        +  where False = <MagicMock name='mock.add' id='140002427542352'>.called
E        +    where <MagicMock name='mock.add' id='140002427542352'> = <MagicMock id='140002442381584'>.add

flutes/Test4DT_tests/test_flutes_structure_register_no_map_class_0_test_valid_input.py:19: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_structure_register_no_map_class_0_test_valid_input.py::test_register_no_map_class
============================== 1 failed in 0.09s ===============================
"""