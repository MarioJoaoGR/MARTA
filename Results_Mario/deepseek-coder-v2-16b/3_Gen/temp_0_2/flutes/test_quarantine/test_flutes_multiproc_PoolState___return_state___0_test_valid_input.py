
import pytest
from flutes.multiproc import PoolState
import multiprocessing
import collections

@pytest.fixture
def pool_state():
    class WordCounter(PoolState):
        def __init__(self):
            self.word_cnt = collections.Counter()
        
        @PoolState.exception_wrapper()  # prevent the worker from crashing, thus losing data
        def count_words(self, sentence):
            self.word_cnt.update(sentence.split())
    
    return WordCounter()

def test_valid_input(pool_state):
    pool = multiprocessing.Pool(processes=4)
    sentences = ["This is a test.", "Another test here."]
    
    # Map the tasks as usual.
    for _ in pool.imap_unordered(WordCounter.count_words, sentences, chunksize=1000):
        pass
    
    word_counter = collections.Counter()
    # Gather the states and perform the reduce step.
    states = pool.get_states()
    for state in states:
        word_counter.update(state.word_cnt)
    
    assert word_counter == {'This': 1, 'is': 1, 'a': 1, 'test.': 1, 'Another': 1, 'here.': 1}

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc_PoolState___return_state___0_test_valid_input
flutes/Test4DT_tests/test_flutes_multiproc_PoolState___return_state___0_test_valid_input.py:13:9: E1101: Class 'PoolState' has no 'exception_wrapper' member (no-member)
flutes/Test4DT_tests/test_flutes_multiproc_PoolState___return_state___0_test_valid_input.py:24:33: E0602: Undefined variable 'WordCounter' (undefined-variable)
flutes/Test4DT_tests/test_flutes_multiproc_PoolState___return_state___0_test_valid_input.py:29:13: E1101: Instance of 'Pool' has no 'get_states' member (no-member)


"""