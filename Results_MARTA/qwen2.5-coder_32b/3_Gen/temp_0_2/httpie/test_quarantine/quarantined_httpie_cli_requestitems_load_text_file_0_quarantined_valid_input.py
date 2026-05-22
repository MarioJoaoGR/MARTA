
import os
from httpie.cli.requestitems import KeyValueArg, ParseError
from unittest.mock import patch

def load_text_file(item: KeyValueArg) -> str:
    """
    Loads and returns the contents of a text file specified by the given path.

    Parameters:
        item (KeyValueArg): An object containing the path to the text file as its value, 
                            along with its original representation for error messages.

    Returns:
        str: The decoded content of the text file.

    Raises:
        ParseError: If there is an issue with reading or decoding the file, including if the file cannot be found or read, 
                    or if the content cannot be decoded as UTF-8 (which is typical for text files).
    """
    path = item.value
    try:
        with open(os.path.expanduser(path), 'rb') as f:
            return f.read().decode()
    except OSError as e:
        raise ParseError(f'{item.orig!r}: {e}')
    except UnicodeDecodeError:
        raise ParseError(
            f'{item.orig!r}: cannot embed the content of {item.value!r},'
        )

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/httpie
configfile: pytest.ini
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 0 items

--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
============================ no tests ran in 0.24s =============================
"""