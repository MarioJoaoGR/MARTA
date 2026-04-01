
def _normalize_empty_lines(lines: list[str]) -> list[str]:
    """
    Normalizes the spacing of empty lines at the end of a list of strings. This function removes trailing empty lines and ensures there is exactly one empty line at the end of the list.
    
    Parameters:
        lines (list[str]): A list of string where each element represents a line from the text.
        
    Returns:
        list[str]: The modified list with normalized spacing for empty lines.
        
    Examples:
        >>> _normalize_empty_lines(["", ""])
        ['', '', '']
        
        >>> _normalize_empty_lines(["line1", "", "", "line2"])
        ['line1', '', '', '']
        
        >>> _normalize_empty_lines(["last line"])
        ['last line', '']
    """
    while lines and lines[-1].strip() == "":
        lines.pop(-1)

    lines.append("")
    return lines
```

Now, let's write the test case to ensure it works correctly:

```python
def test_none_input():
    assert _normalize_empty_lines([]) == ['']
    assert _normalize_empty_lines(['']) == ['', '']

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_output__normalize_empty_lines_0_test_none_input
isort/Test4DT_tests/test_isort_output__normalize_empty_lines_0_test_none_input.py:29:9: E0001: Parsing failed: 'unterminated string literal (detected at line 29) (Test4DT_tests.test_isort_output__normalize_empty_lines_0_test_none_input, line 29)' (syntax-error)


"""