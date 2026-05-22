
import pytest
from unittest.mock import patch
from httpie.output.formatters.colors import get_available_styles, BUNDLED_STYLES

@pytest.mark.parametrize("mocked_styles, expected", [
    (['default', 'friendly'], sorted(BUNDLED_STYLES | set(['default', 'friendly']))),
    ([], sorted(set([])))
])
def test_get_available_styles(mocked_styles, expected):
    with patch('pygments.styles.get_all_styles') as mock_get_all_styles:
        mock_get_all_styles.return_value = mocked_styles
        assert get_available_styles() == expected

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

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_formatters_colors_get_available_styles_4_test_edge_case.py . [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_____________ test_get_available_styles[mocked_styles1-expected1] ______________

mocked_styles = [], expected = []

    @pytest.mark.parametrize("mocked_styles, expected", [
        (['default', 'friendly'], sorted(BUNDLED_STYLES | set(['default', 'friendly']))),
        ([], sorted(set([])))
    ])
    def test_get_available_styles(mocked_styles, expected):
        with patch('pygments.styles.get_all_styles') as mock_get_all_styles:
            mock_get_all_styles.return_value = mocked_styles
>           assert get_available_styles() == expected
E           AssertionError: assert ['auto', <Pie..., 'solarized'] == []
E             
E             Left contains 5 more items, first extra item: 'auto'
E             Use -v to get more diff

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_formatters_colors_get_available_styles_4_test_edge_case.py:13: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_formatters_colors_get_available_styles_4_test_edge_case.py::test_get_available_styles[mocked_styles1-expected1]
========================= 1 failed, 1 passed in 0.26s ==========================
"""