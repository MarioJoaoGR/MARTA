
import pytest
from isort.pretty_printer import ISortPrettyPrinter
from isort.config import Config

def test_none_config():
    config = None
    with pytest.raises(TypeError):
        ISortPrettyPrinter(config)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_literal_ISortPrettyPrinter___init___0_test_none_config
isort/Test4DT_tests/test_isort_literal_ISortPrettyPrinter___init___0_test_none_config.py:3:0: E0401: Unable to import 'isort.pretty_printer' (import-error)
isort/Test4DT_tests/test_isort_literal_ISortPrettyPrinter___init___0_test_none_config.py:3:0: E0611: No name 'pretty_printer' in module 'isort' (no-name-in-module)
isort/Test4DT_tests/test_isort_literal_ISortPrettyPrinter___init___0_test_none_config.py:4:0: E0401: Unable to import 'isort.config' (import-error)
isort/Test4DT_tests/test_isort_literal_ISortPrettyPrinter___init___0_test_none_config.py:4:0: E0611: No name 'config' in module 'isort' (no-name-in-module)


"""