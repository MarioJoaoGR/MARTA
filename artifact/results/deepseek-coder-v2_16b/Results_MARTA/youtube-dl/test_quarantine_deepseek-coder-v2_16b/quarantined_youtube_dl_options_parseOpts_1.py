
import pytest
from youtube_dl.options import parseOpts


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_options_parseOpts_1.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

self = <optparse.OptionParser object at 0x7f9cdf9320b0>
args = ['--json-report', '--json-report-file=pytest_report_deepseek-coder-v2_16b.json']
values = <Values at 0x7f9cdf7983d0: {'update_self': None, 'ignoreerrors': False, 'dump_user_agent': False, 'list_extractors': F...'fixup': 'detect_or_warn', 'prefer_ffmpeg': None, 'ffmpeg_location': None, 'exec_cmd': None, 'convertsubtitles': None}>

    def parse_args(self, args=None, values=None):
        """
        parse_args(args : [string] = sys.argv[1:],
                   values : Values = None)
        -> (values : Values, args : [string])
    
        Parse the command-line options found in 'args' (default:
        sys.argv[1:]).  Any errors result in a call to 'error()', which
        by default prints the usage message to stderr and calls
        sys.exit() with an error message.  On success returns a pair
        (values, args) where 'values' is a Values instance (with all
        your option values) and 'args' is the list of arguments left
        over after parsing options.
        """
        rargs = self._get_args(args)
        if values is None:
            values = self.get_default_values()
    
        # Store the halves of the argument list as attributes for the
        # convenience of callbacks:
        #   rargs
        #     the rest of the command-line (the "r" stands for
        #     "remaining" or "right-hand")
        #   largs
        #     the leftover arguments -- ie. what's left after removing
        #     options and their arguments (the "l" stands for "leftover"
        #     or "left-hand")
        self.rargs = rargs
        self.largs = largs = []
        self.values = values
    
        try:
>           stop = self._process_args(largs, rargs, values)

/opt/conda/envs/test4py_env/lib/python3.10/optparse.py:1387: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/conda/envs/test4py_env/lib/python3.10/optparse.py:1427: in _process_args
    self._process_long_opt(rargs, values)
/opt/conda/envs/test4py_env/lib/python3.10/optparse.py:1480: in _process_long_opt
    opt = self._match_long_opt(opt)
/opt/conda/envs/test4py_env/lib/python3.10/optparse.py:1465: in _match_long_opt
    return _match_abbrev(opt, self._long_opt)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

