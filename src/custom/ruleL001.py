from sqlfluff.core.rules import (
    BaseRule,
    LintResult,
    RuleContext,
)

from sqlfluff.core.rules.crawlers import SegmentSeekerCrawler
from sqlfluff.core.rules.doc_decorators import (
    document_configuration,
    document_fix_compatible,
    document_groups,
)
from typing import List


@document_groups
@document_fix_compatible
@document_configuration
class Rule_Custom_L001(BaseRule):
    """When adding a column with a not null constraint, must be set a non-null default value.

    **Anti-pattern**

    Does not set default value for columns with not null constraints.

    .. code-block:: sql

        ALTER TABLE tbl
        ADD COLUMN col1 TEXT
        NOT NULL

    **Best practice**

    Set default value for columns with not null constraints.

    .. code-block:: sql

        ALTER TABLE tbl
        ADD COLUMN col1 TEXT
        DEFAULT '' NOT NULL
    """

    groups = ("all",)
    crawl_behaviour = SegmentSeekerCrawler({"column_reference"})

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _eval(self, context: RuleContext):
        for stack in context.parent_stack:
            if stack.is_type('alter_table_action_segment'):
                phrases = stack.raw.lower().split()
                if not self.is_sql_for_adding_columns(phrases):
                    continue

                if self.has_notnull_constraint(phrases) and not self.has_default_value_other_than_null(phrases):
                    return LintResult(
                        anchor=stack,
                        description="Set a non-null default value for columns with a NOT NULL constraint."
                    )

    @staticmethod
    def is_sql_for_adding_columns(phrases: List[str]) -> bool:
        return phrases[0] == 'add'

    @staticmethod
    def has_notnull_constraint(phrases: List[str]) -> bool:
        return 'not' in phrases and phrases[phrases.index('not') + 1] == 'null'

    @staticmethod
    def has_default_value_other_than_null(phrases: List[str]) -> bool:
        return 'default' in phrases and phrases[phrases.index('default') + 1] != 'null'
