from enum import EnumMeta


class Location(EnumMeta):
    """
    When should the Context Menu be opened? Files? Directories?
    """

    LEFT_PANEL = r"HKEY_CURRENT_USER\Software\Classes\directory\Background\shell"
    LEFT_PANEL_ADMIN = r"HKEY_CLASSES_ROOT\Directory\Background\shell"
    RIGHT_PANEL = r"HKEY_CURRENT_USER\Software\Classes\directory\shell"
    RIGHT_PANEL_ADMIN = r"HKEY_CLASSES_ROOT\Directory\shell"
    FILE = r"HKEY_CURRENT_USER\Software\Classes\*\shell"
    FILE_ADMIN = r"HKEY_CLASSES_ROOT\*\shell"
    DESKTOP = r"HKEY_CLASSES_ROOT\DesktopBackground\Shell"
