from enum import StrEnum


class ContextMenuLocation(StrEnum):
    """When should the Context Menu be opened? Files? Directories?
    """
    # All Files
    ALL_FILES_ADMIN = r"HKEY_LOCAL_MACHINE\Software\Classes\*\shell"
    ALL_FILES_USER = r"HKEY_CURRENT_USER\Software\Classes\*\shell"

    # Specific File Types
    SPECIFIC_FILE_TYPE_ADMIN = r"HKEY_LOCAL_MACHINE\Software\Classes\{extension}\shell"
    SPECIFIC_FILE_TYPE_USER = r"HKEY_CURRENT_USER\Software\Classes\{extension}\shell"

    # File Type Class
    # FILE_TYPE_CLASS_ADMIN = r"HKEY_LOCAL_MACHINE\Software\Classes\<file-class>\shell"
    # FILE_TYPE_CLASS_USER = r"HKEY_CURRENT_USER\Software\Classes\<file-class>\shell"

    # Folders
    FOLDERS_ADMIN = r"HKEY_LOCAL_MACHINE\Software\Classes\Folder\shell"
    FOLDERS_USER = r"HKEY_CURRENT_USER\Software\Classes\Folder\shell"

    # Directory Background
    DIRECTORY_BACKGROUND_ADMIN = r"HKEY_LOCAL_MACHINE\Software\Classes\Directory\Background\shell"
    DIRECTORY_BACKGROUND_USER = r"HKEY_CURRENT_USER\Software\Classes\Directory\Background\shell"

    # Drives
    DRIVES_ADMIN = r"HKEY_LOCAL_MACHINE\Software\Classes\Drive\shell"
    DRIVES_USER = r"HKEY_CURRENT_USER\Software\Classes\Drive\shell"

    # General Directories
    GENERAL_DIRECTORIES_ADMIN = r"HKEY_LOCAL_MACHINE\Software\Classes\Directory\shell"
    GENERAL_DIRECTORIES_USER = r"HKEY_CURRENT_USER\Software\Classes\Directory\shell"

    # Network Folders
    NETWORK_FOLDERS_ADMIN = r"HKEY_LOCAL_MACHINE\Software\Classes\Network\shell"
    NETWORK_FOLDERS_USER = r"HKEY_CURRENT_USER\Software\Classes\Network\shell"

    # Desktop Background
    DESKTOP_BACKGROUND_ADMIN = r"HKEY_LOCAL_MACHINE\Software\Classes\DesktopBackground\shell"
    DESKTOP_BACKGROUND_USER = r"HKEY_CURRENT_USER\Software\Classes\DesktopBackground\shell"

    # Shortcuts (LNK Files)
    SHORTCUTS_ADMIN = r"HKEY_LOCAL_MACHINE\Software\Classes\lnkfile\shell"
    SHORTCUTS_USER = r"HKEY_CURRENT_USER\Software\Classes\lnkfile\shell"

    # Control Panel Items
    # CONTROL_PANEL_ITEMS_ADMIN = r"HKEY_LOCAL_MACHINE\Software\Classes\CLSID\<GUID>\shell"
    # CONTROL_PANEL_ITEMS_USER = r"HKEY_CURRENT_USER\Software\Classes\CLSID\<GUID>\shell"
