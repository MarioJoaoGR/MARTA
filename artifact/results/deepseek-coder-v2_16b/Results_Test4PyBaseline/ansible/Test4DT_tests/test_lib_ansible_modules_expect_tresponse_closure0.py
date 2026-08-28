# Module: ansible.modules.expect
import ansible.module_utils.basic as basic
import pytest

# Module: ansible.modules.expect
def response_closure(module, question, responses):
    resp_gen = (b'%s\n' % to_bytes(r).rstrip(b'\n') for r in responses)

    def wrapped(info):
        try:
            return next(resp_gen)
        except StopIteration:
            module.fail_json(msg="No remaining responses for '%s', "
                                 "output was '%s'" %
                                 (question,
                                  info['child_result_list'][-1]))

    return wrapped

# Test cases for response_closure function
@pytest.fixture
def module():
    return basic.AnsibleModule(argument_spec={})

@pytest.fixture
def responses():
    return ["Response 1", "Response 2", "Response 3"]

@pytest.fixture
def question():
    return "What is your favorite color?"

# Test case for basic usage
def test_response_closure_basic(module, responses, question):
    wrapped_function = response_closure(module, question, responses)
    info = {'child_result_list': ['blue', 'green']}
    assert wrapped_function(info) == b"Response 1\n"

# Test case for handling no responses left
def test_response_closure_no_responses(module, responses, question):
    wrapped_function = response_closure(module, question, responses[:1])
    info = {'child_result_list': []}
    with pytest.raises(basic.AnsibleModule.fail_json):
        wrapped_function(info)

# Test case for using with different info structure
def test_response_closure_different_info_structure(module, responses, question):
    wrapped_function = response_closure(module, question, responses)
    info = {'child_result': ['chocolate', 'vanilla']}
    assert wrapped_function(info) == b"Response 1\n"
