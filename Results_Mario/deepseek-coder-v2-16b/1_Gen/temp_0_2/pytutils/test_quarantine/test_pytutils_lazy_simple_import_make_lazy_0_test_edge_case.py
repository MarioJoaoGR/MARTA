
import sys
from types import ModuleType
from pytutils.lazy.simple_import import make_lazy as lazy_make_lazy

def make_lazy(module_path):
    """
    Mark that this module should not be imported until an attribute is needed off of it.
    """
    sys_modules = sys.modules  # cache in the locals

    # store our 'instance' data in the closure.
    if hasattr(sys, 'module'):
        module = sys.modules[__name__]
    else:
        module = None

    class LazyModule(_LazyModuleMarker):
        """
        A standin for a module to prevent it from being imported
        """
        def __mro__(self):
            """
            Override the __mro__ to fool `isinstance`.
            """
            # We don't use direct subclassing because `ModuleType` has an
            # incompatible metaclass base with object (they are both in c)
            # and we are overridding __getattribute__.
            # By putting a __mro__ method here, we can pass `isinstance`
            # checks without ever invoking our __getattribute__ function.
            return (LazyModule, ModuleType)

        def __getattribute__(self, attr):
            """
            Override __getattribute__ to hide the implementation details.
            """
            if module is None:
                del sys_modules[module_path]
                module = __import__(module_path)
                sys_modules[module_path] = module

            return getattr(module, attr)

    sys_modules[module_path] = LazyModule()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_lazy_simple_import_make_lazy_0_test_edge_case
pytutils/Test4DT_tests/test_pytutils_lazy_simple_import_make_lazy_0_test_edge_case.py:18:21: E0602: Undefined variable '_LazyModuleMarker' (undefined-variable)


"""