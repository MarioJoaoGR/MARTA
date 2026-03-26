
import pytest
from unittest.mock import MagicMock
from isort.literal import ISortPrettyPrinter
from isort.config import Config  # Assuming Config is defined in isort.config

def test_valid_input():
    config = MagicMock()
    config.line_length = 80  # Example value, adjust as necessary
    
    pretty_printer = ISortPrettyPrinter(config)
    
    assert isinstance(pretty_printer, ISortPrettyPrinter)
    assert pretty_printer.width == 80
    assert pretty_printer.compact is True

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_literal_ISortPrettyPrinter___init___0_test_valid_input
isort/Test4DT_tests/test_isort_literal_ISortPrettyPrinter___init___0_test_valid_input.py:5:0: E0401: Unable to import 'isort.config' (import-error)
isort/Test4DT_tests/test_isort_literal_ISortPrettyPrinter___init___0_test_valid_input.py:5:0: E0611: No name 'config' in module 'isort' (no-name-in-module)
isort/Test4DT_tests/test_isort_literal_ISortPrettyPrinter___init___0_test_valid_input.py:14:11: E1101: Instance of 'ISortPrettyPrinter' has no 'width' member; maybe '_width'? (no-member)
isort/Test4DT_tests/test_isort_literal_ISortPrettyPrinter___init___0_test_valid_input.py:15:11: E1101: Instance of 'ISortPrettyPrinter' has no 'compact' member; maybe '_compact'? (no-member)


"""