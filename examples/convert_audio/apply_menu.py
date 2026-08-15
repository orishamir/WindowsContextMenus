# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "windows_context_menus",
# ]
#
# [tool.uv.sources]
# windows_context_menus = { path = "../../" }
# ///

from windows_context_menus import CommandPlaceholder, Condition, ContextMenu, ContextMenuBinding, ExplorerItemType, RegistryHandler

CONVERT_AUDIO_COMMAND = f'cmd.exe /c ffmpeg -i "{CommandPlaceholder.FIRST_SELECTED}" {{}}'

ConvertToWAV = ContextMenu(
    display_text="Convert to WAV",
    command=CONVERT_AUDIO_COMMAND.format('"%V".wav'),
    condition=Condition.model_validate(
        {
            "extension": {
                "ne": ".wav",
            },
        },
    ),
)

ConvertToMP3 = ContextMenu(
    display_text="Convert to MP3",
    command=CONVERT_AUDIO_COMMAND.format('"%V".mp3'),
    condition=Condition.model_validate(
        {
            "extension": {
                "ne": ".mp3",
            },
        },
    ),
)

ConvertToOGG = ContextMenu(
    display_text="Convert to OGG",
    command=CONVERT_AUDIO_COMMAND.format('"%V".ogg'),
    condition=Condition.model_validate(
        {
            "extension": {
                "ne": ".ogg",
            },
        },
    ),
)

ConvertToFLAC = ContextMenu(
    display_text="Convert to FLAC",
    command=CONVERT_AUDIO_COMMAND.format('"%V".flac'),
    condition=Condition.model_validate(
        {
            "extension": {
                "ne": ".flac",
            },
        },
    ),
)

menu = ContextMenu(
    display_text="Convert to...",
    icon=r"D:\Pictures\Convert_arrow.ico",
    condition=Condition.model_validate(
        {
            "extension": {
                "in": [".mp3", ".wav", ".ogg", ".flac"],
            },
        },
    ),
    submenus=[
        ConvertToWAV,
        ConvertToMP3,
        ConvertToOGG,
        ConvertToFLAC,
    ],
)

if __name__ == "__main__":
    RegistryHandler().apply_context_menu(
        menu,
        bindings=[
            ContextMenuBinding(
                ExplorerItemType.ALL_FILES,
            ),
        ],
    )
