"""
https://learn.microsoft.com/en-us/windows/win32/shell/context-menu-handlers

https://learn.microsoft.com/en-us/previous-versions//ff521735(v=vs.85)
"""
from src.conditions import ExtensionType
from src.location import Location
from src.registry_interaction import apply_context_menu
from src.context_menu import ContextMenu
from src.features import (
    Command,
    EntryName,
    Icon,
    Condition
)

CONVERT_IMAGE_COMMAND = 'cmd.exe /c convert_image.py "%V"'

convert_to_png_entry = ContextMenu(
    "ConvertToPng",
    [
        EntryName("Convert to PNG"),
        Command(f'{CONVERT_IMAGE_COMMAND} png'),
        Condition(
            ExtensionType != ".png"
        )
    ]
)

convert_to_jpeg_entry = ContextMenu(
    "ConvertToJPEG",
    [
        EntryName("Convert to JPEG"),
        Command(f'{CONVERT_IMAGE_COMMAND} jpeg'),
        Condition(
            ExtensionType != ".jpeg"
        )
    ]
)

convert_to_ico_entry = ContextMenu(
    "ConvertToIco",
    [
        EntryName("Convert to ICO"),
        Command(f'{CONVERT_IMAGE_COMMAND} ico'),
        Condition(
            ExtensionType != ".ico"
        )
    ]
)

convert_to_bmp_entry = ContextMenu(
    "ConvertToBmp",
    [
        EntryName("Convert to BMP"),
        Command(f'{CONVERT_IMAGE_COMMAND} bmp'),
        Condition(
            ExtensionType != ".bmp"
        )
    ]
)

main: ContextMenu = ContextMenu(
    "ConvertImageType",
    [
        EntryName("Convert to..."),
        Icon(r"D:\Pictures\Convert_arrow.ico"),
        Condition(
            (ExtensionType == ".png") |
            (ExtensionType == ".jpeg") |
            (ExtensionType == ".jpg") |
            (ExtensionType == ".bmp") |
            (ExtensionType == ".ico")
        )
    ],
    [
        convert_to_png_entry,
        convert_to_jpeg_entry,
        convert_to_bmp_entry,
        convert_to_ico_entry
    ]

)

if __name__ == '__main__':
    apply_context_menu(
        main,
        [
            Location.FILE_ADMIN
        ]
    )
