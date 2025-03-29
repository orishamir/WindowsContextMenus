from context_menu_toolkit.registry.aqs_conditions.iaqscondition import IAqsCondition


class AqsConditionsImporter:
    def import_aqs_to_condition(self, aqs_condition: str) -> IAqsCondition:  # noqa: ARG002
        """Import IAqsCondition from string. With parsing and everything."""
        return NotImplemented
