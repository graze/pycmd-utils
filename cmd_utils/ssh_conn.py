'''
SSH Connection

Used to establish SSH connections
'''
import paramiko


def connect(host, username=None, key_filename=None):
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
    return ssh
