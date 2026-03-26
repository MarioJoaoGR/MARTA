
# Module: isort.deprecated.finders
# test_base_finder.py
from isort import Config
import base_finder  # Corrected import statement for 'base_finder'

def test_base_finder_initialization():
    # Arrange
    my_config = Config()
    
    # Act
    finder = base_finder.BaseFinder(my_config)  # Adjusted the instantiation to reflect the corrected import
    
    # Assert
    assert isinstance(finder, base_finder.BaseFinder), "The instance should be an instance of BaseFinder"
    assert finder.config == my_config, "The config attribute should be set to the provided Config object"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_deprecated_finders_BaseFinder___init___0
isort/Test4DT_tests/test_isort_deprecated_finders_BaseFinder___init___0.py:5:0: E0401: Unable to import 'base_finder' (import-error)


"""