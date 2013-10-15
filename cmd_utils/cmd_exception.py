class CommandException(Exception):
    '''
    CommandException
    Raised when a command returns a non-zero exit code

    Attributes:
        exc         - string message
        return_code - return code of command
    '''
    def __init__(self, exc, return_code):
        Exception.__init__(self)
        self.exc = exc
        self.return_code = return_code

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return self.exc
