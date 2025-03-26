from context_menu_toolkit import ContextMenu, ContextMenuBinding
from context_menu_toolkit.registry.exporting.registry_exporter import RegistryExporter
from context_menu_toolkit.registry.registry_interaction import write_registry_key
from context_menu_toolkit.registry.registry_structs.registry_key import RegistryKey


class RegistryHandler:
    """Helper for bridging between pure ContextMenu objects and the registry."""

    def __init__(self) -> None:
        """Basic initialization of RegistryHandler."""
        self.exporter = RegistryExporter()

    def apply_context_menu(
        self,
        menu: ContextMenu,
        bindings: list[ContextMenuBinding],
    ) -> None:
        """Apply context menu to the registry for specified bindings."""
        built_menu: RegistryKey = self.exporter.export_tree(menu)

        for binding in bindings:
            write_registry_key(built_menu, binding.construct_registry_path())

    def export_tree(self, menu: ContextMenu) -> RegistryKey:
        """Export as a RegistryKey tree."""
        return self.exporter.export_tree(menu)

    def export_reg_file(self, menu: ContextMenu, bindings: list[ContextMenuBinding]) -> list[str]:
        r"""Export the Context Menu as a .reg file format.

        Syntax of .reg file:
        <https://support.microsoft.com/en-us/topic/how-to-add-modify-or-delete-registry-subkeys-and-values-by-using-a-reg-file-9c7f37cf-a5e9-e1cd-c4fa-2a26218a1a23>

        Example:
            ```
            Windows Registry Editor Version 5.00

            [HKEY_LOCAL_MACHINE\Software\Classes\*\shell\ConvertVideo]
            "MUIVerb"="Convert mp4..."
            ```

        Returns:
            A list of lines of the .reg file.
        """
        return self.exporter.export_reg_file(menu, bindings)
