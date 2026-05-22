
from httpie.plugins.registry import plugin_manager
from collections import defaultdict
import importlib_metadata

class PluginInstaller:
    """
    A class for installing and listing plugins from a specified directory.

    Parameters:
        env (Environment): An environment object that provides access to configuration settings, standard input/output streams, etc. This is typically an instance of the Environment class provided by the application or framework using this PluginInstaller.
        debug (bool, optional): A flag indicating whether debugging information should be printed. Defaults to False.

    Attributes:
        env (Environment): The environment object containing configuration settings and I/O streams.
        dir (Path): The directory where plugins are located, derived from the environment's config.plugins_dir.
        debug (bool): A flag indicating whether debugging information should be printed.

    Methods:
        list(): Lists all known plugins by iterating over entry points in the specified directory and printing their names, versions, and groups.

    Examples:
        To create a PluginInstaller instance with an environment object for listing plugins:
        
        ```python
        from pathlib import Path
        class Environment:
            def __init__(self):
                self.config = type('Config', (), {'plugins_dir': Path('/path/to/plugins')})()
                self.stdout = DummyStdout()
        
        class DummyStdout:
            def write(self, text):
                print(text)
        
        env = Environment()
        installer = PluginInstaller(env=env, debug=True)
        installer.list()
        ```
    """
    def __init__(self, env: Environment, debug: bool = False) -> None:
        self.env = env
        self.dir = env.config.plugins_dir
        self.debug = debug

        self.setup_plugins_dir()

    def list(self) -> None:
        from httpie.plugins.registry import plugin_manager

        known_plugins = defaultdict(list)

        for entry_point in plugin_manager.iter_entry_points(self.dir):
            ep_info = (entry_point.group, entry_point.name)
            ep_name = get_dist_name(entry_point) or entry_point.module
            known_plugins[ep_name].append(ep_info)

        for plugin, entry_points in known_plugins.items():
            self.env.stdout.write(plugin)

            version = importlib_metadata.version(plugin)
            if version is not None:
                self.env.stdout.write(f' ({version})')
            self.env.stdout.write('\n')

            for group, entry_point in sorted(entry_points):
                self.env.stdout.write(f'  {entry_point} ({group})\n')

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_qwen2.5-coder_32b.test_httpie_manager_tasks_plugins_PluginInstaller_list_0_test_edge_case
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_manager_tasks_plugins_PluginInstaller_list_0_test_edge_case.py:41:28: E0602: Undefined variable 'Environment' (undefined-variable)
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_manager_tasks_plugins_PluginInstaller_list_0_test_edge_case.py:46:8: E1101: Instance of 'PluginInstaller' has no 'setup_plugins_dir' member (no-member)
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_manager_tasks_plugins_PluginInstaller_list_0_test_edge_case.py:55:22: E0602: Undefined variable 'get_dist_name' (undefined-variable)


"""