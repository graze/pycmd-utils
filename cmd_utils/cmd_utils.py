import os
import subprocess
import paramiko


def run_cmd(command, work_dir=None, error_on_return=True):
    '''
    Run shell command
    Input:
        commands - string of command to run
        work_dir - working directory
        error_on_return - raise CommandException on non-zero return code
    Returns:
        (output_str, return_code)
    '''
    if work_dir is not None:
        os.chdir(work_dir)  # Change to working directory

    # Run Command
    ps = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output = ps.communicate()[0]
    return_code = ps.returncode
    # Throw exception if error_on_return is true and return code is not 0
    if error_on_return and return_code:
        exc = "%s\nCOMMAND:%s\nRET_CODE:%i" % (output, command, return_code)
        raise CommandException(exc)

    out = (output, return_code)
    return out


def run_cmd_list(commands, work_dir=None, error_on_return=True):
    '''
    Run a list of shell commands
    Input:
        commands - list of commands to run
        work_dir - working directory
        error_on_return - raise CommandException on non-zero return code
    Returns:
        [(output, return_code), ]
    '''
    if not isinstance(commands, list):
        raise TypeError("Commands must be a list")
    out_list = []
    for command in commands:
        out_list.append(run_cmd(command, work_dir, error_on_return))
    return out_list


def run_ssh_cmd(host, command, work_dir=None, username=None,
                key_filename=None, error_on_return=True):
    '''
    Run shell command over ssh
    Input:
        host - target machine
        command - string of command to run
        work_dir - working directory
        username - target machine user (if not specified current user)
        key_filename - filepath for private key
        error_on_return - raise CommandException on non-zero return
    Returns:
        (output_str, return_code)

    '''
    ssh = paramiko.SSHClient()
    # Auto add missing hostkeys
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # Handle private key and connect
    if key_filename is not None:
        ssh.connect(host, username=username, key_filename=key_filename)
    else:
        # Setting look_for_keys=False here so we only use ssh-agent
        # if we find the file and it's encrypted things break
        ssh.connect(host, username=username, look_for_keys=False)

    # Handle Working Directory
    if work_dir is not None:
        command = "cd %s && %s" % (work_dir, command)

    # Run Command
    stdin, stdout, stderr = ssh.exec_command(command)
    return_code = stdout.channel.recv_exit_status()

    # Combine stdout / stderr
    output = stdout.readlines() + stderr.readlines()
    output = "".join(output)  # Join lines into one string

    # Throw exception if error_on_return is true and return code is not 0
    if error_on_return and return_code:
        ssh.close()  # Tidy Up
        exc = "%s\nCOMMAND:%s\nRET_CODE:%i" % (output, command, return_code)
        raise CommandException(exc)
    out = (output, return_code)

    ssh.close()
    return out


def run_ssh_cmd_list(host, commands, work_dir=None, username=None,
                     key_filename=None, error_on_return=True):
    '''
    Run shell commands over ssh
    Input:
        host - target machine
        commands - list of commands to run
        work_dir - working directory
        username - target machine user (if not specified current user)
        key_filename - filepath for private key
        error_on_return - raise CommandException on non-zero return
    Returns:
        (output_str, return_code)

    '''
    if not isinstance(commands, list):
        raise TypeError("Commands must be a list")

    ssh = paramiko.SSHClient()
    # Auto add missing hostkeys
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # Handle private key and connect
    if key_filename is not None:
        ssh.connect(host, username=username, key_filename=key_filename)
    else:
        # Setting look_for_keys=False here so we only use ssh-agent
        # if we find the file and it's encrypted things break
        ssh.connect(host, username=username, look_for_keys=False)
    out_list = []
    for command in commands:
        # Handle Working Directory
        if work_dir is not None:
            command = "cd %s && %s" % (work_dir, command)

        # Run Command
        stdin, stdout, stderr = ssh.exec_command(command)
        return_code = stdout.channel.recv_exit_status()

        # Combine stdout / stderr
        output = stdout.readlines() + stderr.readlines()
        output = "".join(output)  # Join lines into one string

        # Throw exception if error_on_return is true and return code is not 0
        if error_on_return and return_code:
            ssh.close()  # Tidy Up
            exc = "%s\nCOMMAND:%s\nRET_CODE:%i" % (output, command,
                                                   return_code)
            raise CommandException(exc)
        out_list.append((output, return_code))

    ssh.close()
    return out_list


class CommandException(Exception):
    def __init__(self, exc):
        Exception.__init__(self)
        self.exc = exc

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return self.exc
