from src.exceptions.base_exception import ContextMenuPathException


class NotAFileError(ContextMenuPathException):
    pass


class BadIconExtensionError(ContextMenuPathException):
    pass
