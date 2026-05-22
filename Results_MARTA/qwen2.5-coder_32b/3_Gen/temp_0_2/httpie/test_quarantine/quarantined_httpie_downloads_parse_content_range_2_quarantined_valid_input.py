
import re
from httpie.downloads import parse_content_range, ContentRangeError

def test_valid_input():
    content_range = 'bytes 0-100/100'
    resumed_from = 0
    assert parse_content_range(content_range, resumed_from) == 101

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/httpie
configfile: pytest.ini
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_downloads_parse_content_range_2_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        content_range = 'bytes 0-100/100'
        resumed_from = 0
>       assert parse_content_range(content_range, resumed_from) == 101

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_downloads_parse_content_range_2_test_valid_input.py:8: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

content_range = 'bytes 0-100/100', resumed_from = 0

    def parse_content_range(content_range: str, resumed_from: int) -> int:
        """
        Parse and validate Content-Range header.
    
        <https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html>
    
        :param content_range: the value of a Content-Range response header
                              eg. "bytes 21010-47021/47022"
        :param resumed_from: first byte pos. from the Range request header
        :return: total size of the response body when fully downloaded.
    
        """
        if content_range is None:
            raise ContentRangeError('Missing Content-Range')
    
        pattern = (
            r'^bytes (?P<first_byte_pos>\d+)-(?P<last_byte_pos>\d+)'
            r'/(\*|(?P<instance_length>\d+))$'
        )
        match = re.match(pattern, content_range)
    
        if not match:
            raise ContentRangeError(
                f'Invalid Content-Range format {content_range!r}')
    
        content_range_dict = match.groupdict()
        first_byte_pos = int(content_range_dict['first_byte_pos'])
        last_byte_pos = int(content_range_dict['last_byte_pos'])
        instance_length = (
            int(content_range_dict['instance_length'])
            if content_range_dict['instance_length']
            else None
        )
    
        # "A byte-content-range-spec with a byte-range-resp-spec whose
        # last- byte-pos value is less than its first-byte-pos value,
        # or whose instance-length value is less than or equal to its
        # last-byte-pos value, is invalid. The recipient of an invalid
        # byte-content-range- spec MUST ignore it and any content
        # transferred along with it."
        if (first_byte_pos > last_byte_pos
            or (instance_length is not None
                and instance_length <= last_byte_pos)):
>           raise ContentRangeError(
                f'Invalid Content-Range returned: {content_range!r}')
E           httpie.downloads.ContentRangeError: Invalid Content-Range returned: 'bytes 0-100/100'

httpie/httpie/downloads.py:70: ContentRangeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_downloads_parse_content_range_2_test_valid_input.py::test_valid_input
============================== 1 failed in 0.21s ===============================
"""