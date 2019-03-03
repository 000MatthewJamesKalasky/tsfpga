import datetime
from collections import OrderedDict

from tsfpga.git_utils import git_commands_are_available, get_git_commit


class Bit:

    def __init__(self, idx, name, description):
        self.idx = idx
        self.name = name
        self.description = description


# mode: (mode_readable, description)
REGISTER_MODES = {
    "r": ("Read", "PS can read a value that PL provides."),
    "w": ("Write", "PS can write a value that is available for PL usage."),
    "r_w": (
        "Read, Write",
        "PS can write a value and read it back. The written value is available for PL usage."),
    "wpulse": ("Write-pulse", "PS can write a value that is asserted for one cycle in PL."),
    "r_wpulse": (
        "Read, Write-pulse",
        "PS can read a value that PL provides. "
        "PS can write a value that is asserted for one cycle in PL."),
}


class Register:

    def __init__(self, name, idx, mode, description=""):
        self.name = name
        self.idx = idx
        self.mode = mode
        self.description = description
        self.bits = []

    def append_bit(self, bit_name, bit_description):
        idx = len(self.bits)
        bit = Bit(idx, bit_name, bit_description)

        self.bits.append(bit)
        return bit

    @property
    def mode_readable(self):
        return REGISTER_MODES[self.mode][0]

    @property
    def address(self):
        address_int = 4 * self.idx
        num_nibbles_needed = 4
        formatting_string = "0x{:0%iX}" % num_nibbles_needed
        return formatting_string.format(address_int)


class RegisterList:

    def __init__(self, name):
        self.name = name
        self.registers = OrderedDict()

    def append(self, register_name, mode):
        idx = len(self.registers)
        register = Register(register_name, idx, mode)

        self.registers[register_name] = register
        return register

    @staticmethod
    def generated_info():
        """
        A string informing the user that a file is automatically generated
        """
        info = "Automatically generated file"
        return info

    @staticmethod
    def generated_source_info():
        """
        A string containing info about the source of the generated register information
        """
        git_commit_info = ""
        if git_commands_are_available():
            git_commit = get_git_commit()
            git_commit_info = "from " + git_commit + " "

        time_info = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

        info = f"Generated {git_commit_info}on {time_info}."
        return info

    def iterate_registers(self):
        for register in self.registers.values():
            yield register