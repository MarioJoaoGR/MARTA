
import pytest
from flutils.namedtupleutils import _to_namedtuple


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b/test_flutils_namedtupleutils__to_namedtuple_0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
____________________________ test_valid_input_dict _____________________________

    def test_valid_input_dict():
        result = _to_namedtuple({'key': 'value'}, _started=True)
>       assert result == {'key': 'value'}
E       AssertionError: assert NamedTuple(key='value') == {'key': 'value'}
E         
E         Use -v to get more diff

/opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b/test_flutils_namedtupleutils__to_namedtuple_0.py:7: AssertionError
___________________________ test_error_invalid_type ____________________________

    def test_error_invalid_type():
        with pytest.raises(TypeError) as e:
            _to_namedtuple('not supported', _started=False)
        expected_message = "Can convert only 'list', 'tuple', 'dict' to a NamedTuple; got: (str) not supported"
>       assert str(e.value) == expected_message
E       AssertionError: assert 'Can convert ...not supported' == 'Can convert ...not supported'
E         
E         Skipping 54 identical leading characters in diff, use -v to show
E         - le; got: (str) not supported
E         + le; got: ('str') not supported
E         ?           +   +

/opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b/test_flutils_namedtupleutils__to_namedtuple_0.py:13: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b/test_flutils_namedtupleutils__to_namedtuple_0.py::test_valid_input_dict
FAILED ../../../../../opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b/test_flutils_namedtupleutils__to_namedtuple_0.py::test_error_invalid_type
============================== 2 failed in 0.07s ===============================
"""