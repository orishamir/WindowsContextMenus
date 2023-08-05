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

CONVERT_AUDIO_COMMAND = 'cmd.exe /c ffmpeg -i "%V" {}'

ConvertToWAV = ContextMenu(
    "ConvertToWAV",
    [
        EntryName("Convert to WAV"),
        Command(CONVERT_AUDIO_COMMAND.format('"%V".wav')),
        Condition(
            ExtensionType != "wav"
        )
    ]
)

ConvertToMP3 = ContextMenu(
    "ConvertToMP3",
    [
        EntryName("Convert to MP3"),
        Command(CONVERT_AUDIO_COMMAND.format('"%V".mp3')),
        Condition(
            ExtensionType != "mp3"
        )
    ]
)

ConvertToOGG = ContextMenu(
    "ConvertToOGG",
    [
        EntryName("Convert to OGG"),
        Command(CONVERT_AUDIO_COMMAND.format('"%V".ogg')),
        Condition(
            ExtensionType != ".ogg"
        )
    ]
)

ConvertToFLAC = ContextMenu(
    "ConvertToFLAC",
    [
        EntryName("Convert to FLAC"),
        Command(CONVERT_AUDIO_COMMAND.format('"%V".flac')),
        Condition(
            ExtensionType != ".flac"
        )
    ]
)

main = ContextMenu(
    "ConvertAudioType",
    [
        EntryName("Convert to..."),
        Icon(r"D:\Pictures\Convert_arrow.ico"),
        Condition(
            (ExtensionType == ".mp3") |
            (ExtensionType == ".wav") |
            (ExtensionType == ".ogg") |
            (ExtensionType == ".flac")

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
    print(apply_context_menu(
        main,
        [
            Location.FILE_ADMIN
        ]
    ))
