
import pytest
from prettyprinter import ISortPrettyPrinter
from isort import Config

@pytest.fixture
def config():
    return Config(line_length=88, compact=True)

def test_none_config(config):
    printer = ISortPrettyPrinter(config)
    assert isinstance(printer, ISortPrettyPrinter)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_literal_ISortPrettyPrinter___init___0_test_none_config
isort/Test4DT_tests/test_isort_literal_ISortPrettyPrinter___init___0_test_none_config.py:3:0: E0401: Unable to import 'prettyprinter' (import-error)


"""