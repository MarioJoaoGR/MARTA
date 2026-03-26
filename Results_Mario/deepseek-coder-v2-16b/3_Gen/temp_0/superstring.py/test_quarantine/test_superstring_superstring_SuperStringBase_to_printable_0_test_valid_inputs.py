
class SuperStringBase:

    def to_printable(self, start_index=None, end_index=None):
        """
        Returns a printable representation of the string. If no parameters are provided, it returns the entire string. 
        If 'start_index' and/or 'end_index' are specified, it returns the substring starting from 'start_index' (inclusive) 
        to 'end_index' (exclusive).

        Parameters:
            start_index (int): The index at which the substring should start. Defaults to None, meaning the beginning of the string.
            end_index (int): The index at which the substring should end. Defaults to None, meaning the end of the string.

        Returns:
            str: A printable representation of the string or its specified substring.

        Examples:
            >>> obj = SuperStringBase()
            >>> print(obj.to_printable())  # Outputs the entire string if no parameters are provided
            >>> print(obj.to_printable(2))  # Outputs the substring starting from index 2 to the end of the string
            >>> print(obj.to_printable(0, 5))  # Outputs the substring from index 0 (inclusive) to index 5 (exclusive)
        """
        if start_index is None and end_index is None:
            return str(self)
        elif start_index is not None and end_index is not None:
            return str(self)[start_index:end_index]
        elif start_index is not None:
            return str(self)[start_index:]
        elif end_index is not None:
            return str(self)[:end_index]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/superstring.py
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 0 items

--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
============================ no tests ran in 0.03s =============================
"""