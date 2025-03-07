"""
https://learn.microsoft.com/en-us/windows/win32/shell/context-menu-handlers

https://learn.microsoft.com/en-us/previous-versions//ff521735(v=vs.85)
"""
from context_menu_toolkit.conditions import ExtensionType
from context_menu_toolkit.conditions.comparison_type import ComparisonType
from context_menu_toolkit.context_menu_bindings import ContextMenuBinding, MenuAccessScope, MenuItemType
from context_menu_toolkit.registry_interaction import apply_context_menu
from context_menu_toolkit.context_menu import ContextMenu
from context_menu_toolkit.features import (
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
            ExtensionType(ComparisonType.NOT_EQUAL, ".png")
        )
    ]
)

convert_to_jpeg_entry = ContextMenu(
    "ConvertToJPEG",
    [
        EntryName("Convert to JPEG"),
        Command(f'{CONVERT_IMAGE_COMMAND} jpeg'),
        ConditionFeature(
            ExtensionType(ComparisonType.NOT_EQUAL, ".jpeg")
        )
    ]
)

convert_to_ico_entry = ContextMenu(
    "ConvertToIco",
    [
        EntryName("Convert to ICO"),
        Command(f'{CONVERT_IMAGE_COMMAND} ico'),
        ConditionFeature(
            ExtensionType(ComparisonType.NOT_EQUAL, ".ico")
        )
    ]
)

convert_to_bmp_entry = ContextMenu(
    "ConvertToBmp",
    [
        EntryName("Convert to BMP"),
        Command(f'{CONVERT_IMAGE_COMMAND} bmp'),
        ConditionFeature(
            ExtensionType(ComparisonType.NOT_EQUAL, ".bmp")
        )
    ]
)
convert_to_webp_entry = ContextMenu(
    "ConvertToWebp",
    [
        EntryName("Convert to WEBP"),
        Command(f'{CONVERT_IMAGE_COMMAND} webp'),
        ConditionFeature(
            ExtensionType(ComparisonType.NOT_EQUAL, ".webp")
        )
    ]
)
main: ContextMenu = ContextMenu(
    "ConvertImageType",
    [
        EntryName("Convert to..."),
        Icon(r"D:\Pictures\Convert_arrow.ico"),
        ConditionFeature(
            ExtensionType(ComparisonType.EQUALS, ".png") |
            ExtensionType(ComparisonType.EQUALS, ".jpeg") |
            ExtensionType(ComparisonType.EQUALS, ".jpg") |
            ExtensionType(ComparisonType.EQUALS, ".bmp") |
            ExtensionType(ComparisonType.EQUALS, ".ico") |
            ExtensionType(ComparisonType.EQUALS, ".webp")
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
        bindings=[
            ContextMenuBinding(MenuAccessScope.ALL_USERS, MenuItemType.ALL_FILES),
        ],
    )
