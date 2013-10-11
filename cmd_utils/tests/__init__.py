from nose.tools import raises
import cmd_utils


def test_run_cmd():
    '''
    Test run_cmd()
    '''
    EXPECTED = ("true\n", 0)
    CMD = 'echo true'
    DIR = '.'

    output = cmd_utils.run_cmd(CMD, DIR, error_on_return=False)
    print output

    assert EXPECTED == output


def test_run_cmd_wd():
    '''
    Test run_cmd() working directory handling
    '''
    EXPECTED = ("/\n", 0)
    CMD = 'pwd'
    DIR = '/'

    output = cmd_utils.run_cmd(CMD, DIR, error_on_return=False)
    print output

    assert EXPECTED == output


@raises(cmd_utils.CommandException)
def test_run_cmd_rc():
    '''
    Test run_cmd() return code handling
    '''
    CMD = 'false'
    DIR = '.'

    cmd_utils.run_cmd(CMD, DIR)


def test_run_cmd_list():
    '''
    Test run_cmd_list()
    '''
    EXPECTED = [("true\n", 0), ("true\n", 0)]
    CMDS = ['echo true', 'echo true']
    DIR = '.'

    output = cmd_utils.run_cmd_list(CMDS, DIR, error_on_return=False)
    print output

    assert EXPECTED == output


def test_run_ssh_cmd():
    '''
    Test run_ssh_cmd()
    '''
    EXPECTED = ('true\n', 0)
    HOST = '127.0.0.1'
    CMD = 'echo true'
    DIR = '.'

    output = cmd_utils.run_ssh_cmd(HOST, CMD, DIR, error_on_return=False)
    print output

    assert EXPECTED == output


def test_run_ssh_cmd_wd():
    '''
    Test run_ssh_cmd() working directory handling
    '''
    EXPECTED = ("/\n", 0)
    HOST = '127.0.0.1'
    CMD = 'pwd'
    DIR = '/'

    output = cmd_utils.run_ssh_cmd(HOST, CMD, DIR, error_on_return=False)
    print output

    assert EXPECTED == output


@raises(cmd_utils.CommandException)
def test_run_ssh_cmd_rc():
    '''
    Test run_ssh_cmd() return code handling
    '''
    HOST = '127.0.0.1'
    CMD = 'false'
    DIR = '.'

    cmd_utils.run_ssh_cmd(HOST, CMD, DIR)


def test_run_ssh_cmd_list():
    '''
    Test run_ssh_cmd_list()
    '''
    EXPECTED = [("true\n", 0), ("true\n", 0)]
    HOST = '127.0.0.1'
    CMD = ['echo true', 'echo true']
    DIR = '.'

    output = cmd_utils.run_ssh_cmd_list(HOST, CMD, DIR, error_on_return=False)
    print output

    assert EXPECTED == output
