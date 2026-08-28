
import pytest
from youtube_dl.jsinterp import JSInterpreter


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_jsinterp_JSInterpreter_call_function_0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_case ________________________________

    def test_valid_case():
        interpreter = JSInterpreter("function add(a, b) { return a + b; }")
>       result = interpreter.call_function('add', 3, 4)

/opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_jsinterp_JSInterpreter_call_function_0.py:7: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/youtube-dl/youtube_dl/jsinterp.py:252: in call_function
    return f(args)
/opt/marta/baselines/codamosa/replication/test-apps/youtube-dl/youtube_dl/jsinterp.py:258: in resf
    res, abort = self.interpret_statement(stmt, local_vars)
/opt/marta/baselines/codamosa/replication/test-apps/youtube-dl/youtube_dl/jsinterp.py:56: in interpret_statement
    v = self.interpret_expression(expr, local_vars, allow_recursion)
/opt/marta/baselines/codamosa/replication/test-apps/youtube-dl/youtube_dl/jsinterp.py:193: in interpret_expression
    y, abort = self.interpret_statement(
/opt/marta/baselines/codamosa/replication/test-apps/youtube-dl/youtube_dl/jsinterp.py:56: in interpret_statement
    v = self.interpret_expression(expr, local_vars, allow_recursion)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <youtube_dl.jsinterp.JSInterpreter object at 0x7fedd6aaca00>, expr = 'b'
local_vars = {' b': 4, 'a': 3}, allow_recursion = 99

    def interpret_expression(self, expr, local_vars, allow_recursion):
        expr = expr.strip()
        if expr == '':  # Empty expression
            return None
    
        if expr.startswith('('):
            parens_count = 0
            for m in re.finditer(r'[()]', expr):
                if m.group(0) == '(':
                    parens_count += 1
                else:
                    parens_count -= 1
                    if parens_count == 0:
                        sub_expr = expr[1:m.start()]
                        sub_result = self.interpret_expression(
                            sub_expr, local_vars, allow_recursion)
                        remaining_expr = expr[m.end():].strip()
                        if not remaining_expr:
                            return sub_result
                        else:
                            expr = json.dumps(sub_result) + remaining_expr
                        break
            else:
                raise ExtractorError('Premature end of parens in %r' % expr)
    
        for op, opfunc in _ASSIGN_OPERATORS:
            m = re.match(r'''(?x)
                (?P<out>%s)(?:\[(?P<index>[^\]]+?)\])?
                \s*%s
                (?P<expr>.*)$''' % (_NAME_RE, re.escape(op)), expr)
            if not m:
                continue
            right_val = self.interpret_expression(
                m.group('expr'), local_vars, allow_recursion - 1)
    
            if m.groupdict().get('index'):
                lvar = local_vars[m.group('out')]
                idx = self.interpret_expression(
                    m.group('index'), local_vars, allow_recursion)
                assert isinstance(idx, int)
                cur = lvar[idx]
                val = opfunc(cur, right_val)
                lvar[idx] = val
                return val
            else:
                cur = local_vars.get(m.group('out'))
                val = opfunc(cur, right_val)
                local_vars[m.group('out')] = val
                return val
    
        if expr.isdigit():
            return int(expr)
    
        var_m = re.match(
            r'(?!if|return|true|false)(?P<name>%s)$' % _NAME_RE,
            expr)
        if var_m:
>           return local_vars[var_m.group('name')]
E           KeyError: 'b'

/opt/marta/baselines/codamosa/replication/test-apps/youtube-dl/youtube_dl/jsinterp.py:116: KeyError
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        interpreter = JSInterpreter("function add(a, b) { return a + b; }")
        with pytest.raises(KeyError):
>           interpreter.call_function('multiply', 3, 4)

/opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_jsinterp_JSInterpreter_call_function_0.py:13: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/youtube-dl/youtube_dl/jsinterp.py:251: in call_function
    f = self.extract_function(funcname)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <youtube_dl.jsinterp.JSInterpreter object at 0x7fedd6aafa60>
funcname = 'multiply'

    def extract_function(self, funcname):
        func_m = re.search(
            r'''(?x)
                (?:function\s+%s|[{;,]\s*%s\s*=\s*function|var\s+%s\s*=\s*function)\s*
                \((?P<args>[^)]*)\)\s*
                \{(?P<code>[^}]+)\}''' % (
                re.escape(funcname), re.escape(funcname), re.escape(funcname)),
            self.code)
        if func_m is None:
>           raise ExtractorError('Could not find JS function %r' % funcname)
E           youtube_dl.utils.ExtractorError: Could not find JS function 'multiply'; please report this issue on https://yt-dl.org/bug . Make sure you are using the latest version; see  https://yt-dl.org/update  on how to update. Be sure to call youtube-dl with the --verbose flag and include its complete output.

/opt/marta/baselines/codamosa/replication/test-apps/youtube-dl/youtube_dl/jsinterp.py:245: ExtractorError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_jsinterp_JSInterpreter_call_function_0.py::test_valid_case
FAILED ../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_jsinterp_JSInterpreter_call_function_0.py::test_invalid_input
============================== 2 failed in 0.58s ===============================
"""