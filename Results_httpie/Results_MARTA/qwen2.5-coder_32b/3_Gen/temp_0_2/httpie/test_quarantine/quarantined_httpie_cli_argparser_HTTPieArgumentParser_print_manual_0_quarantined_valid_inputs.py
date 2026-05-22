
import argparse
from unittest.mock import patch, MagicMock

class HTTPieHelpFormatter(argparse.HelpFormatter):
    pass

class HTTPieArgumentParser(argparse.ArgumentParser):
    def __init__(self, *args, formatter_class=HTTPieHelpFormatter, **kwargs):
        kwargs.setdefault('add_help', False)
        super().__init__(*args, formatter_class=formatter_class, **kwargs)

    @patch('httpie.output.ui.man_pages')
    def print_manual(self, man_pages):
        if man_pages.is_available(self.env.program_name):
            man_pages.display_for(self.env, self.env.program_name)
            return None

        text = self.format_help()
        with self.env.rich_console.pager():
            self.env.rich_console.print(text, highlight=False)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_qwen2.5-coder_32b.test_httpie_cli_argparser_HTTPieArgumentParser_print_manual_0_test_valid_inputs
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_cli_argparser_HTTPieArgumentParser_print_manual_0_test_valid_inputs.py:15:34: E1101: Instance of 'HTTPieArgumentParser' has no 'env' member (no-member)
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_cli_argparser_HTTPieArgumentParser_print_manual_0_test_valid_inputs.py:16:34: E1101: Instance of 'HTTPieArgumentParser' has no 'env' member (no-member)
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_cli_argparser_HTTPieArgumentParser_print_manual_0_test_valid_inputs.py:16:44: E1101: Instance of 'HTTPieArgumentParser' has no 'env' member (no-member)
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_cli_argparser_HTTPieArgumentParser_print_manual_0_test_valid_inputs.py:20:13: E1101: Instance of 'HTTPieArgumentParser' has no 'env' member (no-member)
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_cli_argparser_HTTPieArgumentParser_print_manual_0_test_valid_inputs.py:21:12: E1101: Instance of 'HTTPieArgumentParser' has no 'env' member (no-member)


"""