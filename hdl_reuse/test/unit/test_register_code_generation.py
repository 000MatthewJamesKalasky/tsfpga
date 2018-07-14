import unittest

from hdl_reuse.register_list import RegisterList
from hdl_reuse.register_html_generator import RegisterHtmlGenerator
from hdl_reuse.register_vhdl_generator import RegisterVhdlGenerator


class TestRegisterCodeGeneration(unittest.TestCase):

    def setUp(self):
        register_list = RegisterList("sensor")

        register = register_list.append("conf", "r_w")
        register.description = "conf desc"
        register.append_bit("conf_bit_0", "conf bit 0 desc")
        register.append_bit("conf_bit_1", "")

        register = register_list.append("addr", "w")
        register.description = "addr desc"

        self.html_generator = RegisterHtmlGenerator(register_list)
        self.vhdl_generator = RegisterVhdlGenerator(register_list)

    def test_generated_html_contains_all_fields_in_correct_order(self):
        expected = """
  <tr>
    <td><strong>conf</strong></td>
    <td>0x0000</td>
    <td>Read, Write</td>
    <td>conf desc</td>
  </tr>
  <tr>
    <td>&nbsp;&nbsp;<em>conf_bit_0</em></td>
    <td>0</td>
    <td></td>
    <td>conf bit 0 desc</td>
  </tr>
  <tr>
    <td>&nbsp;&nbsp;<em>conf_bit_1</em></td>
    <td>1</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td><strong>addr</strong></td>
    <td>0x0004</td>
    <td>Write</td>
    <td>addr desc</td>
  </tr>
"""
        assert expected in self.html_generator.get_table()
        assert expected in self.html_generator.get_page()

    # pylint: disable=protected-access
    def test_markdown_parser_can_handle_anntotating_sentences(self):
        expected = "This sentence <b>should have a large portion</b> in bold face"
        text = "This sentence **should have a large portion** in bold face"
        assert expected in self.html_generator._markdown_parser(text)
        text = "This sentence __should have a large portion__ in bold face"
        assert expected in self.html_generator._markdown_parser(text)

        expected = "This sentence <em>should have a large portion</em> in italics"
        text = "This sentence *should have a large portion* in italics"
        assert expected in self.html_generator._markdown_parser(text)
        text = "This sentence _should have a large portion_ in italics"
        assert expected in self.html_generator._markdown_parser(text)

    def test_generated_vhdl_contains_all_fields_in_correct_order(self):
        expected = """
  constant sensor_conf : integer := 0;
  constant sensor_addr : integer := 1;

  constant sensor_reg_map : reg_definition_vec_t(0 to 2 - 1) := (
    (idx => sensor_conf, reg_type => r_w),
    (idx => sensor_addr, reg_type => w)
  );

  constant sensor_conf_conf_bit_0 : integer := 0;
  constant sensor_conf_conf_bit_1 : integer := 1;
"""
        assert expected in self.vhdl_generator.get_package()
