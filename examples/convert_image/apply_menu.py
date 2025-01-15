"""
https://learn.microsoft.com/en-us/windows/win32/shell/context-menu-handlers

https://learn.microsoft.com/en-us/previous-versions//ff521735(v=vs.85)
"""
from src.conditions import ExtensionType
from src.context_menu_locations import ContextMenuLocation
from src.registry_interaction import apply_context_menu
from src.context_menu import ContextMenu
from src.features import (
    Command,
    EntryName,
    Icon,
    ConditionFeature,
)

CONVERT_IMAGE_COMMAND = 'cmd.exe /c convert_image.py "%V"'

convert_to_png_entry = ContextMenu(
    "ConvertToPng",
    [
        EntryName("Convert to PNG"),
        Command(f'{CONVERT_IMAGE_COMMAND} png'),
        ConditionFeature(
            ExtensionType != ".png"
        )
    ]
)

convert_to_jpeg_entry = ContextMenu(
    "ConvertToJPEG",
    [
        EntryName("Convert to JPEG"),
        Command(f'{CONVERT_IMAGE_COMMAND} jpeg'),
        ConditionFeature(
            ExtensionType != ".jpeg"
        )
    ]
)

convert_to_ico_entry = ContextMenu(
    "ConvertToIco",
    [
        EntryName("Convert to ICO"),
        Command(f'{CONVERT_IMAGE_COMMAND} ico'),
        ConditionFeature(
            ExtensionType != ".ico"
        )
    ]
)

convert_to_bmp_entry = ContextMenu(
    "ConvertToBmp",
    [
        EntryName("Convert to BMP"),
        Command(f'{CONVERT_IMAGE_COMMAND} bmp'),
        ConditionFeature(
            ExtensionType != ".bmp"
        )
    ]
)
convert_to_webp_entry = ContextMenu(
    "ConvertToWebp",
    [
        EntryName("Convert to WEBP"),
        Command(f'{CONVERT_IMAGE_COMMAND} webp'),
        ConditionFeature(
            ExtensionType != ".webp"
        )
    ]
)
main: ContextMenu = ContextMenu(
    "ConvertImageType",
    [
        EntryName("Convert to..."),
        Icon(r"D:\Pictures\Convert_arrow.ico"),
        ConditionFeature(
            (ExtensionType == ".png") |
            (ExtensionType == ".jpeg") |
            (ExtensionType == ".jpg") |
            (ExtensionType == ".bmp") |
            (ExtensionType == ".ico") |
            (ExtensionType == ".webp")
        )
    ],
    [
        convert_to_png_entry,
        convert_to_ico_entry,
        convert_to_jpeg_entry,
        convert_to_bmp_entry,
        convert_to_webp_entry
    ]

)

if __name__ == '__main__':
    apply_context_menu(
        main,
        ContextMenuLocation.ALL_FILES_ADMIN,
    )
