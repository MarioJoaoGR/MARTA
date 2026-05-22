
import argparse
from httpie.cli.options import ParserSpec
import unittest.mock as mock

def parser_to_parser_spec(parser: argparse.ArgumentParser, **kwargs) -> ParserSpec:
    """Take an existing argparse parser, and create a spec from it."""
    return ParserSpec(
        program=parser.prog,
        description=parser.description,
        epilog=parser.epilog,
        **kwargs
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
============================ no tests ran in 0.18s =============================
"""