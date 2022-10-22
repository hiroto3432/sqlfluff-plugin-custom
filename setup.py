"""Setup file for example plugin."""
from setuptools import find_packages, setup

# Change these names in your plugin, e.g. company name or plugin purpose.
PLUGIN_LOGICAL_NAME = "custom"
PLUGIN_ROOT_MODULE = "custom"

setup(
    name="sqlfluff-plugin-{plugin_logical_name}".format(
        plugin_logical_name=PLUGIN_LOGICAL_NAME
    ),
    version="0.1.0",
    author="hiroto3432",
    include_package_data=True,
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires="sqlfluff>=0.4.0",
    entry_points={
        "sqlfluff": [
            "{plugin_logical_name} = {plugin_root_module}.rules".format(
                plugin_logical_name=PLUGIN_LOGICAL_NAME,
                plugin_root_module=PLUGIN_ROOT_MODULE,
            )
        ]
    },
)
