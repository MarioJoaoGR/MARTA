
import pytest
from xml.dom import minidom
from httpie.output.formatters.xml import pretty_xml

@pytest.mark.parametrize("doc, expected", [
    (minidom.parseString('<?xml version="1.0" encoding="UTF-8"?>\n<root>content</root>'), '<?xml version="1.0" encoding="UTF-8"?>\n<root>content</root>')
])
def test_valid_input(doc, expected):
    assert pretty_xml(doc) == expected

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

httpie/Test4DT_tests_codestral/test_httpie_output_formatters_xml_pretty_xml_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_ test_valid_input[doc0-<?xml version="1.0" encoding="UTF-8"?>\n<root>content</root>] _

doc = <xml.dom.minidom.Document object at 0x7febd18dae10>
expected = '<?xml version="1.0" encoding="UTF-8"?>\n<root>content</root>'

    @pytest.mark.parametrize("doc, expected", [
        (minidom.parseString('<?xml version="1.0" encoding="UTF-8"?>\n<root>content</root>'), '<?xml version="1.0" encoding="UTF-8"?>\n<root>content</root>')
    ])
    def test_valid_input(doc, expected):
>       assert pretty_xml(doc) == expected
E       assert '<root>content</root>' == '<?xml versio...ontent</root>'
E         
E         - <?xml version="1.0" encoding="UTF-8"?>
E           <root>content</root>

httpie/Test4DT_tests_codestral/test_httpie_output_formatters_xml_pretty_xml_0_test_valid_input.py:10: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_codestral.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_codestral/test_httpie_output_formatters_xml_pretty_xml_0_test_valid_input.py::test_valid_input[doc0-<?xml version="1.0" encoding="UTF-8"?>\n<root>content</root>]
============================== 1 failed in 0.16s ===============================
"""