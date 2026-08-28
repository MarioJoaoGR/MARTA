
import pytest
from unittest.mock import patch, MagicMock
from pypara.dcc import DCCRegistryMachinery, DCC
from decimal import Decimal
import datetime
from pypara.money import Money, Currencies

# Test for edge cases where buffers are not empty but not properly initialized
def test_edge_cases():
    with patch('pypara.dcc.DCCRegistryMachinery') as mock_registry:
        # Arrange
        mock_registry.return_value._buffer_main = {}
        mock_registry.return_value._buffer_altn = {"act_act": MagicMock()}

        # Act
        registry = DCCRegistryMachinery()
        table = registry.table()

        # Assert
        assert isinstance(table, dict), "Expected a dictionary but got something else"
        assert len(table) == 1, "Expected one item in the table but found more or less"
        assert "act_act" in table, "Expected 'act_act' to be in the table but it was not found"

# Test for invalid inputs where both buffers are empty
def test_invalid_inputs():
    with patch('pypara.dcc.DCCRegistryMachinery') as mock_registry:
        # Arrange
        mock_registry.return_value._buffer_main = {}
        mock_registry.return_value._buffer_altn = {}

        # Act
        registry = DCCRegistryMachinery()
        table = registry.table()

        # Assert
        assert isinstance(table, dict), "Expected a dictionary but got something else"
        assert len(table) == 0, "Expected no items in the table but found more or less"

# Test for valid operation where both buffers are populated
def test_valid_operation():
    with patch('pypara.dcc.DCCRegistryMachinery') as mock_registry:
        # Arrange
        mock_registry.return_value._buffer_main = {"act_act": MagicMock()}
        mock_registry.return_value._buffer_altn = {"act_act": MagicMock(), "another_dcc": MagicMock()}

        # Act
        registry = DCCRegistryMachinery()
        table = registry.table()

        # Assert
        assert isinstance(table, dict), "Expected a dictionary but got something else"
        assert len(table) == 2, "Expected two items in the table but found more or less"
        assert "act_act" in table, "Expected 'act_act' to be in the table but it was not found"
        assert "another_dcc" in table, "Expected 'another_dcc' to be in the table but it was not found"

# Test for calculation of interest using a specific DCC
def test_calculate_interest():
    with patch('pypara.dcc.DCCRegistryMachinery') as mock_registry:
        # Arrange
        principal = Money(Currencies["USD"], Decimal(1000000), datetime.date.today())
        start_date = datetime.date(2007, 12, 28)
        end_date = datetime.date(2008, 2, 28)
        rate = Decimal(0.01)
        dcc = DCC("Act/Act", ["act_act"])
        mock_registry.return_value._buffer_main = {"Act/Act": dcc}
        mock_registry.return_value._buffer_altn = {"act_act": dcc}

        # Act
        registry = DCCRegistryMachinery()
        interest_amount = dcc.interest(principal, rate, start_date, end_date, end_date)

        # Assert
        assert isinstance(interest_amount, Money), "Expected a Money object but got something else"
        assert abs(interest_amount.qty - Decimal('1694.29')) < 0.01, f"Unexpected interest amount: {interest_amount.qty}"

# Test for calculation of interest with different dates
def test_calculate_interest_with_different_dates():
    with patch('pypara.dcc.DCCRegistryMachinery') as mock_registry:
        # Arrange
        principal = Money(Currencies["USD"], Decimal(1000000), datetime.date.today())
        start_date = datetime.date(2008, 2, 28)
        end_date = datetime.date(2007, 12, 28)
        rate = Decimal(0.01)
        dcc = DCC("Act/Act", ["act_act"])
        mock_registry.return_value._buffer_main = {"Act/Act": dcc}
        mock_registry.return_value._buffer_altn = {"act_act": dcc}

        # Act
        registry = DCCRegistryMachinery()
        interest_amount = dcc.interest(principal, rate, end_date, start_date, start_date)

        # Assert
        assert isinstance(interest_amount, Money), "Expected a Money object but got something else"
        assert abs(interest_amount.qty - Decimal('0.00')) < 0.01, f"Unexpected interest amount: {interest_amount.qty}"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 0 items / 1 error

==================================== ERRORS ====================================
_______ ERROR collecting test_pypara_dcc_DCCRegistryMachinery_table_1.py _______
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_DCCRegistryMachinery_table_1.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_DCCRegistryMachinery_table_1.py:7: in <module>
    from pypara.money import Money, Currencies
E   ModuleNotFoundError: No module named 'pypara.money'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_DCCRegistryMachinery_table_1.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.23s ===============================
"""