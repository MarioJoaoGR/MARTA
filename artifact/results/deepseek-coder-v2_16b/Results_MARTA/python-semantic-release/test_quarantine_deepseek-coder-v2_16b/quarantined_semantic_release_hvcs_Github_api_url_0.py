
import pytest
from semantic_release.hvcs import Github


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_hvcs_Github_api_url_0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_____________________________ test_api_url_default _____________________________

    def test_api_url_default():
        """Test API URL without a custom domain."""
        config = {}
        with pytest.MonkeyPatch().context() as mp:
            mp.setattr('semantic_release.hvcs.config', lambda: config)
>           assert Github.api_url() == 'https://api.github.com'

/opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_hvcs_Github_api_url_0.py:10: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

    @staticmethod
    def api_url() -> str:
        """Github api_url property
    
        :return: The Github API URL
        """
        # not necessarily prefixed with api in the case of a custom domain, so
        # can't just default DEFAULT_DOMAIN to github.com
>       hvcs_domain = config.get("hvcs_domain")
E       AttributeError: 'function' object has no attribute 'get'

/opt/marta/baselines/codamosa/replication/test-apps/python-semantic-release/semantic_release/hvcs.py:114: AttributeError
__________________________ test_api_url_custom_domain __________________________

    def test_api_url_custom_domain():
        """Test API URL with a custom domain."""
        config = {"hvcs_domain": "customdomain.com"}
        with pytest.MonkeyPatch().context() as mp:
            mp.setattr('semantic_release.hvcs.config', lambda: config)
>           assert Github.api_url() == 'https://customdomain.com'

/opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_hvcs_Github_api_url_0.py:17: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

    @staticmethod
    def api_url() -> str:
        """Github api_url property
    
        :return: The Github API URL
        """
        # not necessarily prefixed with api in the case of a custom domain, so
        # can't just default DEFAULT_DOMAIN to github.com
>       hvcs_domain = config.get("hvcs_domain")
E       AttributeError: 'function' object has no attribute 'get'

/opt/marta/baselines/codamosa/replication/test-apps/python-semantic-release/semantic_release/hvcs.py:114: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_hvcs_Github_api_url_0.py::test_api_url_default
FAILED ../../../../../opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_hvcs_Github_api_url_0.py::test_api_url_custom_domain
============================== 2 failed in 0.24s ===============================
"""