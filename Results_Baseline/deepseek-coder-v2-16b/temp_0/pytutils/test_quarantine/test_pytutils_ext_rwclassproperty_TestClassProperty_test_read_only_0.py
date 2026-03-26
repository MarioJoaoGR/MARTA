
from unittest import TestCase
try:
    from classproperty import meta  # Importing with a try-except block to handle the pylint error about module not found.
except ModuleNotFoundError:
    raise ModuleNotFoundError("The 'classproperty' module could not be imported.")

from pytutils.ext.rwclassproperty import TestClassProperty

# Assuming sentinel is defined somewhere in your codebase or as a placeholder for some test utility.
sentinel = type('Sentinel', (object,), {'nothing': None, 'get_only': None})()

class TestZ(TestCase):
    def test_read_only(self):
        class Z(object, metaclass=meta):
            _get_set = sentinel.nothing

            @classmethod
            def get_only(cls):
                return sentinel.get_only

        self.assertEqual(sentinel.get_only, Z.get_only())
        with self.assertRaises(AttributeError):
            setattr(Z, 'get_only', 123)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pytutils
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 0 items / 1 error

==================================== ERRORS ====================================
_ ERROR collecting Test4DT_tests/test_pytutils_ext_rwclassproperty_TestClassProperty_test_read_only_0.py _
ImportError while importing test module '/projects/F202407648IACDCF2/mario/pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_TestClassProperty_test_read_only_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_TestClassProperty_test_read_only_0.py:4: in <module>
    from classproperty import meta  # Importing with a try-except block to handle the pylint error about module not found.
E   ModuleNotFoundError: No module named 'classproperty'

During handling of the above exception, another exception occurred:
/usr/local/lib/python3.11/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_TestClassProperty_test_read_only_0.py:6: in <module>
    raise ModuleNotFoundError("The 'classproperty' module could not be imported.")
E   ModuleNotFoundError: The 'classproperty' module could not be imported.
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_TestClassProperty_test_read_only_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.14s ===============================
"""