
import pytest
from httpie.output.writer import write_stream_with_colors_win
from io import StringIO

@pytest.fixture
def setup_streams():
    stream = StringIO("This is \x1b[31mred\x1b[0m text.")
    outfile = StringIO()
    return stream, outfile

def test_write_stream_with_colors_win(setup_streams):
    stream, outfile = setup_streams
    write_stream_with_colors_win(stream, outfile, True)
    assert "\x1b[31mred\x1b[0m" in outfile.getvalue()

def test_write_stream_with_colors_win_flush(setup_streams):
    stream, outfile = setup_streams
    write_stream_with_colors_win(stream, outfile, True)
    assert "\x1b[31mred\x1b[0m" in outfile.getvalue()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/httpie
configfile: pytest.ini
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_writer_write_stream_with_colors_win_0_test_valid_input.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
______________________ test_write_stream_with_colors_win _______________________

setup_streams = (<_io.StringIO object at 0x7f558ba220e0>, <_io.StringIO object at 0x7f558ba21ab0>)

    def test_write_stream_with_colors_win(setup_streams):
        stream, outfile = setup_streams
>       write_stream_with_colors_win(stream, outfile, True)

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_writer_write_stream_with_colors_win_0_test_valid_input.py:14: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

stream = <_io.StringIO object at 0x7f558ba220e0>
outfile = <_io.StringIO object at 0x7f558ba21ab0>, flush = True

    def write_stream_with_colors_win(
        stream: 'BaseStream',
        outfile: TextIO,
        flush: bool
    ):
        """Like `write`, but colorized chunks are written as text
        directly to `outfile` to ensure it gets processed by colorama.
        Applies only to Windows and colorized terminal output.
    
        """
        color = b'\x1b['
        encoding = outfile.encoding
        for chunk in stream:
>           if color in chunk:
E           TypeError: 'in <string>' requires string as left operand, not bytes

httpie/httpie/output/writer.py:92: TypeError
___________________ test_write_stream_with_colors_win_flush ____________________

setup_streams = (<_io.StringIO object at 0x7f558b7c1b40>, <_io.StringIO object at 0x7f558b7c2440>)

    def test_write_stream_with_colors_win_flush(setup_streams):
        stream, outfile = setup_streams
>       write_stream_with_colors_win(stream, outfile, True)

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_writer_write_stream_with_colors_win_0_test_valid_input.py:19: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

stream = <_io.StringIO object at 0x7f558b7c1b40>
outfile = <_io.StringIO object at 0x7f558b7c2440>, flush = True

    def write_stream_with_colors_win(
        stream: 'BaseStream',
        outfile: TextIO,
        flush: bool
    ):
        """Like `write`, but colorized chunks are written as text
        directly to `outfile` to ensure it gets processed by colorama.
        Applies only to Windows and colorized terminal output.
    
        """
        color = b'\x1b['
        encoding = outfile.encoding
        for chunk in stream:
>           if color in chunk:
E           TypeError: 'in <string>' requires string as left operand, not bytes

httpie/httpie/output/writer.py:92: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_writer_write_stream_with_colors_win_0_test_valid_input.py::test_write_stream_with_colors_win
FAILED httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_writer_write_stream_with_colors_win_0_test_valid_input.py::test_write_stream_with_colors_win_flush
============================== 2 failed in 0.16s ===============================
"""