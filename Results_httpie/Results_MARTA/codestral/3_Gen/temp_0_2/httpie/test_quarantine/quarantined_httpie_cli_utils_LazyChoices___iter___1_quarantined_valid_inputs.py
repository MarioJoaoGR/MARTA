
import pytest
from httpie.cli.utils import LazyChoices, get_simple_list
from unittest.mock import patch

class TestLazyChoices:
    @pytest.fixture(autouse=True)
    def setup(self):
        with patch('httpie.cli.utils.get_simple_list', return_value=[1, 2, 3]):
            self.choices = LazyChoices(getter=get_simple_list)

    def test_valid_inputs(self):
        assert list(self.choices) == [1, 2, 3]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_codestral.test_httpie_cli_utils_LazyChoices___iter___1_test_valid_inputs
httpie/Test4DT_tests_codestral/test_httpie_cli_utils_LazyChoices___iter___1_test_valid_inputs.py:3:0: E0611: No name 'get_simple_list' in module 'httpie.cli.utils' (no-name-in-module)


"""