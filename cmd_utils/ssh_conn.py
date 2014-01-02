"""
SSH Connection.

Used to establish SSH connections

"""
import socket
import cmd_exception
import paramiko


def connect(host, username=None, key_filename=None):
    """
    Connect to target host.

    Returns:
        SSH connection
    Raises:
        SSHError

    """
    ssh = paramiko.SSHClient()
    # Auto add missing hostkeys
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # Handle private key and connect
        if key_filename is not None:
            ssh.connect(host, username=username, key_filename=key_filename)
        else:
            # Setting look_for_keys=False here so we only use ssh-agent
            # if we find the file and it's encrypted things break
            ssh.connect(host, username=username, look_for_keys=False)
        return ssh
    except socket.error as e:
        # Handle socket errors, normally due to incorrect / unreachable host
        raise cmd_exception.SSHError("SSH Failed: %s" % e.strerror)
    except paramiko.SSHException as e:
        # Handle SSH errors, normally authentication issues
        raise cmd_exception.SSHError("SSH Failed: %s" % e.message)
