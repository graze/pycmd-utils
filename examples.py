'''
Examples of cmd_utils
'''
import cmd_utils

print "Local - List current dir"
output = cmd_utils.run_cmd("ls -l")
print "Output:\n%s" % output

print "Local - List a different dir"
output = cmd_utils.run_cmd("ls -l", "/")
print "Output:\n%s" % output

print "Local - Catch Exception"
try:
    output = cmd_utils.run_cmd("THISCOMMANDDOESNOTEXIST")
except cmd_utils.ReturnCodeError as e:
    print "Caught Error:",
    print e

print ""

print "Local - Multiple Commands"
commands = ["pwd", "ls -l", "pwd"]
output = cmd_utils.run_cmd_list(commands)
print "0 Output:\n%s" % output[0]
print "1 Output:\n%s" % output[1]
print "2 Output:\n%s" % output[2]

# Note the following remote commands expect you to be able to login
# to localhost via ssh

print "Remote - List root dir"
output = cmd_utils.run_ssh_cmd("127.0.0.1", "ls -l", "/")
print "Output:\n%s" % output

print "Remote - Multiple Commands"
commands = ["pwd", "ls -l", "pwd"]
output = cmd_utils.run_ssh_cmd_list("127.0.0.1", commands, "/")
print "0 Output:\n%s" % output[0]
print "1 Output:\n%s" % output[1]
print "2 Output:\n%s" % output[2]

# Streaming Commands, these return a generator enabling you to get output
# while the command is running, unlike the default functions

# Here we use a generator to get all output
print "Streaming Local - List current dir"
output = [line for line in cmd_utils.streaming.run_cmd("ls -l")]
print "Output:\n%s" % output

# Here we use a for loop to print as it executes
print "Streaming Local - Ping Localhost"
print "Output:"
for line in cmd_utils.streaming.run_cmd("ping -c 5 127.0.0.1"):
    print line,  # Stdout lines already have \n on them

# Here we use a for loop to print as it executes
print "Streaming Local - Multiple Commands"
commands = ["pwd", "ls -l", "pwd"]
print "Output:"
for line in cmd_utils.streaming.run_cmd_list(commands):
    print line,  # Stdout lines already have \n on them

# Note the following remote commands expect you to be able to login
# to localhost via ssh

print "Streaming Remote - List root dir"
print "Output:"
for line in cmd_utils.streaming.run_ssh_cmd("127.0.0.1", "ls -l", "/"):
    print line,  # Stdout lines already have \n on them

print "Streaming Remote - Multiple Commands"
commands = ["pwd", "ls -l", "pwd"]
print "Output:"
for line in cmd_utils.streaming.run_ssh_cmd_list("127.0.0.1", commands, "/"):
    print line,  # Stdout lines already have \n on them
