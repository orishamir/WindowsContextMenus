from enum import StrEnum


class MenuAccessScope(StrEnum):
    """The access scope of the context menu.

    Either all users or current user only.
    The enum's value indicates the base registry location of that scope.
    """

    ALL_USERS = r"HKEY_LOCAL_MACHINE\Software\Classes"
    CURRENT_USER = r"HKEY_CURRENT_USER\Software\Classes"
    # HKEY_CLASS_ROOT - https://stackoverflow.com/a/55118854 should not be written to.
