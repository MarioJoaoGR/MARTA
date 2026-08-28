
import pytest
from pymonet.immutable_list import ImmutableList


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b/test_pymonet_immutable_list_ImmutableList___eq___0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
______________________________ test_valid_case_1 _______________________________

    def test_valid_case_1():
        sub_list = ImmutableList(head=2, tail=ImmutableList(head=3))
        list1 = ImmutableList(head=1, tail=sub_list)
>       assert list1 == ImmutableList(head=1, tail=ImmutableList(head=2))
E       assert <pymonet.immutable_list.ImmutableList object at 0x7fcf626c21a0> == <pymonet.immutable_list.ImmutableList object at 0x7fcf626c2140>
E        +  where <pymonet.immutable_list.ImmutableList object at 0x7fcf626c2140> = ImmutableList(head=1, tail=<pymonet.immutable_list.ImmutableList object at 0x7fcf626c21d0>)
E        +    where <pymonet.immutable_list.ImmutableList object at 0x7fcf626c21d0> = ImmutableList(head=2)

/opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b/test_pymonet_immutable_list_ImmutableList___eq___0.py:8: AssertionError
_______________________________ test_error_case ________________________________

    def test_error_case():
        list1 = ImmutableList(head=1, tail=ImmutableList(head=2))
        with pytest.raises(TypeError):
>           assert list1 == "not an ImmutableList"
E           AssertionError: assert <pymonet.immutable_list.ImmutableList object at 0x7fcf626c00d0> == 'not an ImmutableList'

/opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b/test_pymonet_immutable_list_ImmutableList___eq___0.py:13: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b/test_pymonet_immutable_list_ImmutableList___eq___0.py::test_valid_case_1
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b/test_pymonet_immutable_list_ImmutableList___eq___0.py::test_error_case
============================== 2 failed in 0.06s ===============================
"""