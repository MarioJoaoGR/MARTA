
import json
from pathlib import Path
from httpie.config import __version__

class BaseConfigDict:
    def __init__(self, path: Path):
        super().__init__()
        self.path = path
        self.__meta__ = {}

    def save(self, *, bump_version: bool = False):
        if bump_version or 'httpie' not in self.__meta__:
            self.__meta__['httpie'] = __version__
        if self.helpurl:
            self.__meta__['help'] = self.helpurl
        if self.about:
            self.__meta__['about'] = self.about

        self.ensure_directory()

        json_string = json.dumps(
            obj=self.post_process_data(self),
            indent=4,
            sort_keys=True,
            ensure_ascii=True,
        )
        self.path.write_text(json_string + '\n', encoding='UTF8')

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_codestral.test_httpie_config_BaseConfigDict_save_0_test_edge_cases
httpie/Test4DT_tests_codestral/test_httpie_config_BaseConfigDict_save_0_test_edge_cases.py:15:11: E1101: Instance of 'BaseConfigDict' has no 'helpurl' member (no-member)
httpie/Test4DT_tests_codestral/test_httpie_config_BaseConfigDict_save_0_test_edge_cases.py:16:36: E1101: Instance of 'BaseConfigDict' has no 'helpurl' member (no-member)
httpie/Test4DT_tests_codestral/test_httpie_config_BaseConfigDict_save_0_test_edge_cases.py:17:11: E1101: Instance of 'BaseConfigDict' has no 'about' member (no-member)
httpie/Test4DT_tests_codestral/test_httpie_config_BaseConfigDict_save_0_test_edge_cases.py:18:37: E1101: Instance of 'BaseConfigDict' has no 'about' member (no-member)
httpie/Test4DT_tests_codestral/test_httpie_config_BaseConfigDict_save_0_test_edge_cases.py:20:8: E1101: Instance of 'BaseConfigDict' has no 'ensure_directory' member (no-member)
httpie/Test4DT_tests_codestral/test_httpie_config_BaseConfigDict_save_0_test_edge_cases.py:23:16: E1101: Instance of 'BaseConfigDict' has no 'post_process_data' member (no-member)


"""