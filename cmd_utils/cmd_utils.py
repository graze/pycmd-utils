import os
import subprocess
import paramiko


def run_cmd(commands, work_dir, error_on_return=True):
    '''
    Run shell command(s)
    Input:
        commands - list of commands or string for one command
        work_dir - working directory
        error_on_return - raise CommandException on non-zero return code
    Returns:
        [(output, return_code), (output, return_code)]
        OR
        (output_str, return_code)
    '''
    # Single command to list
    if isinstance(commands, str):
        commands = [commands]

    os.chdir(work_dir)  # Change to working directory
    out_list = []  # Output of commands

    for cmd in commands:
        # Run Command
        ps = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
        output = ps.communicate()[0]
        return_code = ps.returncode
        # Throw exception if error_on_return is true and return code is not 0
        if error_on_return and return_code:
            exc = "%s\nCOMMAND:%s\nRET_CODE:%i" % (output, cmd, return_code)
            raise CommandException(exc)
        out_list.append((output, return_code))

    # Handle single element outlist
    if len(out_list) == 1:
        return out_list[0]
    return out_list


def run_ssh_cmd(host, username, commands, work_dir, key_filename=None,
                error_on_return=True):
    '''
    Run shell command(s) over ssh
    Input:
        host - target machine
        username - target machine user
        commands - list of commands or string for one command
        work_dir - working directory
        key_filename - filepath for private key
        error_on_return - raise CommandException on non-zero return
    Returns:
        [(output, return_code), (output, return_code)]
        OR
        (output_str, return_code)

    '''
    # Single command to list
    if isinstance(commands, str):
        commands = [commands]

    ssh = paramiko.SSHClient()
    # Auto add missing hostkeys
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # Handle private key and connect
    if key_filename is not None:
        ssh.connect(host, username=username, key_filename=key_filename)
    else:
        ssh.connect(host, username=username)

    out_list = []

    for cmd in commands:
        # Handle Working Directory
        # Must be done for every command as working directory resets
        cmd = "cd %s && %s" % (work_dir, cmd)

        # Run Command
        stdin, stdout, stderr = ssh.exec_command(cmd)
        return_code = stdout.channel.recv_exit_status()

        # Combine stdout / stderr
        output = stdout.readlines() + stderr.readlines()
        output = "".join(output)  # Join lines into one string

        # Throw exception if error_on_return is true and return code is not 0
        if error_on_return and return_code:
            ssh.close()  # Tidy Up
            exc = "%s\nCOMMAND:%s\nRET_CODE:%i" % (output, cmd, return_code)
            raise CommandException(exc)
        out_list.append((output, return_code))

    ssh.close()

    # Handle single element outlist
    if len(out_list) == 1:
        return out_list[0]
    return out_list


class CommandException(Exception):
    def __init__(self, exc):
        Exception.__init__(self)
        self.exc = exc

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return self.exc
