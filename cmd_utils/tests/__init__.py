from nose.tools import raises
import cmd_utils


def test_run_cmd():
    '''
    Test run_cmd()
    '''
    EXPECTED = "true\n"
    CMD = 'echo true'
    output = cmd_utils.run_cmd(CMD)
    print output
    assert EXPECTED == output


def test_run_cmd_wd():
    '''
    Test run_cmd() working directory handling
    '''
    EXPECTED = "/\n"
    CMD = 'pwd'
    DIR = '/'
    output = cmd_utils.run_cmd(CMD, DIR)
    print output
    assert EXPECTED == output


@raises(cmd_utils.CommandException)
def test_run_cmd_rc():
    '''
    Test run_cmd() return code handling
    '''
    CMD = 'false'
    output = cmd_utils.run_cmd(CMD)
    print output


def test_run_cmd_list():
    '''
    Test run_cmd_list()
    '''
    EXPECTED = ["true\n", "true\n"]
    CMDS = ['echo true', 'echo true']
    output = cmd_utils.run_cmd_list(CMDS)
    print output
    assert EXPECTED == output


def test_run_ssh_cmd():
    '''
    Test run_ssh_cmd()
    '''
    EXPECTED = 'true\n'
    HOST = '127.0.0.1'
    CMD = 'echo true'
    output = cmd_utils.run_ssh_cmd(HOST, CMD)
    print output
    assert EXPECTED == output


def test_run_ssh_cmd_wd():
    '''
    Test run_ssh_cmd() working directory handling
    '''
    EXPECTED = "/\n"
    HOST = '127.0.0.1'
    CMD = 'pwd'
    DIR = '/'
    output = cmd_utils.run_ssh_cmd(HOST, CMD, DIR)
    print output
    assert EXPECTED == output


@raises(cmd_utils.CommandException)
def test_run_ssh_cmd_rc():
    '''
    Test run_ssh_cmd() return code handling
    '''
    HOST = '127.0.0.1'
    CMD = 'false'
    output = cmd_utils.run_ssh_cmd(HOST, CMD)
    print output


def test_run_ssh_cmd_list():
    '''
    Test run_ssh_cmd_list()
    '''
    EXPECTED = ["true\n", "true\n"]
    HOST = '127.0.0.1'
    CMD = ['echo true', 'echo true']
    output = cmd_utils.run_ssh_cmd_list(HOST, CMD)
    print output
    assert EXPECTED == output


# Streaming Tests


def test_streaming_run_cmd():
    '''
    Test streaming.run_cmd()
    '''
    EXPECTED = ["true\n"]
    CMD = 'echo true'
    output = [line for line in cmd_utils.streaming.run_cmd(CMD)]
    print output
    assert EXPECTED == output


def test_streaming_run_cmd_wd():
    '''
    Test run_cmd() working directory handling
    '''
    EXPECTED = ["/\n"]
    CMD = 'pwd'
    DIR = '/'
    output = [line for line in cmd_utils.streaming.run_cmd(CMD, DIR)]
    print output
    assert EXPECTED == output


@raises(cmd_utils.CommandException)
def test_streaming_run_cmd_rc():
    '''
    Test run_cmd() return code handling
    '''
    CMD = 'false'
    output = [line for line in cmd_utils.streaming.run_cmd(CMD)]
    print output


def test_streaming_run_cmd_list():
    '''
    Test run_cmd_list()
    '''
    EXPECTED = ["true\n", "true\n"]
    CMDS = ['echo true', 'echo true']
    output = [line for line in cmd_utils.streaming.run_cmd_list(CMDS)]
    print output
    assert EXPECTED == output


def test_streaming_run_ssh_cmd():
    '''
    Test run_ssh_cmd()
    '''
    EXPECTED = ['true\n']
    HOST = '127.0.0.1'
    CMD = 'echo true'
    output = [line for line in cmd_utils.streaming.run_ssh_cmd(HOST, CMD)]
    print output
    assert EXPECTED == output


def test_streaming_run_ssh_cmd_wd():
    '''
    Test run_ssh_cmd() working directory handling
    '''
    EXPECTED = ["/\n"]
    HOST = '127.0.0.1'
    CMD = 'pwd'
    DIR = '/'
    output = [line for line in cmd_utils.streaming.run_ssh_cmd(HOST, CMD, DIR)]
    print output
    assert EXPECTED == output


@raises(cmd_utils.CommandException)
def test_streaming_run_ssh_cmd_rc():
    '''
    Test run_ssh_cmd() return code handling
    '''
    HOST = '127.0.0.1'
    CMD = 'false'
    output = [line for line in cmd_utils.streaming.run_ssh_cmd(HOST, CMD)]
    print output


def test_streaming_run_ssh_cmd_list():
    '''
    Test run_ssh_cmd_list()
    '''
    EXPECTED = ["true\n", "true\n"]
    HOST = '127.0.0.1'
    CMD = ['echo true', 'echo true']
    output = [line for line in cmd_utils.streaming.run_ssh_cmd_list(HOST, CMD)]
    print output
    assert EXPECTED == output
