'''
Examples of cmd_utils
'''
import os
import pwd
import cmd_utils

USER = pwd.getpwuid(os.getuid()).pw_name  # Get current username

print "Local - List current dir"
output = cmd_utils.run_cmd("ls -l", ".")
print "Output:\n%s" % output[0]  # Output
print "Return Code: %i" % output[1]  # Return Code

print "Local - Ignore a non-zero return"
output = cmd_utils.run_cmd("false", ".", error_on_return=False)
print "Output:\n%s" % output[0]  # Output
print "Return Code: %i" % output[1]  # Return Code

print "Local - List a different dir"
output = cmd_utils.run_cmd("ls -l", "/")
print "Output:\n%s" % output[0]  # Output
print "Return Code: %i" % output[1]  # Return Code

print "Local - Multiple Commands"
commands = ["pwd", "ls -l", "pwd"]
output = cmd_utils.run_cmd(commands, ".")
print "0 Output:\n%s" % output[0][0]        # Command 0 Output
print "0 Return Code: %i" % output[0][1]    # Command 0 Return Code
print "1 Output:\n%s" % output[1][0]        # Command 1 Output
print "1 Return Code: %i" % output[1][1]    # Command 1 Return Code
print "2 Output:\n%s" % output[2][0]        # Command 2 Output
print "2 Return Code: %i" % output[2][1]    # Command 2 Return Code

# Note the following remote commands expect you to be able to login
# to localhost via ssh

print "Remote - List root dir"
output = cmd_utils.run_ssh_cmd("127.0.0.1", USER, "ls -l", "/")
print "Output:\n%s" % output[0]  # Output
print "Return Code: %i" % output[1]  # Return Code

print "Remote - Ignore non-zero return"
output = cmd_utils.run_ssh_cmd("127.0.0.1", USER, "false", "/",
                               error_on_return=False)
print "Output:\n%s" % output[0]  # Output
print "Return Code: %i" % output[1]  # Return Code

print "Remote - Multiple Commands"
commands = ["pwd", "ls -l", "pwd"]
output = cmd_utils.run_ssh_cmd("127.0.0.1", USER, commands, "/")
print "0 Output:\n%s" % output[0][0]        # Command 0 Output
print "0 Return Code: %i" % output[0][1]    # Command 0 Return Code
print "1 Output:\n%s" % output[1][0]        # Command 1 Output
print "1 Return Code: %i" % output[1][1]    # Command 1 Return Code
print "2 Output:\n%s" % output[2][0]        # Command 2 Output
print "2 Return Code: %i" % output[2][1]    # Command 2 Return Code
