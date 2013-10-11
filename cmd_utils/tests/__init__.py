from nose.tools import raises
import cmd_utils


def test_run_cmd():
    '''
    Test run_cmd()
    '''
    EXPECTED = "true\n"
    EXPECTED_RC = 0

    CMD = 'echo true'
    DIR = '.'

    output = cmd_utils.run_cmd(CMD, DIR, error_on_return=False)
    print output

    assert EXPECTED == output[0]
    assert EXPECTED_RC == output[1]


def test_run_cmd_wd():
    '''
    Test run_cmd() working directory handling
    '''
    EXPECTED = "/\n"
    EXPECTED_RC = 0

    CMD = 'pwd'
    DIR = '/'

    output = cmd_utils.run_cmd(CMD, DIR, error_on_return=False)
    print output

    assert EXPECTED == output[0]
    assert EXPECTED_RC == output[1]


def test_run_cmd_rc():
    '''
    Test run_cmd() return code handling
    '''

    CMD = 'false'
    DIR = '.'

    try:
        # False command returns 1
        cmd_utils.run_cmd(CMD, DIR)
    except cmd_utils.CommandException:
        # Expected
        return True
    except:
        return False

    return False


def test_run_ssh_cmd():
    '''
    Test run_ssh_cmd()
    '''
    EXPECTED = 'true\n'
    EXPECTED_RC = 0

    HOST = '127.0.0.1'
    CMD = 'echo true'
    DIR = '.'

    output = cmd_utils.run_ssh_cmd(HOST, CMD, DIR, error_on_return=False)
    print output

    assert EXPECTED == output[0]
    assert EXPECTED_RC == output[1]


def test_run_ssh_cmd_wd():
    '''
    Test run_ssh_cmd() working directory handling
    '''
    EXPECTED = "/\n"
    EXPECTED_RC = 0

    HOST = '127.0.0.1'
    CMD = 'pwd'
    DIR = '/'

    output = cmd_utils.run_ssh_cmd(HOST, CMD, DIR, error_on_return=False)
    print output

    assert EXPECTED == output[0]
    assert EXPECTED_RC == output[1]


@raises(cmd_utils.CommandException)
def test_run_ssh_cmd_rc():
    '''
    Test run_ssh_cmd() return code handling
    '''
    HOST = '127.0.0.1'
    CMD = 'false'
    DIR = '.'

    cmd_utils.run_ssh_cmd(HOST, CMD, DIR)
