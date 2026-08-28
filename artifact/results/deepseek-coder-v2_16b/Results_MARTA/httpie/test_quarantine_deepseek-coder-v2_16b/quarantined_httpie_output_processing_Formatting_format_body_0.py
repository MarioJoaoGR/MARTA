
import pytest
from httpie.output.processing import Formatting
from httpie.context import Environment



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/httpie/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_processing_Formatting_format_body_0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
________________________ test_formatting_initialization ________________________

    def test_formatting_initialization():
>       formatter = Formatting(groups=["group1", "group2"], env=Environment())

/opt/marta/baselines/Results_MARTA/httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_processing_Formatting_format_body_0.py:7: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <httpie.output.processing.Formatting object at 0x7f9ec957ea10>
groups = ['group1', 'group2']
env = <Environment {'colors': 256,
 'config': {'default_options': []},
 'config_dir': PosixPath('/home/joaovitorino/.httpie'...IO name=6 mode='rb+' closefd=True>" mode='r+' encoding='utf-8'>,
 'stdout_encoding': 'utf-8',
 'stdout_isatty': False}>
kwargs = {}
available_plugins = {'colors': [<class 'httpie.output.formatters.colors.ColorFormatter'>], 'format': [<class 'httpie.output.formatters.headers.HeadersFormatter'>, <class 'httpie.output.formatters.json.JSONFormatter'>]}
group = 'group1'

    def __init__(self, groups: List[str], env=Environment(), **kwargs):
        """
        :param groups: names of processor groups to be applied
        :param env: Environment
        :param kwargs: additional keyword arguments for processors
    
        """
        available_plugins = plugin_manager.get_formatters_grouped()
        self.enabled_plugins = []
        for group in groups:
>           for cls in available_plugins[group]:
E           KeyError: 'group1'

/opt/marta/baselines/codamosa/replication/test-apps/httpie/httpie/output/processing.py:39: KeyError
______________________ test_formatting_with_custom_kwargs ______________________

    def test_formatting_with_custom_kwargs():
>       formatter = Formatting(groups=["group1"], env=Environment(), custom_arg="value")

/opt/marta/baselines/Results_MARTA/httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_processing_Formatting_format_body_0.py:11: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <httpie.output.processing.Formatting object at 0x7f9ec93c3a90>
groups = ['group1']
env = <Environment {'colors': 256,
 'config': {'default_options': []},
 'config_dir': PosixPath('/home/joaovitorino/.httpie'...IO name=6 mode='rb+' closefd=True>" mode='r+' encoding='utf-8'>,
 'stdout_encoding': 'utf-8',
 'stdout_isatty': False}>
kwargs = {'custom_arg': 'value'}
available_plugins = {'colors': [<class 'httpie.output.formatters.colors.ColorFormatter'>], 'format': [<class 'httpie.output.formatters.headers.HeadersFormatter'>, <class 'httpie.output.formatters.json.JSONFormatter'>]}
group = 'group1'

    def __init__(self, groups: List[str], env=Environment(), **kwargs):
        """
        :param groups: names of processor groups to be applied
        :param env: Environment
        :param kwargs: additional keyword arguments for processors
    
        """
        available_plugins = plugin_manager.get_formatters_grouped()
        self.enabled_plugins = []
        for group in groups:
>           for cls in available_plugins[group]:
E           KeyError: 'group1'

/opt/marta/baselines/codamosa/replication/test-apps/httpie/httpie/output/processing.py:39: KeyError
_________________________ test_formatting_format_body __________________________

    def test_formatting_format_body():
        class DummyFormatter:
            def __init__(self, **kwargs):
                self.kwargs = kwargs
    
            def format_body(self, content, mime):
                return f"{content} (formatted for {mime})"
    
>       formatter = Formatting(groups=["dummy"], env=Environment())

/opt/marta/baselines/Results_MARTA/httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_processing_Formatting_format_body_0.py:23: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <httpie.output.processing.Formatting object at 0x7f9ec93f3dc0>
groups = ['dummy']
env = <Environment {'colors': 256,
 'config': {'default_options': []},
 'config_dir': PosixPath('/home/joaovitorino/.httpie'...IO name=6 mode='rb+' closefd=True>" mode='r+' encoding='utf-8'>,
 'stdout_encoding': 'utf-8',
 'stdout_isatty': False}>
kwargs = {}
available_plugins = {'colors': [<class 'httpie.output.formatters.colors.ColorFormatter'>], 'format': [<class 'httpie.output.formatters.headers.HeadersFormatter'>, <class 'httpie.output.formatters.json.JSONFormatter'>]}
group = 'dummy'

    def __init__(self, groups: List[str], env=Environment(), **kwargs):
        """
        :param groups: names of processor groups to be applied
        :param env: Environment
        :param kwargs: additional keyword arguments for processors
    
        """
        available_plugins = plugin_manager.get_formatters_grouped()
        self.enabled_plugins = []
        for group in groups:
>           for cls in available_plugins[group]:
E           KeyError: 'dummy'

/opt/marta/baselines/codamosa/replication/test-apps/httpie/httpie/output/processing.py:39: KeyError
=============================== warnings summary ===============================
../../../../../opt/marta/baselines/codamosa/replication/test-apps/httpie/httpie/plugins/manager.py:5
  /opt/marta/baselines/codamosa/replication/test-apps/httpie/httpie/plugins/manager.py:5: DeprecationWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html
    from pkg_resources import iter_entry_points

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_processing_Formatting_format_body_0.py::test_formatting_initialization
FAILED ../../../../../opt/marta/baselines/Results_MARTA/httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_processing_Formatting_format_body_0.py::test_formatting_with_custom_kwargs
FAILED ../../../../../opt/marta/baselines/Results_MARTA/httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_processing_Formatting_format_body_0.py::test_formatting_format_body
========================= 3 failed, 1 warning in 0.43s =========================
"""