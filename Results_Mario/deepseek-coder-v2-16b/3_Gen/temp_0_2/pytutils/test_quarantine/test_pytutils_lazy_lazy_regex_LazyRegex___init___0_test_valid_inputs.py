
from pytutils.lazy import lazy_regex

class LazyRegex:
    """A proxy around a real regex, which won't be compiled until accessed."""
    _regex_attributes_to_copy = ['__copy__', '__deepcopy__', 'findall',
        'finditer', 'match', 'scanner', 'search', 'split', 'sub', 'subn']
    __slots__ = ['_real_regex', '_regex_args', '_regex_kwargs'
        ] + _regex_attributes_to_copy
    
    def __init__(self, args=(), kwargs={}):
        """Create a new proxy object, passing in the args to pass to re.compile

        :param args: The `*args` to pass to re.compile
        :param kwargs: The `**kwargs` to pass to re.compile
        """
        self._real_regex = None
        self._regex_args = args
        self._regex_kwargs = kwargs

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
============================ no tests ran in 0.05s =============================
"""