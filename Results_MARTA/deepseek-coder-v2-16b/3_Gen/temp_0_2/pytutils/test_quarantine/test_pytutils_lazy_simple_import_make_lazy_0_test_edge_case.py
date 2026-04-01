
import sys
from types import ModuleType
from pytutils.lazy.simple_import import _LazyModuleMarker

def make_lazy(module_path):
    """
    Mark that this module should not be imported until an attribute is needed off of it.
    """
    sys_modules = sys.modules  # cache in the locals

    class LazyModule(_LazyModuleMarker):
        """
        A standin for a module to prevent it from being imported
        """
        def __getattribute__(self, attr):
            if 'module' not in self.__dict__:
                del sys_modules[module_path]
                module = __import__(module_path)
                self.module = module
                sys_modules[module_path] = module
            
            return getattr(self.module, attr)

    sys_modules[module_path] = LazyModule()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pytutils
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 0 items

--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
============================ no tests ran in 0.06s =============================
"""