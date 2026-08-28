
import pytest
from pymonet.immutable_list import ImmutableList
from unittest.mock import patch


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b/test_pymonet_immutable_list_ImmutableList_unshift_0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_case ________________________________

    def test_valid_case():
        with patch('pymonet.immutable_list.ImmutableList.__init__', return_value=None):
            my_list = ImmutableList(is_empty=True)
>           new_list = my_list.unshift(1)

/opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b/test_pymonet_immutable_list_ImmutableList_unshift_0.py:9: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/pyMonet/pymonet/immutable_list.py:97: in unshift
    return ImmutableList(new_element) + self
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <pymonet.immutable_list.ImmutableList object at 0x7fee5b076dd0>
other = <pymonet.immutable_list.ImmutableList object at 0x7fee5b076da0>

    def __add__(self, other: 'ImmutableList[T]') -> 'ImmutableList[T]':
        """
        If Maybe is empty return new empty Maybe, in other case
        takes mapper function and returns result of mapper.
    
        :param mapper: function to call with Maybe.value
        :type mapper: Function(A) -> Maybe[B]
        :returns: Maybe[B | None]
        """
        if not isinstance(other, ImmutableList):
            raise ValueError('ImmutableList: you can not add any other instace than ImmutableList')
    
>       if self.tail is None:
E       AttributeError: 'ImmutableList' object has no attribute 'tail'

/opt/marta/baselines/codamosa/replication/test-apps/pyMonet/pymonet/immutable_list.py:39: AttributeError
________________________________ test_edge_case ________________________________

    def test_edge_case():
        with patch('pymonet.immutable_list.ImmutableList.__init__', return_value=None):
            empty_list = ImmutableList(is_empty=True)
>           new_empty_list = empty_list.unshift(None)

/opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b/test_pymonet_immutable_list_ImmutableList_unshift_0.py:16: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/pyMonet/pymonet/immutable_list.py:97: in unshift
    return ImmutableList(new_element) + self
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <pymonet.immutable_list.ImmutableList object at 0x7fee5b0f1ae0>
other = <pymonet.immutable_list.ImmutableList object at 0x7fee5b0f1b70>

    def __add__(self, other: 'ImmutableList[T]') -> 'ImmutableList[T]':
        """
        If Maybe is empty return new empty Maybe, in other case
        takes mapper function and returns result of mapper.
    
        :param mapper: function to call with Maybe.value
        :type mapper: Function(A) -> Maybe[B]
        :returns: Maybe[B | None]
        """
        if not isinstance(other, ImmutableList):
            raise ValueError('ImmutableList: you can not add any other instace than ImmutableList')
    
>       if self.tail is None:
E       AttributeError: 'ImmutableList' object has no attribute 'tail'

/opt/marta/baselines/codamosa/replication/test-apps/pyMonet/pymonet/immutable_list.py:39: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b/test_pymonet_immutable_list_ImmutableList_unshift_0.py::test_valid_case
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b/test_pymonet_immutable_list_ImmutableList_unshift_0.py::test_edge_case
============================== 2 failed in 0.08s ===============================
"""