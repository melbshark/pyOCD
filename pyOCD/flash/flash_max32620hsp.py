"""
 mbed CMSIS-DAP debugger
 Copyright (c) 2006-2013 ARM Limited

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
"""

from flash import Flash

FLC_BASE        = 0x40002000
CLK_DIV         = 0x00000060
BRST_SIZE       = 0x00000020
FLASH_BASE      = 0x00000000
FLASH_SIZE      = 0x00080000
FLASH_SECTOR    = 0x00002000

flash_algo = { 'load_address' : 0x20000000,
               'instructions' : [
    0xE00ABE00, 0x062D780D, 0x24084068, 0xD3000040, 0x1E644058, 0x1C49D1FA, 0x2A001E52, 0x4770D1F2,
    0x4603b510, 0x4893460c, 0x68414448, 0xf0006888, 0xb1087080, 0xbd102001, 0x4448488e, 0x60486880, 
    0xe7f82000, 0x488b4602, 0x68414448, 0xf0206888, 0x60884070, 0x47702000, 0x44484886, 0x68886841, 
    0x7080f000, 0x2001b108, 0x6a484770, 0x2000b148, 0x6a486248, 0x2002b128, 0x6a486248, 0x2001b108, 
    0x6888e7f2, 0x4070f020, 0x5000f040, 0x20006088, 0xb510e7ea, 0x44484877, 0xf7ff6844, 0xb108ffdd, 
    0xbd102001, 0xf42068a0, 0xf440407f, 0x60a0402a, 0xf04068a0, 0x60a00002, 0x68a0bf00, 0x7080f000, 
    0xd1fa2800, 0xf02068a0, 0x60a04070, 0xf0006a60, 0xb1080002, 0xe7e42001, 0xe7e22000, 0x4605b570, 
    0x44484864, 0xf7ff6844, 0xb108ffb7, 0xbd702001, 0xf42068a0, 0xf440407f, 0x60a040aa, 0x68a06025, 
    0x0004f040, 0xbf0060a0, 0xf00068a0, 0x28007080, 0x68a0d1fa, 0x4070f020, 0x6a6060a0, 0x0002f000, 
    0x2001b108, 0x2000e7e3, 0xe92de7e1, 0x460747f0, 0x4690468a, 0x4448484f, 0x46566844, 0xf0084645, 
    0xb1100003, 0xe8bd2001, 0x464587f0, 0xff84f7ff, 0x2001b108, 0x68a0e7f7, 0x6000f020, 0x68a060a0, 
    0x0010f040, 0xe00e60a0, 0xcd016027, 0x68a06320, 0x0001f040, 0xbf0060a0, 0xf00068a0, 0x28007080, 
    0x1d3fd1fa, 0x2e041f36, 0xf007d303, 0x2800001f, 0x4838d1ea, 0x68c04448, 0xd1212880, 0xd31f2e10, 
    0xf02068a0, 0x60a00010, 0xf04068a0, 0x60a06000, 0x6027e014, 0x6320cd01, 0x6360cd01, 0x63a0cd01, 
    0x63e0cd01, 0xf04068a0, 0x60a00001, 0x68a0bf00, 0x7080f000, 0xd1fa2800, 0x3e103710, 0xd2e82e10, 
    0xd3192e04, 0xf02068a0, 0x60a06000, 0xf04068a0, 0x60a00010, 0x6027e00e, 0x6320cd01, 0xf04068a0, 
    0x60a00001, 0x68a0bf00, 0x7080f000, 0xd1fa2800, 0x1f361d3f, 0xd2ee2e04, 0x68a2b306, 0x6200f022, 
    0x68a260a2, 0x0210f042, 0xf04f60a2, 0x21ff30ff, 0x682ae005, 0x0201ea62, 0x02094010, 0x2e001e76, 
    0x6027d1f7, 0x68a26320, 0x0201f042, 0xbf0060a2, 0xf00268a2, 0x2a007280, 0xbf00d1fa, 0xf02068a0, 
    0x60a04070, 0xf0006a60, 0xb1080002, 0xe76a2001, 0xe7682000, 0x00000004, 0x00000000, 0x00000000, 
    FLC_BASE, CLK_DIV, BRST_SIZE, FLASH_BASE, FLASH_SIZE, FLASH_SECTOR,
                                ],
               'pc_init' : 0x20000021,
               'pc_eraseAll' : 0x20000093,
               'pc_erase_sector' : 0x200000DD,
               'pc_program_page' : 0x2000012B,
               'begin_data' : 0x20003000,       # Analyzer uses a max of 512 B data (128 pages * 4 bytes / page)
               'page_buffers' : [0x20003000, 0x20003800],   # Enable double buffering
               'begin_stack' : 0x20001000,
               'static_base' : 0x20000278,
               'min_program_length' : 4,
               'analyzer_supported' : True,
               'analyzer_address' : 0x20004000  # Analyzer 0x20004000..0x20004600
              };

class Flash_max32620hsp(Flash):

    def __init__(self, target):
        super(Flash_max32620hsp, self).__init__(target, flash_algo)
