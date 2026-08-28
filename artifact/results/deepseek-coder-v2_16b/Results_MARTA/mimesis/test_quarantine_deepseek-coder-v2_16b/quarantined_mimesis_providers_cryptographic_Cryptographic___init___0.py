
import pytest
from mimesis.providers.cryptographic import Cryptographic



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_cryptographic_Cryptographic___init___0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
_________________________ test_default_initialization __________________________

    def test_default_initialization():
        cryptographic_data = Cryptographic()
>       assert hasattr(cryptographic_data, '_locale'), "Expected _locale attribute to be present"
E       AssertionError: Expected _locale attribute to be present
E       assert False
E        +  where False = hasattr(<mimesis.providers.cryptographic.Cryptographic object at 0x7f8d7f3613c0>, '_locale')

/opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_cryptographic_Cryptographic___init___0.py:7: AssertionError
______________________ test_custom_locale_initialization _______________________

    def test_custom_locale_initialization():
>       cryptographic_data = Cryptographic(locale='es')

/opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_cryptographic_Cryptographic___init___0.py:10: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <mimesis.providers.cryptographic.Cryptographic object at 0x7f8d7f363820>
args = (), kwargs = {'locale': 'es'}

    def __init__(self, *args, **kwargs) -> None:
        """Initialize attributes.
    
        :param seed: Seed.
        """
>       super().__init__(*args, **kwargs)
E       TypeError: BaseProvider.__init__() got an unexpected keyword argument 'locale'

/opt/marta/baselines/codamosa/replication/test-apps/mimesis/mimesis/providers/cryptographic.py:25: TypeError
__________________________ test_invalid_locale_error ___________________________

    def test_invalid_locale_error():
        with pytest.raises(TypeError) as e:
            Cryptographic(locale='xyz')
>       assert str(e.value) == "Cryptographic.__init__() got an unexpected keyword argument 'locale'", f"Expected TypeError but got {str(e.value)}"
E       AssertionError: Expected TypeError but got BaseProvider.__init__() got an unexpected keyword argument 'locale'
E       assert "BaseProvider...ment 'locale'" == "Cryptographi...ment 'locale'"
E         
E         - Cryptographic.__init__() got an unexpected keyword argument 'locale'
E         ? ^ --- ^ -----
E         + BaseProvider.__init__() got an unexpected keyword argument 'locale'
E         ? ^^^^^  ^^^^

/opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_cryptographic_Cryptographic___init___0.py:16: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_cryptographic_Cryptographic___init___0.py::test_default_initialization
FAILED ../../../../../opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_cryptographic_Cryptographic___init___0.py::test_custom_locale_initialization
FAILED ../../../../../opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_cryptographic_Cryptographic___init___0.py::test_invalid_locale_error
============================== 3 failed in 0.12s ===============================
"""