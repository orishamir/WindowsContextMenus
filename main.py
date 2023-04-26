from src.location import Location
from src.registry_interaction import apply_context_menu
from src.registry_structs.registry_key import RegistryKey
from src.context_menu import ContextMenu
from src.features import Command, EntryName

main: ContextMenu = ContextMenu(
    "main",
    [
        EntryName("ballssszz"),
    ],
    [
        ContextMenu(
            "MyTest2",
            [
                EntryName("Open with MyTest555"),
                Command('"c:\\windows\\system32\\cmd.exe" /c start chrome www.gmail.com'),
            ]
        ),
        ContextMenu(
            "MyTest1",
            [
                EntryName("Open with MyTest1312"),
                Command('"c:\\windows\\system32\\cmd.exe" /c start chrome www.ynet.co.il'),
            ]
        )
    ]
)

apply_context_menu(
    main,
    [Location.FILE]
)
