
import pytest
import argparse
from thefuck.conf import Settings


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/thefuck/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/thefuck/Test4DT_tests_deepseek-coder-v2_16b/test_thefuck_conf_Settings_init_0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
___________________________ test_valid_input_default ___________________________

    def test_valid_input_default():
        settings = Settings()
>       with pytest.raises(NotImplementedError):
E       Failed: DID NOT RAISE <class 'NotImplementedError'>

/opt/marta/baselines/Results_MARTA/thefuck/Test4DT_tests_deepseek-coder-v2_16b/test_thefuck_conf_Settings_init_0.py:8: Failed
__________________________ test_valid_input_with_args __________________________

    def test_valid_input_with_args():
        parser = argparse.ArgumentParser()
        parser.add_argument('--debug', action='store_true')
        args = parser.parse_args(['--debug'])
    
        settings = Settings(args=args)
        with pytest.raises(NotImplementedError):
>           settings.init(args)

/opt/marta/baselines/Results_MARTA/thefuck/Test4DT_tests_deepseek-coder-v2_16b/test_thefuck_conf_Settings_init_0.py:18: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/thefuck/thefuck/conf.py:34: in init
    self.update(self._settings_from_args(args))
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = {'args': Namespace(debug=True), 'user_dir': PosixPath('/home/joaovitorino/.thefuck')}
args = Namespace(debug=True)

    def _settings_from_args(self, args):
        """Loads settings from args."""
        if not args:
            return {}
    
        from_args = {}
>       if args.yes:
E       AttributeError: 'Namespace' object has no attribute 'yes'

/opt/marta/baselines/codamosa/replication/test-apps/thefuck/thefuck/conf.py:121: AttributeError
=============================== warnings summary ===============================
../../../../../opt/marta/baselines/codamosa/replication/test-apps/thefuck/thefuck/conf.py:1
  /opt/marta/baselines/codamosa/replication/test-apps/thefuck/thefuck/conf.py:1: DeprecationWarning: the imp module is deprecated in favour of importlib and slated for removal in Python 3.12; see the module's documentation for alternative uses
    from imp import load_source

test_thefuck_conf_Settings_init_0.py::test_valid_input_default
test_thefuck_conf_Settings_init_0.py::test_valid_input_with_args
  /opt/marta/baselines/codamosa/replication/test-apps/thefuck/thefuck/conf.py:52: UserWarning: Config path /home/joaovitorino/.thefuck is deprecated. Please move to /home/joaovitorino/.config/thefuck
    warn(u'Config path {} is deprecated. Please move to {}'.format(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/thefuck/Test4DT_tests_deepseek-coder-v2_16b/test_thefuck_conf_Settings_init_0.py::test_valid_input_default
FAILED ../../../../../opt/marta/baselines/Results_MARTA/thefuck/Test4DT_tests_deepseek-coder-v2_16b/test_thefuck_conf_Settings_init_0.py::test_valid_input_with_args
======================== 2 failed, 3 warnings in 0.14s =========================
"""