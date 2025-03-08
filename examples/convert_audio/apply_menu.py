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
    ConditionFeature
)

CONVERT_AUDIO_COMMAND = 'cmd.exe /c ffmpeg -i "%V" {}'

ConvertToWAV = ContextMenu(
    "ConvertToWAV",
    [
        EntryName("Convert to WAV"),
        Command(CONVERT_AUDIO_COMMAND.format('"%V".wav')),
        ConditionFeature(
            ExtensionType(ComparisonType.NOT_EQUAL, ".wav")
        )
    ],

)

ConvertToMP3 = ContextMenu(
    "ConvertToMP3",
    [
        EntryName("Convert to MP3"),
        Command(CONVERT_AUDIO_COMMAND.format('"%V".mp3')),
        ConditionFeature(
            ExtensionType(ComparisonType.NOT_EQUAL, ".mp3"),
        )
    ]
)

ConvertToOGG = ContextMenu(
    "ConvertToOGG",
    [
        EntryName("Convert to OGG"),
        Command(CONVERT_AUDIO_COMMAND.format('"%V".ogg')),
        ConditionFeature(
            ExtensionType(ComparisonType.NOT_EQUAL, ".ogg"),
        )
    ]
)

ConvertToFLAC = ContextMenu(
    "ConvertToFLAC",
    [
        EntryName("Convert to FLAC"),
        Command(CONVERT_AUDIO_COMMAND.format('"%V".flac')),
        ConditionFeature(
            ExtensionType(ComparisonType.NOT_EQUAL, ".flac"),
        )
    ]
)

main = ContextMenu(
    "ConvertAudioType",
    [
        EntryName("Convert to..."),
        Icon(r"D:\Pictures\Convert_arrow.ico"),
        ConditionFeature(
            ExtensionType(ComparisonType.EQUALS, ".mp3") |
            ExtensionType(ComparisonType.EQUALS, ".wav") |
            ExtensionType(ComparisonType.EQUALS, ".ogg") |
            ExtensionType(ComparisonType.EQUALS, ".flac")
        )
    ],
    [
        ConvertToWAV,
        ConvertToMP3,
        ConvertToOGG,
        ConvertToFLAC
    ]
)

if __name__ == '__main__':
    apply_context_menu(
        main,
        bindings=[
            ContextMenuBinding(MenuAccessScope.ALL_USERS, MenuItemType.ALL_FILES),
        ],
    )
