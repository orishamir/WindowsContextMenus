from enum import StrEnum


class CommandPlaceholder(StrEnum):
    r"""Enum representing Windows shell command placeholders used in registry context menus.

    References:
        [^1]: <https://gist.github.com/Prince-Mandor/c1db742bd2951989db84acfbc7b9562f#gistcomment-1921453>
        [^2]: <https://superuser.com/a/473602>

    Warning:
        If you select multiple files/folders on right-click, each will be called separately.
        This effectively makes placeholders such as %2, %3, %~, etc. useless, and %* equivalent to %1.[^1] [^2]

        [^1]: <https://stackoverflow.com/a/1822850>
        [^2]: <https://superuser.com/a/473602>

    Question:
        The difference between Directory and Folder is that Folders include special folders.
        In the tables below, Folder refers to virtual folders only.
        See [Directory vs. Folder](https://superuser.com/q/169457/)
    """

    FIRST_SELECTED = "%1"
    r"""The first selected item.

    Value depends on the item type being clicked:

    |   Item Type             |     Placeholder Value                           |    Example                                                         |
    | :---------------------- | :---------------------------------------------- | :----------------------------------------------------------------- |
    |   File                  |   The file's path (resolved if its a shortcut)  |   "C:\Windows\System32\cmd.exe"                                    |
    |   Directory             |   The directory's path                          |   "C:\Windows\System32\"                                           |
    |   Folder                |   "::{CLSID}" of the special shell folder[^1]   |   "::{20D04FE0-3AEA-1069-A2D8-08002B30309D}" - "This PC" folder    |
    |   Drive                 |   Drive letter + ":\"                           |   "C:\"                                                            |
    |   Shortcut (Link File)  |   The path of the shortcut (.lnk)               |   "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Word.lnk"  |
    |   Directory Background  |   Error
    |   Desktop Background    |   Error

    [^1]:
        CLSIDs identify special folders. See <https://www.autohotkey.com/docs/v1/misc/CLSID-List.htm>
    """

    CURRENT_DIRECTORY = "%v"
    r"""The first selected item, or the working directory if nothing selected.

    Value depends on the item type being clicked:

    |   Item Type             |     Placeholder Value                           |    Example                                                         |
    | :---------------------- | :---------------------------------------------- | :----------------------------------------------------------------- |
    |   File                  |   The file's path (resolved if its a shortcut)  |   "C:\Windows\System32\cmd.exe"                                    |
    |   Directory             |   The directory's path                          |   "C:\Windows\System32\"                                           |
    |   Folder                |   "::{CLSID}" of the special shell folder[^1]   |   "::{20D04FE0-3AEA-1069-A2D8-08002B30309D}" - "This PC" folder    |
    |   Drive                 |   Drive letter + ":\"                           |   "C:\"                                                            |
    |   Shortcut (Link File)  |   The path of the shortcut (.lnk)               |   "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Word.lnk"  |
    |   Directory Background  |  The directory path                             |   "C:\Windows\System32\"                                           |
    |   Desktop Background    |  The desktop path                               |   "C:\Users\user\Desktop"                                          |

    [^1]:
        CLSIDs identify special folders. See <https://www.autohotkey.com/docs/v1/misc/CLSID-List.htm>
    """

    WORKING_DIRECTORY = "%w"
    r"""The containing working directory.

    Value depends on the item type being clicked:

    |   Item Type             |  Placeholder Value            |    Example                                                 |
    | :---------------------- | :---------------------------- | :--------------------------------------------------------- |
    |   File                  |  The file's parent path       |   "C:\Windows\System32\cmd.exe"                            |
    |   Directory             |  The directory's parent path  |   "C:\Windows\System32\"                                   |
    |   Folder                |  Error
    |   Drive                 |  Error
    |   Shortcut (Link File)  |  The shortcut's parent path   |   "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\"  |
    |   Directory Background  |  The directory path           |   "C:\Windows\System32\"                                   |
    |   Desktop Background    |  The desktop path             |   "C:\Users\user\Desktop"                                  |
    """

    LONG_FILE_NAME = "%l"
    """Long file name form of the first parameter.

    I have no idea what this is.
    """

    HOTKEY = "%h"
    """Hotkey value.

    I have no idea what this is.
    """

    IDLIST_HANDLE = "%i"
    """IDList stored in a shared memory handle.

    I have no idea what this is.
    """

    DESKTOP_PARSING_NAME = "%d"
    r"""Desktop absolute parsing name (for non-filesystem items).

    **Unknown the difference between this and %1.**

    Value depends on the item type being clicked:

    |   Item Type             |   Placeholder Value                               |    Example                                                         |
    | :---------------------- | :------------------------------------------------ | :----------------------------------------------------------------- |
    |   File                  |   The file's path (unresolved if its a shortcut)  |   "C:\Windows\System32\cmd.exe"                                    |
    |   Directory             |   The directory's path                            |   "C:\Windows\System32\"                                           |
    |   Folder                |   "::{CLSID}" of the special shell folder[^1]     |   "::{20D04FE0-3AEA-1069-A2D8-08002B30309D}" - "This PC" folder    |
    |   Drive                 |   Drive letter + ":\"                             |   "C:\"                                                            |
    |   Shortcut (Link File)  |   The path of the shortcut (.lnk)                 |   "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Word.lnk"  |
    |   Directory Background  |   Error (crashes explorer.exe)
    |   Desktop Background    |   Error (crashes explorer.exe)

    [^1]:
        CLSIDs identify special folders. See <https://www.autohotkey.com/docs/v1/misc/CLSID-List.htm>
    """
