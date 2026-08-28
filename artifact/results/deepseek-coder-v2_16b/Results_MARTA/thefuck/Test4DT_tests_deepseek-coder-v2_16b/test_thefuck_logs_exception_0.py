
import pytest
from unittest.mock import patch
from traceback import format_exception
import colorama
from thefuck.logs import exception

def test_exception_with_colorama():
    with patch('sys.stderr') as mock_stderr:
        title = "My Warning Title"
        exc_info = (ValueError, ValueError("An error occurred"), None)
        exception(title, exc_info)

        expected_output = u'{warn}[WARN] {title}:{reset}\n{trace}' \
                          u'{warn}----------------------------{reset}\n\n'.format(
            warn=colorama.Back.RED + colorama.Fore.WHITE + colorama.Style.BRIGHT,
            reset=colorama.Style.RESET_ALL,
            title=title,
            trace=''.join(format_exception(*exc_info)))
        
        mock_stderr.write.assert_called_with(expected_output)
