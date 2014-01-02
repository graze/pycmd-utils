"""Exceptions for cmd_utils."""


class CommandException(Exception):

    """
    Base Exception for cmd_utils exceptions.

    Attributes:
        exc         - string message
        return_code - return code of command

    """

    def __init__(self, exc, return_code=None):
        Exception.__init__(self)
        self.exc = exc
        self.return_code = return_code

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return self.exc


class ReturnCodeError(CommandException):

    """Raised when a command returns a non-zero exit code."""

    pass


class SSHError(CommandException):

    """Raised when SSH connection fails."""

    pass
