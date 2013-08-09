"""
cmd_utils - Command Utilities

Wrappers for subprocess.Popen and paramiko to enable easy running of commands
locally and on remotely with error handling.

Note tests require an ssh server running locally, and authentication to be
setup.
"""
from .cmd_utils import run_cmd, run_ssh_cmd, CommandException
