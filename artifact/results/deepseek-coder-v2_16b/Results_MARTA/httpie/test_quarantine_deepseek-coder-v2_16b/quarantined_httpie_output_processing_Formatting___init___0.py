
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

../../../../../opt/marta/baselines/Results_MARTA/httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_processing_Formatting___init___0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
_________________________ test_default_initialization __________________________

    def test_default_initialization():
>       formatter = Formatting(groups=["group1"])

/opt/marta/baselines/Results_MARTA/httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_processing_Formatting___init___0.py:7: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <httpie.output.processing.Formatting object at 0x7fc51ea533d0>
groups = ['group1']
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
__________________________ test_custom_configuration ___________________________

    def test_custom_configuration():
>       formatter = Formatting(groups=["group1"], env=Environment(), format_options={"headers": True, "body": False})

/opt/marta/baselines/Results_MARTA/httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_processing_Formatting___init___0.py:12: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <httpie.output.processing.Formatting object at 0x7fc51ea8bd00>
groups = ['group1']
env = <Environment {'colors': 256,
 'config': {'default_options': []},
 'config_dir': PosixPath('/home/joaovitorino/.httpie'...IO name=6 mode='rb+' closefd=True>" mode='r+' encoding='utf-8'>,
 'stdout_encoding': 'utf-8',
 'stdout_isatty': False}>
kwargs = {'format_options': {'body': False, 'headers': True}}
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
____________________ test_using_different_processor_groups _____________________

    def test_using_different_processor_groups():
>       formatter = Formatting(groups=["group2"])

/opt/marta/baselines/Results_MARTA/httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_processing_Formatting___init___0.py:17: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <httpie.output.processing.Formatting object at 0x7fc51eabc9a0>
groups = ['group2']
env = <Environment {'colors': 256,
 'config': {'default_options': []},
 'config_dir': PosixPath('/home/joaovitorino/.httpie'...IO name=6 mode='rb+' closefd=True>" mode='r+' encoding='utf-8'>,
 'stdout_encoding': 'utf-8',
 'stdout_isatty': False}>
kwargs = {}
available_plugins = {'colors': [<class 'httpie.output.formatters.colors.ColorFormatter'>], 'format': [<class 'httpie.output.formatters.headers.HeadersFormatter'>, <class 'httpie.output.formatters.json.JSONFormatter'>]}
group = 'group2'

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
E           KeyError: 'group2'

/opt/marta/baselines/codamosa/replication/test-apps/httpie/httpie/output/processing.py:39: KeyError
=============================== warnings summary ===============================
../../../../../opt/marta/baselines/codamosa/replication/test-apps/httpie/httpie/plugins/manager.py:5
  /opt/marta/baselines/codamosa/replication/test-apps/httpie/httpie/plugins/manager.py:5: DeprecationWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html
    from pkg_resources import iter_entry_points

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_processing_Formatting___init___0.py::test_default_initialization
FAILED ../../../../../opt/marta/baselines/Results_MARTA/httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_processing_Formatting___init___0.py::test_custom_configuration
FAILED ../../../../../opt/marta/baselines/Results_MARTA/httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_processing_Formatting___init___0.py::test_using_different_processor_groups
========================= 3 failed, 1 warning in 0.40s =========================
"""