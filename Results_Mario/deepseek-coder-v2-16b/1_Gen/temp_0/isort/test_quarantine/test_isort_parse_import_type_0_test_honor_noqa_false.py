
# Import the necessary function from the correct module
from isort.parse import import_type
from isort.config import Config, DEFAULT_CONFIG

def test_honor_noqa_false():
    # Create a mock config with honor_noqa set to False
    config = Config()
    config.honor_noqa = False
    
    # Test the function with a line that contains 'noqa' but should not be ignored due to config setting
    assert import_type("# noqa: F401", config) == 'straight'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_parse_import_type_0_test_honor_noqa_false
isort/Test4DT_tests/test_isort_parse_import_type_0_test_honor_noqa_false.py:4:0: E0401: Unable to import 'isort.config' (import-error)
isort/Test4DT_tests/test_isort_parse_import_type_0_test_honor_noqa_false.py:4:0: E0611: No name 'config' in module 'isort' (no-name-in-module)


"""