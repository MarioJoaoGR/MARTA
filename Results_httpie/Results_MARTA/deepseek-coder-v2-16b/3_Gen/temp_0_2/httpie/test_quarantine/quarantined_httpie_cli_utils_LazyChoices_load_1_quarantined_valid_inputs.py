
from unittest.mock import patch, Mock
import httpie.cli.utils

class TestLazyChoices:
    @patch('httpie.cli.utils.LazyChoices')
    def test_valid_inputs(self, mock_LazyChoices):
        # Arrange
        mock_getter = Mock()
        mock_getter.__iter__.return_value = [1, 2, 3]
        mock_LazyChoices.return_value.load.return_value = mock_getter

        # Act
        lazy_choices = httpie.cli.utils.LazyChoices(getter=lambda: [1, 2, 3])

        # Assert
        assert iter(lazy_choices) == [1, 2, 3]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/httpie
configfile: pytest.ini
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_cli_utils_LazyChoices_load_1_test_valid_inputs.py F [100%]

=================================== FAILURES ===================================
______________________ TestLazyChoices.test_valid_inputs _______________________

self = <test_httpie_cli_utils_LazyChoices_load_1_test_valid_inputs.TestLazyChoices object at 0x7f8983ce6d10>
mock_LazyChoices = <MagicMock name='LazyChoices' id='140228598920336'>

    @patch('httpie.cli.utils.LazyChoices')
    def test_valid_inputs(self, mock_LazyChoices):
        # Arrange
        mock_getter = Mock()
>       mock_getter.__iter__.return_value = [1, 2, 3]

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_cli_utils_LazyChoices_load_1_test_valid_inputs.py:10: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <Mock id='140228600202192'>, name = '__iter__'

    def __getattr__(self, name):
        if name in {'_mock_methods', '_mock_unsafe'}:
            raise AttributeError(name)
        elif self._mock_methods is not None:
            if name not in self._mock_methods or name in _all_magics:
                raise AttributeError("Mock object has no attribute %r" % name)
        elif _is_magic(name):
>           raise AttributeError(name)
E           AttributeError: __iter__

/usr/local/lib/python3.11/unittest/mock.py:655: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_cli_utils_LazyChoices_load_1_test_valid_inputs.py::TestLazyChoices::test_valid_inputs
============================== 1 failed in 0.18s ===============================
"""