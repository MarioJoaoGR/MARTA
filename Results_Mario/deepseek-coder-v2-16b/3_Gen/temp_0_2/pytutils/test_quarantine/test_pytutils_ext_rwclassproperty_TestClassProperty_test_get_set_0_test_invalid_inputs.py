
from unittest.mock import MagicMock, sentinel
from pytutils.ext.rwclassproperty import classproperty
import pytest

class TestClassProperty:
    def test_get_set(self):
        get_only_cls = MagicMock()
        get_set_get_cls = MagicMock()
        get_set_set_cls = MagicMock()

        class Z(object, metaclass=classproperty.meta):
            _get_set = sentinel.nothing

            @classproperty
            def get_only(cls):
                get_only_cls(cls)
                return sentinel.get_only

            @classproperty
            def get_set(cls):
                get_set_get_cls(cls)
                return cls._get_set

            @get_set.setter
            def get_set(cls, value):
                get_set_set_cls(cls)
                cls._get_set = value

        for c, msg in [(Z, "class"), (Z(), "instance")]:
            with pytest.subTest(msg=msg):
                # Reset
                Z._get_set = sentinel.nothing

                # Test get_only
                assert sentinel.get_only == c.get_only()
                get_only_cls.assert_called_once_with(Z)
                get_only_cls.reset_mock()

                # Should return our initial "nothing" value
                assert sentinel.nothing == c.get_set()
                get_set_get_cls.assert_called_once_with(Z)
                get_set_get_cls.reset_mock()

                # Now test the set
                c.get_set = sentinel.get_set_val
                assert sentinel.get_set_val == c.get_set()
                get_set_set_cls.assert_called_once_with(Z)
                get_set_set_cls.reset_mock()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_ext_rwclassproperty_TestClassProperty_test_get_set_0_test_invalid_inputs
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_TestClassProperty_test_get_set_0_test_invalid_inputs.py:16:12: E0213: Method 'get_only' should have "self" as first argument (no-self-argument)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_TestClassProperty_test_get_set_0_test_invalid_inputs.py:21:12: E0213: Method 'get_set' should have "self" as first argument (no-self-argument)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_TestClassProperty_test_get_set_0_test_invalid_inputs.py:26:12: E0213: Method 'get_set' should have "self" as first argument (no-self-argument)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_TestClassProperty_test_get_set_0_test_invalid_inputs.py:31:17: E1101: Module 'pytest' has no 'subTest' member (no-member)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_TestClassProperty_test_get_set_0_test_invalid_inputs.py:36:44: E1120: No value for argument 'cls' in unbound method call (no-value-for-parameter)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_TestClassProperty_test_get_set_0_test_invalid_inputs.py:41:43: E1120: No value for argument 'cls' in unbound method call (no-value-for-parameter)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_TestClassProperty_test_get_set_0_test_invalid_inputs.py:41:43: E1120: No value for argument 'value' in unbound method call (no-value-for-parameter)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_TestClassProperty_test_get_set_0_test_invalid_inputs.py:47:47: E1120: No value for argument 'cls' in unbound method call (no-value-for-parameter)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_TestClassProperty_test_get_set_0_test_invalid_inputs.py:47:47: E1120: No value for argument 'value' in unbound method call (no-value-for-parameter)


"""