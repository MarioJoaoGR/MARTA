
import pytest
from youtube_dl.options import Option

def _format_option_string(option):
    """
    Formats an option string for command-line interfaces, combining short and long options with optional metavar.
    
    Parameters:
        option (object): An object representing a command-line option. This object should have attributes `_short_opts` and `_long_opts`, which are lists containing the short and long option strings respectively. It should also have a method `takes_value()` that returns whether the option takes an argument, and an attribute `metavar` for the metavar of the value if it does.
    
    Returns:
        str: A formatted string representing the combined short and long options with optional metavar. If there are both short and long options, they will be separated by a comma and space. If the option takes an argument, the metavar will be appended after a space.
    
    Examples:
        >>> _format_option_string(Option('-o', '--option'))
        '-o'
        
        >>> opt = Option('-o', '--option')
        >>> opt.metavar = 'METAVAR'
        >>> _format_option_string(opt)
        '-o, --option METAVAR'
    """
    opts = []

    if option._short_opts:
        opts.append(option._short_opts[0])
    if option._long_opts:
        opts.append(option._long_opts[0])
    if len(opts) > 1:
        opts.insert(1, ', ')

    if option.takes_value():
        opts.append(' %s' % option.metavar)

    return ''.join(opts)

# Test cases for _format_option_string function
def test_format_option_basic():
    opt = Option('-o', '--option')
    assert _format_option_string(opt) == '-o'

def test_format_option_with_metavar():
    opt = Option('-o', '--option')
    opt.metavar = 'METAVAR'
    assert _format_option_string(opt) == '-o, --option METAVAR'

def test_format_option_takes_value():
    opt = Option('-o', '--option')
    opt.metavar = 'VALUE'
    opt.takes_value()  # Ensure this method is defined and returns True for testing purposes
    assert _format_option_string(opt) == '-o, --option VALUE'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 0 items / 1 error

==================================== ERRORS ====================================
_____ ERROR collecting test_youtube_dl_options__format_option_string_0.py ______
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_options__format_option_string_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_options__format_option_string_0.py:3: in <module>
    from youtube_dl.options import Option
E   ImportError: cannot import name 'Option' from 'youtube_dl.options' (/opt/marta/baselines/codamosa/replication/test-apps/youtube-dl/youtube_dl/options.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_options__format_option_string_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.63s ===============================
"""