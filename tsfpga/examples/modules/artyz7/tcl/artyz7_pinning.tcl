# --------------------------------------------------------------------------------------------------
# Copyright (c) Lukas Vik. All rights reserved.
#
# This file is part of the tsfpga project, a project platform for modern FPGA development.
# https://tsfpga.com
# https://github.com/tsfpga/tsfpga
# --------------------------------------------------------------------------------------------------
# From https://github.com/Digilent/digilent-xdc/blob/master/Arty-Z7-20-Master.xdc
# Further pins and all original names available there.
# --------------------------------------------------------------------------------------------------

# Clock Signal.
set_property -dict {"PACKAGE_PIN" "H16" "IOSTANDARD" "LVCMOS33"} [get_ports "clk_ext"]
create_clock -add -name "clk_ext" -period 8.00 -waveform {0 4} [get_ports "clk_ext"]

# LEDs.
set_property -dict {"PACKAGE_PIN" "R14" "IOSTANDARD" "LVCMOS33"} [get_ports "led[0]"]
set_property -dict {"PACKAGE_PIN" "P14" "IOSTANDARD" "LVCMOS33"} [get_ports "led[1]"]
set_property -dict {"PACKAGE_PIN" "N16" "IOSTANDARD" "LVCMOS33"} [get_ports "led[2]"]
set_property -dict {"PACKAGE_PIN" "M14" "IOSTANDARD" "LVCMOS33"} [get_ports "led[3]"]
