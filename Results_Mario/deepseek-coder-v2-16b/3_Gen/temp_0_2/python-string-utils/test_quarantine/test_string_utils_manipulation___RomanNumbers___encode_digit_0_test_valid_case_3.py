
class __RomanNumbers:
    __mappings = [{(1): 'I', (5): 'V'}, {(1): 'X', (5): 'L'}, {(1): 'C', (5): 'D'}, {(1): 'M'}]
    __reversed_mappings = [{v: k for k, v in m.items()} for m in __mappings]

    @classmethod
    def __encode_digit(cls, index: int, value: int) -> str:
        # if digit is zero, there is no sign to display
        if value == 0:
            return ''

        # from 1 to 3 we have just to repeat the sign N times (eg: III, XXX...)
        if value <= 3:
            return cls.__mappings[index][1] * value

        # if 4 we have to add unit prefix
        if value == 4:
            return cls.__mappings[index][1] + cls.__mappings[index][5]

        # if is 5, is a straight map
        if value == 5:
            return cls.__mappings[index][5]

        # if 6, 7 or 8 we have to append unit suffixes
        if value <= 8:
            suffix = cls.__mappings[index][1] * (value - 5)
            return cls.__mappings[index][5] + suffix

        # if 9 we have to prepend current unit to next
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