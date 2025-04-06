from enum import StrEnum


class WindowsIcon(StrEnum):
    r"""A very limited list of possible values for icons.

    This is only a very partial list.
    For exploring more options, download [IconExtract](https://www.nirsoft.net/utils/iconsext.html) (Bottom of the page),
    open the wanted dll/exe, for example C:\Windows\System32\imageres.dll.
    You'll see a list of icons, with a number in parentheses.
    To use that icon, path_to_icon="imageres.dll,-{icon_number}".
    Note the negative sign before the icon number.

    Tip:
        The DLL "imageres.dll" is highly recommended.

    Notice:
        Sometimes a negative icon number won't work, instead you'll need to use icon_number-1 (the actual index).

    Notice:
        It is possible that a newer, more modern icon exists for the icon you're looking for.
        For example "shell32.dll,-322" is the newer "ieframe.dll,19".

    [^1]: <https://www.urtech.ca/2022/07/solved-download-list-of-icons-in-shell32-dll/amp>
    [^2]: <https://www.digitalcitizen.life/where-find-most-windows-10s-native-icons>
    [^3]: <https://diymediahome.org/windows-icons-reference-list-with-details-locations-images> - Older icons
    """

    THIS_PC = "shell32.dll,-16"
    DOCUMENTS_FOLDER = "shell32.dll,-235"
    PICTURES_FOLDER = "shell32.dll,-236"
    MUSIC_FOLDER = "shell32.dll,-237"
    VIDEOS_FOLDER = "shell32.dll,-238"
    HOME = "shell32.dll,-51380"
    DOWNLOADS_FOLDER = "imageres.dll,-184"
    DESKTOP_FOLDER = "imageres.dll,-183"

    UNDO = "imageres.dll,-5315"
    REDO = "imageres.dll,-5311"
    USER_ACCOUNT_CONTROL_UAC = "imageres.dll,-78"
    """Also see has_lua_shield."""

    CLOUD = "imageres.dll,-1404"

    YELLOW_PADLOCK = "shell32.dll,-48"
    CONTROL_PANEL = "shell32.dll,-22"
    EMPTY_TRASH_BIN = "shell32.dll,-32"
    FULL_TRASH_BIN = "shell32.dll,-33"
    BLUE_PLAY_BUTTON = "shell32.dll,-246"

    RED_FORBIDDEN = "shell32.dll,-200"
    RED_X = "shell32.dll,-220"
    RED_CHECKMARK = "shell32.dll,-253"
    GREEN_CHECKMARK = "shell32.dll,-16802"
    GREEN_CHECKMARK_BOXED = "imageres.dll,-1400"
    REFRESH = "imageres.dll,-1401"

    CMD = "cmd.exe"
