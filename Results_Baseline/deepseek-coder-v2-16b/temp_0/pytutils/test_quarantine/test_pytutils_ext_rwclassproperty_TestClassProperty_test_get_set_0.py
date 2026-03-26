
from unittest import TestCase, mock
from pytutils.ext.rwclassproperty import TestClassProperty
from pytutils.ext.rwclassproperty import sentinel  # Assuming this is a module providing 'sentinel'

# Mocking necessary components for testing
class TestZ(TestCase):
    def test_get_set(self):
        get_only_cls = mock.MagicMock()
        get_set_get_cls = mock.MagicMock()
        get_set_set_cls = mock.MagicMock()

        class Z(object, metaclass=TestClassProperty.meta):
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
            with self.subTest(msg=msg):
                # Reset
                Z._get_set = sentinel.nothing

                # Test get_only
                self.assertEqual(sentinel.get_only, c.get_only)
                get_only_cls.assert_called_once_with(Z)
                get_only_cls.reset_mock()

                # Should return our initial "nothing" value
                self.assertEqual(sentinel.nothing, c.get_set)
                get_set_get_cls.assert_called_once_with(Z)
                get_set_get_cls.reset_mock()

                # Now test the set
                c.get_set = sentinel.get_set_val
                get_set_set_cls.assert_called_once_with(Z)
                get_set_set_cls.reset_mock()

                self.assertEqual(sentinel.get_set_val, c.get_set)
                get_set_get_cls.assert_called_once_with(Z)
                get_set_get_cls.reset_mock()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_ext_rwclassproperty_TestClassProperty_test_get_set_0
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_TestClassProperty_test_get_set_0.py:17:12: E0213: Method 'get_only' should have "self" as first argument (no-self-argument)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_TestClassProperty_test_get_set_0.py:16:13: E0602: Undefined variable 'classproperty' (undefined-variable)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_TestClassProperty_test_get_set_0.py:22:12: E0213: Method 'get_set' should have "self" as first argument (no-self-argument)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_TestClassProperty_test_get_set_0.py:21:13: E0602: Undefined variable 'classproperty' (undefined-variable)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_TestClassProperty_test_get_set_0.py:27:12: E0213: Method 'get_set' should have "self" as first argument (no-self-argument)


"""