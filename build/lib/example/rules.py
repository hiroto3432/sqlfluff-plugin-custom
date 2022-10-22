from sqlfluff.core.plugin import hookimpl
from sqlfluff.core.rules import (
    BaseRule,
)
from typing import List
import os.path

from sqlfluff.core.config import ConfigLoader

@hookimpl
def get_rules() -> List[BaseRule]:
    """Get plugin rules."""
    return []


@hookimpl
def load_default_config() -> dict:
    """Loads the default configuration for the plugin."""
    return ConfigLoader.get_global().load_config_file(
        file_dir=os.path.dirname(__file__),
        file_name="plugin_default_config.cfg",
    )
