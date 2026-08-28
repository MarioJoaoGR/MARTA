
import pytest
from youtube_dl.jsinterp import JSInterpreter
import re

def remove_quotes(name):
    if name.startswith('"') or name.startswith("'"):
        return name[1:-1]
    return name

def build_function(argnames, code):
    def func(*args):
        local_vars = {arg: val for arg, val in zip(argnames, args)}
        exec(code, {}, local_vars)
        return local_vars['return'] if 'return' in local_vars else None
    return func

class TestJSInterpreter:
    
    @pytest.fixture
    def interpreter(self):
        code = "var obj = { add(a, b) { return a + b; }, subtract(a, b) { return a - b; } };"
        return JSInterpreter(code)

    def test_valid_input(self, interpreter):
        functions = interpreter.extract_object('obj')
        assert 'add' in functions
        assert callable(functions['add'])
        assert functions['add'](5, 3) == 8
        
        assert 'subtract' in functions
        assert callable(functions['subtract'])
        assert functions['subtract'](5, 3) == 2

    def test_invalid_input(self, interpreter):
        with pytest.raises(AttributeError):
            functions = interpreter.extract_object('invalidObj')
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_jsinterp_JSInterpreter_extract_object_0.py F [ 50%]
.                                                                        [100%]

=================================== FAILURES ===================================
______________________ TestJSInterpreter.test_valid_input ______________________

self = <test_youtube_dl_jsinterp_JSInterpreter_extract_object_0.TestJSInterpreter object at 0x7f775427a740>
interpreter = <youtube_dl.jsinterp.JSInterpreter object at 0x7f775427ab00>

    def test_valid_input(self, interpreter):
>       functions = interpreter.extract_object('obj')

/opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_jsinterp_JSInterpreter_extract_object_0.py:26: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <youtube_dl.jsinterp.JSInterpreter object at 0x7f775427ab00>
objname = 'obj'

    def extract_object(self, objname):
        _FUNC_NAME_RE = r'''(?:[a-zA-Z$0-9]+|"[a-zA-Z$0-9]+"|'[a-zA-Z$0-9]+')'''
        obj = {}
        obj_m = re.search(
            r'''(?x)
                (?<!this\.)%s\s*=\s*{\s*
                    (?P<fields>(%s\s*:\s*function\s*\(.*?\)\s*{.*?}(?:,\s*)?)*)
                }\s*;
            ''' % (re.escape(objname), _FUNC_NAME_RE),
            self.code)
>       fields = obj_m.group('fields')
E       AttributeError: 'NoneType' object has no attribute 'group'

/opt/marta/baselines/codamosa/replication/test-apps/youtube-dl/youtube_dl/jsinterp.py:223: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_jsinterp_JSInterpreter_extract_object_0.py::TestJSInterpreter::test_valid_input
========================= 1 failed, 1 passed in 0.61s ==========================
"""