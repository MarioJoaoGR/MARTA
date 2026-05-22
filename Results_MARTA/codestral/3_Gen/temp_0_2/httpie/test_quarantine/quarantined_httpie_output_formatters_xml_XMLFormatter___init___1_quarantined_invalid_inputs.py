
import pytest
from httpie.output.formatters.xml import XMLFormatter

def test_invalid_inputs():
    with pytest.raises(TypeError):
        XMLFormatter()

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

httpie/Test4DT_tests_codestral/test_httpie_output_formatters_xml_XMLFormatter___init___1_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        with pytest.raises(TypeError):
>           XMLFormatter()

httpie/Test4DT_tests_codestral/test_httpie_output_formatters_xml_XMLFormatter___init___1_test_invalid_inputs.py:7: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
httpie/httpie/output/formatters/xml.py:56: in __init__
    super().__init__(**kwargs)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <httpie.output.formatters.xml.XMLFormatter object at 0x7fd55b26aa50>
kwargs = {}

    def __init__(self, **kwargs):
        """
        :param env: an class:`Environment` instance
        :param kwargs: additional keyword argument that some
                       formatters might require.
    
        """
        self.enabled = True
        self.kwargs = kwargs
>       self.format_options = kwargs['format_options']
E       KeyError: 'format_options'

httpie/httpie/plugins/base.py:140: KeyError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_codestral.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_codestral/test_httpie_output_formatters_xml_XMLFormatter___init___1_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.13s ===============================
"""