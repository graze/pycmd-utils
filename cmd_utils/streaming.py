"""
Streaming Shell / SSH Commands.

Return Generator Objects enabling streaming output

"""
import os
import subprocess


from cmd_exception import ReturnCodeError
import ssh_conn


def run_cmd(command, work_dir=None):
    """
    Run shell command with streaming output.

    Input:
        command  - string of command to run
        work_dir - working directory
    Returns(per iteration):
        output_str
    Raises:
        CommandException
            ReturnCodeError

    """
    if work_dir is not None:
        os.chdir(work_dir)  # Change to working directory

    # Run Command
    ps = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)

    # Read + yield stdout until process ends
    while ps.poll() is None:
        line = ps.stdout.readline()
        if line != "":
            yield line

    return_code = ps.returncode
    # Throw exception if return code is not 0
    if return_code:
        exc = "\nCOMMAND:%s\nRET_CODE:%i" % (command, return_code)
        raise ReturnCodeError(exc, return_code)


def run_cmd_list(commands, work_dir=None):
    """
    Run a list of shell commands with streaming output.

    Input:
        commands - list of commands to run
        work_dir - working directory
    Returns (per iteration):
        output_str
    Raises:
        TypeError
        CommandException
            ReturnCodeError

    """
    if not isinstance(commands, list):
        raise TypeError("commands must be a list")
    for command in commands:
        for line in run_cmd(command, work_dir):
            yield line


def run_ssh_cmd(host, command, work_dir=None, username=None,
                key_filename=None, _connection=None):
    """
    Run shell command over ssh with streaming output.

    Input:
        host         - target machine
        command      - string of command to run
        work_dir     - working directory
        username     - target machine user (if not specified current user)
        key_filename - filepath for private key
        _connection  - SSH Connection
    Returns(per iteration):
        output_str
    Raises:
        CommandException
            SSHError
            ReturnCodeError

    """
    # If no connection passed in create our own
    if _connection is None:
        ssh = ssh_conn.connect(host, username, key_filename)
    else:
        ssh = _connection

    # Handle Working Directory
    if work_dir is not None:
        command = "cd %s && %s" % (work_dir, command)

    # Run Command
    stdin, stdout, stderr = ssh.exec_command(command)

    while True:
        out = stdout.readline()
        # Stderr can block waiting so check to see if its ready
        if stderr.channel.recv_stderr_ready():
            out = out + stderr.readline()
        # If
        if out != "":
            yield out
        else:
            break

    return_code = stdout.channel.recv_exit_status()
    # Throw exception if return code is not 0
    if return_code:
        ssh.close()  # Tidy Up
        exc = "COMMAND:%s\nRET_CODE:%i" % (command, return_code)
        raise ReturnCodeError(exc, return_code)

    if _connection is None:
        ssh.close()


def run_ssh_cmd_list(host, commands, work_dir=None, username=None,
                     key_filename=None):
    """
    Run a list of shell commands over ssh with streaming output.

    Input:
        host         - target machine
        commands     - list of commands to run
        work_dir     - working directory
        username     - target machine user (if not specified current user)
        key_filename - filepath for private key
    Returns (per iteration):
        output_str
    Raises:
        TypeError
        CommandException
            SSHError
            ReturnCodeError

    """
    if not isinstance(commands, list):
        raise TypeError("commands must be a list")

    ssh = ssh_conn.connect(host, username, key_filename)

    for command in commands:
        for line in run_ssh_cmd(host, command, work_dir, username,
                                key_filename, ssh):
            yield line

    ssh.close()
