
import pytest
from unittest.mock import MagicMock, patch
from httpie.output.processing import is_valid_mime

@pytest.mark.parametrize("mime, expected", [
    ("image/png", True),
    ("text/html", True),
    ("application/pdf", True),
    ("invalid-mime", False),
    (None, False),
    ("", False),
])
def test_is_valid_mime_basic(mime, expected):
    with patch('httpie.output.processing.MIME_RE', MagicMock()):
        mock_re = MagicMock()
        mock_re.match.return_value = None if mime == "invalid-mime" else True
        with patch('httpie.output.processing.MIME_RE', mock_re):
            assert is_valid_mime(mime) == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/httpie
configfile: pytest.ini
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 6 items

httpie/Test4DT_tests_codestral/test_httpie_output_processing_is_valid_mime_0_test_is_valid_mime_basic.py . [ 16%]
..FFF                                                                    [100%]

=================================== FAILURES ===================================
_________________ test_is_valid_mime_basic[invalid-mime-False] _________________

mime = 'invalid-mime', expected = False

    @pytest.mark.parametrize("mime, expected", [
        ("image/png", True),
        ("text/html", True),
        ("application/pdf", True),
        ("invalid-mime", False),
        (None, False),
        ("", False),
    ])
    def test_is_valid_mime_basic(mime, expected):
        with patch('httpie.output.processing.MIME_RE', MagicMock()):
            mock_re = MagicMock()
            mock_re.match.return_value = None if mime == "invalid-mime" else True
            with patch('httpie.output.processing.MIME_RE', mock_re):
>               assert is_valid_mime(mime) == expected
E               AssertionError: assert None == False
E                +  where None = is_valid_mime('invalid-mime')

httpie/Test4DT_tests_codestral/test_httpie_output_processing_is_valid_mime_0_test_is_valid_mime_basic.py:19: AssertionError
_____________________ test_is_valid_mime_basic[None-False] _____________________

mime = None, expected = False

    @pytest.mark.parametrize("mime, expected", [
        ("image/png", True),
        ("text/html", True),
        ("application/pdf", True),
        ("invalid-mime", False),
        (None, False),
        ("", False),
    ])
    def test_is_valid_mime_basic(mime, expected):
        with patch('httpie.output.processing.MIME_RE', MagicMock()):
            mock_re = MagicMock()
            mock_re.match.return_value = None if mime == "invalid-mime" else True
            with patch('httpie.output.processing.MIME_RE', mock_re):
>               assert is_valid_mime(mime) == expected
E               assert None == False
E                +  where None = is_valid_mime(None)

httpie/Test4DT_tests_codestral/test_httpie_output_processing_is_valid_mime_0_test_is_valid_mime_basic.py:19: AssertionError
_______________________ test_is_valid_mime_basic[-False] _______________________

mime = '', expected = False

    @pytest.mark.parametrize("mime, expected", [
        ("image/png", True),
        ("text/html", True),
        ("application/pdf", True),
        ("invalid-mime", False),
        (None, False),
        ("", False),
    ])
    def test_is_valid_mime_basic(mime, expected):
        with patch('httpie.output.processing.MIME_RE', MagicMock()):
            mock_re = MagicMock()
            mock_re.match.return_value = None if mime == "invalid-mime" else True
            with patch('httpie.output.processing.MIME_RE', mock_re):
>               assert is_valid_mime(mime) == expected
E               AssertionError: assert '' == False
E                +  where '' = is_valid_mime('')

httpie/Test4DT_tests_codestral/test_httpie_output_processing_is_valid_mime_0_test_is_valid_mime_basic.py:19: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_codestral.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_codestral/test_httpie_output_processing_is_valid_mime_0_test_is_valid_mime_basic.py::test_is_valid_mime_basic[invalid-mime-False]
FAILED httpie/Test4DT_tests_codestral/test_httpie_output_processing_is_valid_mime_0_test_is_valid_mime_basic.py::test_is_valid_mime_basic[None-False]
FAILED httpie/Test4DT_tests_codestral/test_httpie_output_processing_is_valid_mime_0_test_is_valid_mime_basic.py::test_is_valid_mime_basic[-False]
========================= 3 failed, 3 passed in 0.23s ==========================
"""