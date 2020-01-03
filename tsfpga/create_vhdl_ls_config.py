# ------------------------------------------------------------------------------
# Copyright (c) Lukas Vik. All rights reserved.
# ------------------------------------------------------------------------------

from os.path import abspath, dirname, join
import toml



def create_configuration(output_path, modules=None, vunit_proj=None):
    """
    Create a configuration file (vhdl_ls.toml) for the rust_hdl VHDL Language Server.

    Can be used with modules and an "empty" VUnit project, or with a complete VUnit
    project with all user files added.

    Execution of this function takes roughly 12 ms for a large project (62 modules and a
    VUnit project).

    :param output_path: Output folder.
    :param modules: A list of Module objects.
    :param vunit_proj: A VUnit project.
    """
    toml_data = dict(libraries=dict())

    if modules is not None:
        for module in modules:
            vhd_file_wildcard = join(abspath(module.path), "**", "*.vhd")
            toml_data["libraries"][module.library_name] = dict(files=[vhd_file_wildcard])

    if vunit_proj is not None:
        for source_file in vunit_proj.get_compile_order():
            if source_file.library.name not in toml_data["libraries"]:
                toml_data["libraries"][source_file.library.name] = dict(files=[])
            toml_data["libraries"][source_file.library.name]["files"].append(abspath(source_file.name))

    with open(join(output_path, "vhdl_ls.toml"), "w") as output_file_handle:
        toml.dump(toml_data, output_file_handle)
