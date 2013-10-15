cmd_utils
=========

Simple wrapper for subprocess and paramiko to enable simpler command execution both locally and remotely.


## Install ##
```
pip install cmd_utils
```
or
```
python setup.py install
```

On Debian/Ubuntu `python-setuptools` and `python-dev` are required.

## Tests ##
Test are done with nosetests and require installation of nose
```
pip install nose

python setup.py test
```

## Examples ##
### Local ###
```python
import cmd_utils

working_dir = "/home/mark/a-git-repo"
command = "git diff-index --quiet HEAD --"

output = cmd_utils.run_cmd(command, target_dir)
```
### Remote ###
```python
import cmd_utils

host = "host.example.com"
working_dir = "/home/mark/a-git-repo"
command = "git diff-index --quiet HEAD --"

output = cmd_utils.run_cmd(host, command, working_dir)
```

## Streaming Examples ##
### Local ###
```python
import cmd_utils

working_dir = "/home/mark/a-git-repo"
command = "git diff-index --quiet HEAD --"

for line in cmd_utils.streaming.run_cmd(command, target_dir):
    print line,
```
### Remote ###
```python
import cmd_utils

host = "host.example.com"
working_dir = "/home/mark/a-git-repo"
command = "git diff-index --quiet HEAD --"

for line in cmd_utils.streaming.run_cmd(host, command, working_dir):
    print line,
```
See `examples.py` for more usage examples.

Versions
--------
* 0.4.0
  - Added streaming commands using generators
  - Removed output of return code and added attribute to CommandException
  - Removed error_on_return parameter, exceptions should be handled instead
  - Tided SSH Command Code
  - Move CommandException into a seperate file
* 0.3.0
  - Moved running of command lists into separate functions (backwards incomp)
  - Made specifying a working directory optional
  - Tidied tests
* 0.2.0
  - Encrypted Keyfile handling fixed
  - Username handling improved (backwards incompatible)
* 0.1 - Initial Release