s = '--json-report'
wordmap = {'--abort-on-error': <Option at 0x7f9cdf9323b0: --abort-on-error>, '--abort-on-unavailable-fragment': <Option at 0x7f9...d-header': <Option at 0x7f9cdf933520: --add-header>, '--add-metadata': <Option at 0x7f9cdf798220: --add-metadata>, ...}

    def _match_abbrev(s, wordmap):
        """_match_abbrev(s : string, wordmap : {string : Option}) -> string
    
        Return the string key in 'wordmap' for which 's' is an unambiguous
        abbreviation.  If 's' is found to be ambiguous or doesn't match any of
        'words', raise BadOptionError.
        """
        # Is there an exact match?
        if s in wordmap:
            return s
        else:
            # Isolate all words with s as a prefix.
            possibilities = [word for word in wordmap.keys()
                             if word.startswith(s)]
            # No exact match, so there had better be just one possibility.
            if len(possibilities) == 1:
                return possibilities[0]
            elif not possibilities:
>               raise BadOptionError(s)
E               optparse.BadOptionError: no such option: --json-report

/opt/conda/envs/test4py_env/lib/python3.10/optparse.py:1670: BadOptionError

During handling of the above exception, another exception occurred:

    def test_valid_inputs():
>       parser, opts, args = parseOpts(['--json-report', '--json-report-file=pytest_report_deepseek-coder-v2_16b.json'])

/opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_options_parseOpts_1.py:6: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/youtube-dl/youtube_dl/options.py:882: in parseOpts
    opts, args = parser.parse_args(overrideArguments)
/opt/conda/envs/test4py_env/lib/python3.10/optparse.py:1389: in parse_args
    self.error(str(err))
/opt/conda/envs/test4py_env/lib/python3.10/optparse.py:1569: in error
    self.exit(2, "%s: error: %s\n" % (self.get_prog_name(), msg))
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <optparse.OptionParser object at 0x7f9cdf9320b0>, status = 2
msg = '__main__.py: error: no such option: --json-report\n'

    def exit(self, status=0, msg=None):
        if msg:
            sys.stderr.write(msg)
>       sys.exit(status)
E       SystemExit: 2

/opt/conda/envs/test4py_env/lib/python3.10/optparse.py:1559: SystemExit
----------------------------- Captured stderr call -----------------------------
Usage: __main__.py [OPTIONS] URL [URL...]

__main__.py: error: no such option: --json-report
_______________________________ test_edge_cases ________________________________

self = <optparse.OptionParser object at 0x7f9cdf809840>
args = ['--json-report', '--json-report-file=pytest_report_deepseek-coder-v2_16b.json']
values = <Values at 0x7f9cdf80a4a0: {'update_self': None, 'ignoreerrors': False, 'dump_user_agent': False, 'list_extractors': F...'fixup': 'detect_or_warn', 'prefer_ffmpeg': None, 'ffmpeg_location': None, 'exec_cmd': None, 'convertsubtitles': None}>

    def parse_args(self, args=None, values=None):
        """
        parse_args(args : [string] = sys.argv[1:],
                   values : Values = None)
        -> (values : Values, args : [string])
    
        Parse the command-line options found in 'args' (default:
        sys.argv[1:]).  Any errors result in a call to 'error()', which
        by default prints the usage message to stderr and calls
        sys.exit() with an error message.  On success returns a pair
        (values, args) where 'values' is a Values instance (with all
        your option values) and 'args' is the list of arguments left
        over after parsing options.
        """
        rargs = self._get_args(args)
        if values is None:
            values = self.get_default_values()
    
        # Store the halves of the argument list as attributes for the
        # convenience of callbacks:
        #   rargs
        #     the rest of the command-line (the "r" stands for
        #     "remaining" or "right-hand")
        #   largs
        #     the leftover arguments -- ie. what's left after removing
        #     options and their arguments (the "l" stands for "leftover"
        #     or "left-hand")
        self.rargs = rargs
        self.largs = largs = []
        self.values = values
    
        try:
>           stop = self._process_args(largs, rargs, values)

/opt/conda/envs/test4py_env/lib/python3.10/optparse.py:1387: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/conda/envs/test4py_env/lib/python3.10/optparse.py:1427: in _process_args
    self._process_long_opt(rargs, values)
/opt/conda/envs/test4py_env/lib/python3.10/optparse.py:1480: in _process_long_opt
    opt = self._match_long_opt(opt)
/opt/conda/envs/test4py_env/lib/python3.10/optparse.py:1465: in _match_long_opt
    return _match_abbrev(opt, self._long_opt)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

s = '--json-report'
wordmap = {'--abort-on-error': <Option at 0x7f9cdf8097b0: --abort-on-error>, '--abort-on-unavailable-fragment': <Option at 0x7f9...d-header': <Option at 0x7f9cdf80b010: --add-header>, '--add-metadata': <Option at 0x7f9cdf80a380: --add-metadata>, ...}

    def _match_abbrev(s, wordmap):
        """_match_abbrev(s : string, wordmap : {string : Option}) -> string
    
        Return the string key in 'wordmap' for which 's' is an unambiguous
        abbreviation.  If 's' is found to be ambiguous or doesn't match any of
        'words', raise BadOptionError.
        """
        # Is there an exact match?
        if s in wordmap:
            return s
        else:
            # Isolate all words with s as a prefix.
            possibilities = [word for word in wordmap.keys()
                             if word.startswith(s)]
            # No exact match, so there had better be just one possibility.
            if len(possibilities) == 1:
                return possibilities[0]
            elif not possibilities:
>               raise BadOptionError(s)
E               optparse.BadOptionError: no such option: --json-report

/opt/conda/envs/test4py_env/lib/python3.10/optparse.py:1670: BadOptionError

During handling of the above exception, another exception occurred:

    def test_edge_cases():
>       parser, opts, args = parseOpts(['--json-report', '--json-report-file=pytest_report_deepseek-coder-v2_16b.json'])

/opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_options_parseOpts_1.py:12: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/youtube-dl/youtube_dl/options.py:882: in parseOpts
    opts, args = parser.parse_args(overrideArguments)
/opt/conda/envs/test4py_env/lib/python3.10/optparse.py:1389: in parse_args
    self.error(str(err))
/opt/conda/envs/test4py_env/lib/python3.10/optparse.py:1569: in error
    self.exit(2, "%s: error: %s\n" % (self.get_prog_name(), msg))
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <optparse.OptionParser object at 0x7f9cdf809840>, status = 2
msg = '__main__.py: error: no such option: --json-report\n'

    def exit(self, status=0, msg=None):
        if msg:
            sys.stderr.write(msg)
>       sys.exit(status)
E       SystemExit: 2

/opt/conda/envs/test4py_env/lib/python3.10/optparse.py:1559: SystemExit
----------------------------- Captured stderr call -----------------------------
Usage: __main__.py [OPTIONS] URL [URL...]

__main__.py: error: no such option: --json-report
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_options_parseOpts_1.py::test_valid_inputs
FAILED ../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_options_parseOpts_1.py::test_edge_cases
============================== 2 failed in 0.70s ===============================
"""