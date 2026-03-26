
class SuperStringBase:
    def character_at(self, index):
        """
        Returns the character at the specified index in the string, converted to uppercase.

        Parameters:
            self (SuperStringBase): The instance of the SuperStringBase class from which this method is called.
            index (int): The position of the character to retrieve from the string. Indexing starts at 0.

        Returns:
            str: The character at the given index after converting it to uppercase. If the index is out of range, it raises an IndexError.

        Raises:
            IndexError: If the provided index is out of range for the string.
        """
        if not (0 <= index < len(self)):
            raise IndexError("Index out of bounds")
        return self[index].upper()

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