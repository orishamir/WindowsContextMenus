from context_menu_toolkit.models.condition_comparisons import (
    ContainsComparison,
    DosWildcardComparison,
    EndswithComparison,
    EqualsComparison,
    GreaterThanComparison,
    GreaterThanEqualsComparison,
    InComparison,
    LessThanComparison,
    LessThanEqualsComparison,
    NinComparison,
    NotEqualsComparison,
    StartswithComparison,
)
from context_menu_toolkit.models.conditions import Condition
from context_menu_toolkit.registry.aqs_conditions.aqs_property_condition import AqsProperty, AqsPropertyCondition, ComparisonType
from context_menu_toolkit.registry.aqs_conditions.custom_aqs_condition import CustomAqsCondition
from context_menu_toolkit.registry.aqs_conditions.iaqscondition import IAqsCondition
from context_menu_toolkit.registry.aqs_conditions.logical_conditions import AqsAnd, AqsNot, AqsOr


class AqsConditionsExporter:
    def export_as_aqs_condition(self, condition: Condition) -> IAqsCondition:
        """Export Condition as a registry Advanced Query Syntax condition."""
        conditions: list[IAqsCondition] = []

        if condition.file_name is not None:
            conditions.append(self._compute_aqs_condition(AqsProperty.FILE_NAME, condition.file_name))

        if condition.file_size is not None:
            conditions.append(self._compute_aqs_condition(AqsProperty.FILE_SIZE, condition.file_size))

        if condition.extension is not None:
            conditions.append(self._compute_aqs_condition(AqsProperty.FILE_EXTENSION, condition.extension))

        if condition.custom_aqs_condition is not None:
            conditions.append(CustomAqsCondition(condition.custom_aqs_condition))

        if condition.and_ is not None:
            conditions.append(
                AqsAnd(
                    [self.export_as_aqs_condition(subcondition) for subcondition in condition.and_],
                ),
            )

        if condition.not_ is not None:
            conditions.append(
                AqsNot(
                    self.export_as_aqs_condition(condition.not_),
                ),
            )

        if condition.nor is not None:
            conditions.append(
                AqsAnd(
                    [AqsNot(self.export_as_aqs_condition(subcondition)) for subcondition in condition.nor],
                ),
            )

        if condition.or_ is not None:
            conditions.append(
                AqsOr(
                    [self.export_as_aqs_condition(subcondition) for subcondition in condition.or_],
                ),
            )

        assert len(conditions) > 0

        if len(conditions) == 1:
            return conditions[0]

        return AqsAnd(conditions)

    def _compute_aqs_condition[T](  # noqa: PLR0912
        self,
        property: AqsProperty,
        comparison: ContainsComparison[T]
        | DosWildcardComparison[T]
        | EndswithComparison[T]
        | EqualsComparison[T]
        | GreaterThanComparison[T]
        | GreaterThanEqualsComparison[T]
        | LessThanComparison[T]
        | LessThanEqualsComparison[T]
        | NotEqualsComparison[T]
        | StartswithComparison[T]
        | InComparison[T]
        | NinComparison[T],
    ) -> IAqsCondition:
        conditions: list[IAqsCondition] = []

        if isinstance(comparison, ContainsComparison) and comparison.contains is not None:
            conditions.append(
                AqsPropertyCondition(
                    property=property,
                    comparison=ComparisonType.CONTAINS,
                    value=comparison.contains,
                ),
            )

        if isinstance(comparison, DosWildcardComparison) and comparison.wildcard is not None:
            conditions.append(
                AqsPropertyCondition(
                    property=property,
                    comparison=ComparisonType.DOS_WILDCARD,
                    value=comparison.wildcard,
                ),
            )

        if isinstance(comparison, EndswithComparison) and comparison.endswith is not None:
            conditions.append(
                AqsPropertyCondition(
                    property=property,
                    comparison=ComparisonType.ENDS_WITH,
                    value=comparison.endswith,
                ),
            )

        if isinstance(comparison, EqualsComparison) and comparison.eq is not None:
            conditions.append(
                AqsPropertyCondition(
                    property=property,
                    comparison=ComparisonType.EQUALS,
                    value=comparison.eq,
                ),
            )

        if isinstance(comparison, GreaterThanComparison) and comparison.gt is not None:
            conditions.append(
                AqsPropertyCondition(
                    property=property,
                    comparison=ComparisonType.GREATER_THAN,
                    value=comparison.gt,
                ),
            )

        if isinstance(comparison, GreaterThanEqualsComparison) and comparison.gte is not None:
            conditions.append(
                AqsPropertyCondition(
                    property=property,
                    comparison=ComparisonType.GREATER_THAN_EQUAL,
                    value=comparison.gte,
                ),
            )

        if isinstance(comparison, LessThanComparison) and comparison.lt is not None:
            conditions.append(
                AqsPropertyCondition(
                    property=property,
                    comparison=ComparisonType.LESS_THAN,
                    value=comparison.lt,
                ),
            )

        if isinstance(comparison, LessThanEqualsComparison) and comparison.lte is not None:
            conditions.append(
                AqsPropertyCondition(
                    property=property,
                    comparison=ComparisonType.LESS_THAN_EQUAL,
                    value=comparison.lte,
                ),
            )

        if isinstance(comparison, NotEqualsComparison) and comparison.ne is not None:
            conditions.append(
                AqsPropertyCondition(
                    property=property,
                    comparison=ComparisonType.NOT_EQUAL,
                    value=comparison.ne,
                ),
            )

        if isinstance(comparison, StartswithComparison) and comparison.startswith is not None:
            conditions.append(
                AqsPropertyCondition(
                    property=property,
                    comparison=ComparisonType.STARTS_WITH,
                    value=comparison.startswith,
                ),
            )

        if isinstance(comparison, InComparison) and comparison.in_ is not None:
            conditions.append(
                AqsOr(
                    [
                        AqsPropertyCondition(
                            property=property,
                            comparison=ComparisonType.EQUALS,
                            value=inner_comparison,
                        )
                        for inner_comparison in comparison.in_
                    ],
                ),
            )

        if isinstance(comparison, NinComparison) and comparison.nin is not None:
            conditions.append(
                AqsAnd(
                    [
                        AqsPropertyCondition(
                            property=property,
                            comparison=ComparisonType.NOT_EQUAL,
                            value=inner_comparison,
                        )
                        for inner_comparison in comparison.nin
                    ],
                ),
            )

        assert len(conditions) > 0

        if len(conditions) == 1:
            return conditions[0]

        return AqsAnd(conditions)
