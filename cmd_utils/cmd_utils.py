"""
Basic Shell / SSH commands.

Non-streaming output is returned after command completes.

"""
import os
import subprocess

from cmd_exception import ReturnCodeError
import ssh_conn


def run_cmd(command, work_dir=None):
    """
    Run shell command.

    Input:
        command  - string of command to run
        work_dir - working directory
    Returns:
        output_str
    Raises:
        CommandException
            ReturnCodeError

    """
    if work_dir is not None:
        os.chdir(work_dir)  # Change to working directory

    # Run Command
    ps = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output = ps.communicate()[0]
    return_code = ps.returncode
    # Throw exception if return code is not 0
    if return_code:
        exc = "%s\nCOMMAND:%s\nRET_CODE:%i" % (output, command, return_code)
        raise ReturnCodeError(exc, return_code)

    return output


def run_cmd_list(commands, work_dir=None):
    """
    Run a list of shell commands.

    Input:
        commands - list of commands to run
        work_dir - working directory
    Returns:
        [output_str, ]
    Raises:
        TypeError
        CommandException
            ReturnCodeError

    """
    if not isinstance(commands, list):
        raise TypeError("commands must be a list")
    out_list = []
    for command in commands:
        out_list.append(run_cmd(command, work_dir))
    return out_list


def run_ssh_cmd(host, command, work_dir=None, username=None,
                key_filename=None, _connection=None):
    """
    Run shell command over ssh.

    Input:
        host         - target machine
        command      - string of command to run
        work_dir     - working directory
        username     - target machine user (if not specified current user)
        key_filename - filepath for private key
        _connection  - SSH Connection
    Returns:
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
    return_code = stdout.channel.recv_exit_status()

    # Combine stdout / stderr
    output = stdout.readlines() + stderr.readlines()
    output = "".join(output)  # Join lines into one string

    # Throw exception if return code is not 0
    if return_code:
        ssh.close()  # Tidy Up
        exc = "%s\nCOMMAND:%s\nRET_CODE:%i" % (output, command, return_code)
        raise ReturnCodeError(exc, return_code)

    if _connection is None:
        ssh.close()
    return output


def run_ssh_cmd_list(host, commands, work_dir=None, username=None,
                     key_filename=None):
    """
    Run shell commands over ssh.

    Input:
        host         - target machine
        commands     - list of commands to run
        work_dir     - working directory
        username     - target machine user (if not specified current user)
        key_filename - filepath for private key
    Returns:
        [output_str, ]
    Raises:
        TypeError
        CommandException
            SSHError
            ReturnCodeError

    """
    if not isinstance(commands, list):
        raise TypeError("commands must be a list")

    ssh = ssh_conn.connect(host, username, key_filename)

    out_list = []
    for command in commands:
        out_list.append(run_ssh_cmd(host, command, work_dir, username,
                                    key_filename, ssh))
    ssh.close()
    return out_list
