
from string_utils.manipulation import __RomanNumbers as RomanNumbers

class __RomanNumbers:
    __mappings = [{(1): 'I', (5): 'V'}, {(1): 'X', (5): 'L'}, {(1): 'C', (5): 'D'}, {(1): 'M'}]
    __reversed_mappings = [{v: k for k, v in m.items()} for m in __mappings]
    
    @classmethod
    def __encode_digit(cls, index: int, value: int) -> str:
        """
        Convert a single Roman numeral digit to its string representation.

        This method is used internally by the `__RomanNumbers.encode` method to convert each digit of the input number into its corresponding Roman numeral representation. It takes two parameters:

        - `index`: An integer representing the position of the digit in the original number, starting from 0 for units place up to 3 for thousands place.
        - `value`: An integer representing the value of the digit (1-9).

        The method returns a string representing the Roman numeral equivalent of the given digit.

        :param index: int - The position of the digit in the number, ranging from 0 to 3.
        :param value: int - The integer value of the digit (1-9).
        :return: str - A string representing the Roman numeral equivalent of the given digit.
        """
        if value == 0:
            return ''

        if value <= 3:
            return cls.__mappings[index][1] * value

        if value == 4:
            return cls.__mappings[index][1] + cls.__mappings[index][5]

        if value == 5:
            return cls.__mappings[index][5]

        if value <= 8:
            suffix = cls.__mappings[index][1] * (value - 5)
            return cls.__mappings[index][5] + suffix

        return cls.__mappings[index][1] + cls.__mappings[index + 1][1]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 0 items

--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
============================ no tests ran in 0.01s =============================

"""