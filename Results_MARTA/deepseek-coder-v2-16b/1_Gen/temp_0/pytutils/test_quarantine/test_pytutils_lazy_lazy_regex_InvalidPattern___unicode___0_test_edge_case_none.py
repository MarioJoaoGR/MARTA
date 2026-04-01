
class InvalidPattern:
    _fmt = 'Invalid pattern(s) found. %(msg)s'
    
    def __init__(self, msg):
        self.msg = msg

    def __unicode__(self):
        return self._format()

    def _format(self):
        """
        A helper method that constructs the error message using the format string and the instance's custom message.
        
        Returns:
            str: The formatted error string with the custom message integrated into the default format string.
        """
        return self._fmt % {'msg': self.msg}

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
============================ no tests ran in 0.04s =============================
"""