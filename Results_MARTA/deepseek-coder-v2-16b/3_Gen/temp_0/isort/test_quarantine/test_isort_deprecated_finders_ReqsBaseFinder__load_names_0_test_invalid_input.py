
from isort.deprecated.finders import ReqsBaseFinder
import pytest
from unittest.mock import MagicMock

@pytest.fixture
def config():
    mock_config = MagicMock()
    mock_config.enabled = True  # Assuming the Config class has an enabled attribute
    return mock_config

def test_invalid_input(config):
    with pytest.raises(TypeError):
        ReqsBaseFinder(config=config, path="some/path")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_deprecated_finders_ReqsBaseFinder__load_names_0_test_invalid_input
isort/Test4DT_tests/test_isort_deprecated_finders_ReqsBaseFinder__load_names_0_test_invalid_input.py:14:8: E0110: Abstract class 'ReqsBaseFinder' with abstract methods instantiated (abstract-class-instantiated)


"""