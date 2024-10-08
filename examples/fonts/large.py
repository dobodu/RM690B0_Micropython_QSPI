# -*- coding: utf-8 -*-
# Converted from arial_mod.ttf using:
#     font2bitmap.py -c 0x20-0x7A arial_mod.ttf 32

MAP = (
    ' !\"#$%&\'()*+,-./0123456789:;<='
    '>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ['
    '\\]^_`abcdefghijklmnopqrstuvwxyz'
)

BPP = 1
HEIGHT = 31
MAX_WIDTH = 32
_WIDTHS = \
    b'\x09\x0b\x0b\x12\x12\x1c\x15\x06\x0b\x0b\x0c\x13\x09\x13\x09\x09'\
    b'\x12\x12\x12\x12\x12\x12\x12\x12\x12\x12\x09\x09\x13\x13\x13\x12'\
    b'\x20\x15\x15\x17\x17\x15\x14\x19\x17\x09\x10\x16\x12\x1b\x17\x19'\
    b'\x15\x19\x17\x15\x13\x17\x15\x20\x15\x15\x14\x09\x0a\x09\x0e\x13'\
    b'\x0b\x11\x11\x10\x11\x11\x0a\x11\x12\x07\x08\x10\x07\x1b\x12\x11'\
    b'\x11\x11\x0b\x10\x09\x12\x0f\x19\x0e\x0f\x0f'

OFFSET_WIDTH = 2
_OFFSETS = \
    b'\x00\x00\x01\x17\x02\x6c\x03\xc1\x05\xef\x08\x1d\x0b\x81\x0e\x0c'\
    b'\x0e\xc6\x10\x1b\x11\x70\x12\xe4\x15\x31\x16\x48\x18\x95\x19\xac'\
    b'\x1a\xc3\x1c\xf1\x1f\x1f\x21\x4d\x23\x7b\x25\xa9\x27\xd7\x2a\x05'\
    b'\x2c\x33\x2e\x61\x30\x8f\x31\xa6\x32\xbd\x35\x0a\x37\x57\x39\xa4'\
    b'\x3b\xd2\x3f\xb2\x42\x3d\x44\xc8\x47\x91\x4a\x5a\x4c\xe5\x4f\x51'\
    b'\x52\x58\x55\x21\x56\x38\x58\x28\x5a\xd2\x5d\x00\x60\x45\x63\x0e'\
    b'\x66\x15\x68\xa0\x6b\xa7\x6e\x70\x70\xfb\x73\x48\x76\x11\x78\x9c'\
    b'\x7c\x7c\x7f\x07\x81\x92\x83\xfe\x85\x15\x86\x4b\x87\x62\x89\x14'\
    b'\x8b\x61\x8c\xb6\x8e\xc5\x90\xd4\x92\xc4\x94\xd3\x96\xe2\x98\x18'\
    b'\x9a\x27\x9c\x55\x9d\x2e\x9e\x26\xa0\x16\xa0\xef\xa4\x34\xa6\x62'\
    b'\xa8\x71\xaa\x80\xac\x8f\xad\xe4\xaf\xd4\xb0\xeb\xb3\x19\xb4\xea'\
    b'\xb7\xf1\xb9\xa3\xbb\x74'

_BITMAPS =\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x03\x80\x70\x0e\x01\xc0\x38\x07\x00\xe0\x1c\x03'\
    b'\x80\x70\x0e\x01\xc0\x10\x02\x00\x40\x08\x01\x00\x20\x00\x00\x00'\
    b'\x38\x07\x00\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xe3'\
    b'\x9c\x73\x8e\x71\xce\x39\xc7\x38\xe2\x08\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x70\xe0\x1c\x38\x0e'\
    b'\x1c\x03\x87\x00\xe1\xc0\x38\x71\xff\xff\x7f\xff\xdf\xff\xf0\x70'\
    b'\xe0\x1c\x38\x0f\x1e\x03\x87\x00\xe1\xc1\xff\xff\x7f\xff\xdf\xff'\
    b'\xf1\xc3\x80\x70\xe0\x1c\x38\x07\x0e\x03\x87\x00\xe1\xc0\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x80'\
    b'\x01\xf8\x01\xff\x80\xff\xf0\x79\x9c\x1c\x63\x87\x18\xe1\xc6\x00'\
    b'\x71\x80\x0f\x60\x03\xf8\x00\x7f\xc0\x07\xfc\x00\x7f\x80\x19\xe0'\
    b'\x06\x3c\x01\x87\x38\x61\xce\x18\x73\xc6\x3c\x79\x9e\x0f\xff\x01'\
    b'\xff\x80\x1f\xc0\x01\x80\x00\x60\x00\x18\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x03\xc0\x0e\x00\xff\x01\xc0\x0e\x70'\
    b'\x1c\x01\xc3\x83\x80\x1c\x38\x38\x01\xc3\x87\x00\x1c\x38\x70\x01'\
    b'\xc3\x8e\x00\x1c\x38\xe0\x00\xe7\x1c\x00\x0f\xe1\xc0\x00\x3c\x38'\
    b'\xf0\x00\x03\xbf\xc0\x00\x73\x9c\x00\x0f\x70\xe0\x00\xe7\x0e\x00'\
    b'\x1c\x70\xe0\x01\xc7\x0e\x00\x38\x70\xe0\x03\x87\x0e\x00\x70\x39'\
    b'\xc0\x07\x03\xfc\x00\xe0\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x07\xc0\x00\x7f\x80\x07\xfc\x00\x78\xf0\x03\x83\x80'\
    b'\x1c\x1c\x00\xe0\xe0\x03\x8e\x00\x0f\xe0\x00\x7e\x00\x07\xe0\x00'\
    b'\x7f\x00\x07\x9c\x00\x70\x71\xc7\x01\xdc\x38\x0e\xe1\xc0\x3e\x0e'\
    b'\x00\xe0\x78\x07\x81\xe0\xfe\x07\xff\xb8\x1f\xf9\xe0\x3f\x04\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x1c\x71\xc7\x1c\x71\xc2\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x60\x18\x06\x01\xc0'\
    b'\x30\x0e\x01\x80\x70\x0e\x01\xc0\x70\x0e\x01\xc0\x38\x07\x00\xe0'\
    b'\x1c\x03\x80\x70\x07\x00\xe0\x1c\x01\xc0\x38\x03\x00\x70\x06\x00'\
    b'\x60\x06\x00\x00\x01\x80\x18\x01\x80\x38\x03\x00\x70\x06\x00\xe0'\
    b'\x1c\x03\x80\x38\x07\x00\xe0\x1c\x03\x80\x70\x0e\x01\xc0\x38\x0e'\
    b'\x01\xc0\x38\x0e\x01\xc0\x30\x0e\x01\x80\x60\x18\x00\x00\x00\x00'\
    b'\x60\x06\x00\x60\x76\xe7\xfe\x1f\x80\xf0\x1f\x83\x9c\x10\x80\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1c\x00\x03\x80\x00\x70\x00'\
    b'\x0e\x00\x01\xc0\x00\x38\x01\xff\xfc\x3f\xff\x87\xff\xf0\x03\x80'\
    b'\x00\x70\x00\x0e\x00\x01\xc0\x00\x38\x00\x07\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x70\x38'\
    b'\x1c\x06\x03\x01\x80\x80\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x1f\xff\xc3\xff\xf8\x7f\xff\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x03\x81\xc0\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x0c\x06\x06\x03\x01\x81\x80\xc0\x60'\
    b'\x60\x30\x18\x1c\x0c\x06\x03\x03\x01\x80\xc0\xc0\x60\x30\x38\x18'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1f\x80\x1f\xf8\x0f'\
    b'\xff\x07\xc3\xc1\xc0\x78\x70\x0e\x38\x03\xce\x00\x73\x80\x1c\xe0'\
    b'\x07\x38\x01\xce\x00\x73\x80\x1c\xe0\x07\x38\x01\xce\x00\x73\x80'\
    b'\x1c\x70\x0e\x1c\x03\x87\xc3\xe0\xff\xf0\x1f\xf8\x01\xf8\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x06\x00\x03\x80\x01\xe0\x00\xf8\x00\xfe\x00\x7f\x80\x3c\xe0'\
    b'\x0c\x38\x00\x0e\x00\x03\x80\x00\xe0\x00\x38\x00\x0e\x00\x03\x80'\
    b'\x00\xe0\x00\x38\x00\x0e\x00\x03\x80\x00\xe0\x00\x38\x00\x0e\x00'\
    b'\x03\x80\x00\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x03\xf8\x03\xff\x81\xff\xf0\x78\x3c\x38'\
    b'\x07\x8e\x00\xe0\x00\x38\x00\x0e\x00\x03\x80\x01\xc0\x00\x70\x00'\
    b'\x38\x00\x1c\x00\x0e\x00\x07\x00\x07\x80\x03\xc0\x01\xc0\x00\xe0'\
    b'\x00\x70\x00\x1f\xff\x8f\xff\xe3\xff\xf8\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\xe0\x07\xfe'\
    b'\x03\xff\xc1\xe0\xf0\xf0\x1e\x38\x03\x80\x00\xe0\x00\x78\x00\x3c'\
    b'\x00\xfe\x00\x3f\x80\x0f\xf0\x00\x1e\x00\x03\xc0\x00\x70\x00\x1c'\
    b'\x00\x07\x38\x01\xcf\x00\xe1\xe0\x78\x3f\xfc\x07\xfe\x00\xfe\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x60\x00\x38\x00\x1e\x00\x0f\x80\x03\xe0\x01\xf8\x00'\
    b'\xee\x00\x7b\x80\x1c\xe0\x0e\x38\x07\x0e\x01\xc3\x80\xe0\xe0\x70'\
    b'\x38\x38\x0e\x0f\xff\xf3\xff\xfc\xff\xff\x00\x0e\x00\x03\x80\x00'\
    b'\xe0\x00\x38\x00\x0e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x03\xff\xe0\xff\xf8\x3f\xfe\x1c\x00'\
    b'\x07\x00\x01\xc0\x00\x70\x00\x1c\xf8\x06\xff\x83\xff\xf0\xf8\x1e'\
    b'\x38\x03\x80\x00\x70\x00\x1c\x00\x07\x00\x01\xc0\x00\x73\x80\x3c'\
    b'\xf0\x0e\x1e\x07\x87\xff\xc0\x7f\xe0\x0f\xe0\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfc\x00'\
    b'\xff\xc0\x7f\xf8\x3c\x1e\x1e\x03\xc7\x00\x71\xc0\x00\xe0\x00\x38'\
    b'\xfc\x0e\xff\x83\xff\xf0\xfc\x1e\x3c\x03\xce\x00\x73\x80\x1c\xe0'\
    b'\x07\x38\x01\xc7\x00\x71\xc0\x38\x3c\x1e\x0f\xff\x01\xff\x80\x1f'\
    b'\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x7f\xff\x1f\xff\xc7\xff\xf0\x00\x18\x00\x0c\x00\x07'\
    b'\x00\x03\x80\x01\xc0\x00\x70\x00\x38\x00\x0e\x00\x07\x00\x01\xc0'\
    b'\x00\xe0\x00\x38\x00\x1c\x00\x07\x00\x01\xc0\x00\x70\x00\x38\x00'\
    b'\x0e\x00\x03\x80\x00\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1f\x80\x1f\xf8\x0f\xff\x07'\
    b'\x81\xc1\xc0\x38\x70\x0e\x1c\x03\x87\x00\xe0\xe0\x70\x1f\xf8\x03'\
    b'\xfc\x03\xff\xc1\xe0\x78\x70\x0e\x38\x01\xce\x00\x73\x80\x1c\xe0'\
    b'\x07\x3c\x03\xc7\x81\xe0\xff\xf0\x1f\xf8\x01\xf8\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x7e'\
    b'\x00\x7f\xc0\x3f\xfc\x1f\x07\x07\x00\xe3\xc0\x18\xe0\x07\x38\x01'\
    b'\xce\x00\x73\x80\x1c\xf0\x0f\x1e\x07\xc3\xff\xf0\x7f\xdc\x0f\xc7'\
    b'\x00\x01\xc0\x00\xe3\x80\x38\xf0\x1e\x1e\x0f\x07\xff\x80\xff\xc0'\
    b'\x0f\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x70\x38\x1c\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\xc0\xe0\x70\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xe0\x70\x38'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x81\xc0\xe0'\
    b'\x30\x18\x0c\x04\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x08\x00\x0f\x00\x07\xe0\x07\xf8\x03\xf8\x03'\
    b'\xf8\x00\xfc\x00\x1c\x00\x03\xf0\x00\x3f\x80\x00\xfe\x00\x07\xf8'\
    b'\x00\x1f\x80\x00\xf0\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x7f\xff\x0f\xff\xe1\xff\xfc\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x03\xff\xf8\x7f\xff\x0f\xff\xe0\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x80\x00\x1e\x00\x03\xf0\x00\x3f\xc0'\
    b'\x00\xfe\x00\x03\xf8\x00\x1f\x80\x00\x70\x00\x7e\x00\x3f\x80\x3f'\
    b'\x80\x3f\xc0\x0f\xc0\x01\xe0\x00\x20\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x0f\xc0\x0f\xfc\x07\xff\x83\xe1\xf0'\
    b'\xe0\x1e\x70\x03\x9c\x00\xe0\x00\x38\x00\x1e\x00\x0f\x00\x07\x80'\
    b'\x03\xc0\x01\xe0\x00\x70\x00\x3c\x00\x0e\x00\x03\x80\x00\xe0\x00'\
    b'\x00\x00\x00\x00\x03\x80\x00\xe0\x00\x38\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01'\
    b'\xff\x00\x00\x0f\xff\xc0\x00\x1f\xff\xf0\x00\x7f\x01\xf8\x00\xf8'\
    b'\x00\x7c\x01\xf0\x00\x1e\x01\xe1\xf1\xcf\x03\xc3\xfb\xc7\x03\x87'\
    b'\xff\x87\x07\x0f\x1f\x83\x87\x1e\x0f\x83\x87\x1c\x07\x83\x8e\x1c'\
    b'\x07\x03\x8e\x38\x07\x03\x8e\x38\x07\x03\x8e\x38\x07\x07\x0e\x38'\
    b'\x0f\x07\x0e\x38\x0e\x0e\x0e\x3c\x1e\x1e\x0f\x1e\x3e\x3c\x07\x1f'\
    b'\xff\xf8\x07\x0f\xef\xf0\x07\x87\x87\xc0\x03\xc0\x00\x01\xc1\xe0'\
    b'\x00\x07\x81\xf8\x00\x0f\x00\x7f\x00\x7e\x00\x3f\xff\xfc\x00\x0f'\
    b'\xff\xf0\x00\x01\xff\x80\x00\x00\x00\x01\xf0\x00\x0f\x80\x00\x7c'\
    b'\x00\x07\x70\x00\x3b\x80\x01\xdc\x00\x1c\x70\x00\xe3\x80\x0e\x0e'\
    b'\x00\x70\x70\x03\x83\x80\x38\x0e\x01\xc0\x70\x0f\xff\x80\xff\xfe'\
    b'\x07\xff\xf0\x70\x01\xc3\x80\x0e\x1c\x00\x71\xc0\x01\xce\x00\x0e'\
    b'\x70\x00\x77\x00\x01\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\xff\x80\x3f\xff\x01'\
    b'\xff\xfc\x0e\x01\xf0\x70\x03\x83\x80\x1c\x1c\x00\xe0\xe0\x07\x07'\
    b'\x00\xf0\x3f\xff\x01\xff\xf8\x0f\xff\xe0\x70\x07\x83\x80\x1e\x1c'\
    b'\x00\x70\xe0\x03\x87\x00\x1c\x38\x00\xe1\xc0\x0f\x0e\x00\xf0\x7f'\
    b'\xff\x83\xff\xf8\x1f\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\xfc\x00\x0f'\
    b'\xfe\x00\x3f\xff\x00\xf8\x1e\x03\xc0\x1e\x0f\x00\x1e\x1c\x00\x1c'\
    b'\x78\x00\x00\xe0\x00\x01\xc0\x00\x03\x80\x00\x07\x00\x00\x0e\x00'\
    b'\x00\x1c\x00\x00\x38\x00\x00\x38\x00\x1c\x70\x00\x78\xf0\x00\xe0'\
    b'\xf0\x03\xc0\xf8\x1f\x00\xff\xfc\x00\xff\xf0\x00\x7f\x80\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x1f\xff\x00\x3f\xff\x80\x7f\xff\x80\xe0\x0f'\
    b'\x81\xc0\x07\x03\x80\x0f\x07\x00\x0e\x0e\x00\x1e\x1c\x00\x1c\x38'\
    b'\x00\x38\x70\x00\x70\xe0\x00\xe1\xc0\x01\xc3\x80\x03\x87\x00\x07'\
    b'\x0e\x00\x1e\x1c\x00\x38\x38\x00\xf0\x70\x01\xc0\xe0\x0f\x81\xff'\
    b'\xfe\x03\xff\xf8\x07\xff\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x3f\xff'\
    b'\x81\xff\xfc\x0f\xff\xe0\x70\x00\x03\x80\x00\x1c\x00\x00\xe0\x00'\
    b'\x07\x00\x00\x38\x00\x01\xff\xf8\x0f\xff\xc0\x7f\xfe\x03\x80\x00'\
    b'\x1c\x00\x00\xe0\x00\x07\x00\x00\x38\x00\x01\xc0\x00\x0e\x00\x00'\
    b'\x70\x00\x03\xff\xfc\x1f\xff\xe0\xff\xff\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f'\
    b'\xff\xf0\xff\xff\x0f\xff\xf0\xe0\x00\x0e\x00\x00\xe0\x00\x0e\x00'\
    b'\x00\xe0\x00\x0e\x00\x00\xe0\x00\x0f\xff\xc0\xff\xfc\x0f\xff\xc0'\
    b'\xe0\x00\x0e\x00\x00\xe0\x00\x0e\x00\x00\xe0\x00\x0e\x00\x00\xe0'\
    b'\x00\x0e\x00\x00\xe0\x00\x0e\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1f\xe0'\
    b'\x00\x7f\xfc\x00\x7f\xff\x00\x7c\x07\xc0\x78\x00\xf0\x78\x00\x38'\
    b'\x38\x00\x1e\x1c\x00\x00\x1c\x00\x00\x0e\x00\x00\x07\x00\x00\x03'\
    b'\x80\x3f\xf1\xc0\x1f\xf8\xe0\x0f\xfc\x70\x00\x0e\x1c\x00\x07\x0e'\
    b'\x00\x03\x87\x80\x01\xc1\xe0\x01\xe0\x7e\x07\xf0\x1f\xff\xf0\x03'\
    b'\xff\xe0\x00\x7f\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x38\x00'\
    b'\xe0\x70\x01\xc0\xe0\x03\x81\xc0\x07\x03\x80\x0e\x07\x00\x1c\x0e'\
    b'\x00\x38\x1c\x00\x70\x38\x00\xe0\x7f\xff\xc0\xff\xff\x81\xff\xff'\
    b'\x03\x80\x0e\x07\x00\x1c\x0e\x00\x38\x1c\x00\x70\x38\x00\xe0\x70'\
    b'\x01\xc0\xe0\x03\x81\xc0\x07\x03\x80\x0e\x07\x00\x1c\x0e\x00\x38'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x07\x03\x81\xc0\xe0\x70\x38\x1c\x0e\x07\x03'\
    b'\x81\xc0\xe0\x70\x38\x1c\x0e\x07\x03\x81\xc0\xe0\x70\x38\x1c\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x38\x00\x38\x00\x38\x00'\
    b'\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00'\
    b'\x38\x00\x38\x00\x38\x00\x38\x00\x38\x70\x38\x70\x38\x70\x38\x78'\
    b'\x70\x3f\xf0\x1f\xe0\x0f\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x70\x01\xe1\xc0\x0f\x07\x00\x78'\
    b'\x1c\x03\xc0\x70\x1e\x01\xc0\xf0\x07\x07\x80\x1c\x3c\x00\x71\xe0'\
    b'\x01\xcf\x00\x07\x7c\x00\x1f\xf8\x00\x7e\xf0\x01\xf1\xe0\x07\x87'\
    b'\x80\x1c\x0f\x00\x70\x1e\x01\xc0\x3c\x07\x00\x70\x1c\x00\xe0\x70'\
    b'\x03\xc1\xc0\x07\x87\x00\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\xc0\x00\x70'\
    b'\x00\x1c\x00\x07\x00\x01\xc0\x00\x70\x00\x1c\x00\x07\x00\x01\xc0'\
    b'\x00\x70\x00\x1c\x00\x07\x00\x01\xc0\x00\x70\x00\x1c\x00\x07\x00'\
    b'\x01\xc0\x00\x70\x00\x1c\x00\x07\x00\x01\xff\xf8\x7f\xfe\x1f\xff'\
    b'\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x03\xe0\x03\xe0\x7c\x00\x7c\x0f\xc0\x1f\x81\xf8\x03'\
    b'\xf0\x3f\x00\x7e\x07\x70\x1d\xc0\xee\x03\xb8\x1d\xc0\x77\x03\x98'\
    b'\x0c\xe0\x73\x83\x9c\x0e\x70\x73\x81\xce\x0e\x70\x38\xe3\x8e\x07'\
    b'\x1c\x71\xc0\xe3\x8e\x38\x1c\x31\x87\x03\x87\x70\xe0\x70\xee\x1c'\
    b'\x0e\x1d\xc3\x81\xc1\xb0\x70\x38\x3e\x0e\x07\x07\xc1\xc0\xe0\x70'\
    b'\x38\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\xc0\x07\x03\xc0'\
    b'\x0e\x07\xc0\x1c\x0f\x80\x38\x1f\x80\x70\x3f\x00\xe0\x77\x01\xc0'\
    b'\xe7\x03\x81\xce\x07\x03\x8e\x0e\x07\x1c\x1c\x0e\x1c\x38\x1c\x1c'\
    b'\x70\x38\x38\xe0\x70\x39\xc0\xe0\x73\x81\xc0\x77\x03\x80\x7e\x07'\
    b'\x00\xfc\x0e\x00\xf8\x1c\x01\xf0\x38\x01\xe0\x70\x01\xc0\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\xfe\x00\x03\xff\xe0\x03\xff\xf8\x03\xe0'\
    b'\x3e\x03\xc0\x07\x83\xc0\x01\xe1\xc0\x00\x70\xe0\x00\x38\xe0\x00'\
    b'\x0e\x70\x00\x07\x38\x00\x03\x9c\x00\x01\xce\x00\x00\xe7\x00\x00'\
    b'\x73\x80\x00\x38\xe0\x00\x38\x70\x00\x1c\x3c\x00\x1e\x0f\x00\x1e'\
    b'\x03\xe0\x3e\x00\xff\xfe\x00\x3f\xfe\x00\x03\xf8\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x07\xff\xc0\x3f\xff\x81\xff\xfe\x0e\x00\xf0'\
    b'\x70\x03\xc3\x80\x0e\x1c\x00\x70\xe0\x03\x87\x00\x1c\x38\x01\xe1'\
    b'\xc0\x1e\x0f\xff\xf0\x7f\xff\x03\xff\xe0\x1c\x00\x00\xe0\x00\x07'\
    b'\x00\x00\x38\x00\x01\xc0\x00\x0e\x00\x00\x70\x00\x03\x80\x00\x1c'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x3f\x80\x00\xff\xf0\x00\xff\xfc'\
    b'\x00\xf8\x1f\x00\xf0\x03\xc0\xf0\x00\xf0\x70\x00\x38\x38\x00\x1c'\
    b'\x38\x00\x07\x1c\x00\x03\x8e\x00\x01\xc7\x00\x00\xe3\x80\x00\x71'\
    b'\xc0\x00\x38\xe0\x00\x1c\x38\x00\x1c\x1c\x02\x0e\x0f\x03\xcf\x03'\
    b'\xc0\xff\x00\xf8\x1f\x00\x3f\xff\xc0\x0f\xff\xf0\x00\xfe\x3e\x00'\
    b'\x00\x0e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x7f\xfc\x00\xff\xfe\x01\xff\xfe'\
    b'\x03\x80\x3c\x07\x00\x3c\x0e\x00\x38\x1c\x00\x70\x38\x00\xe0\x70'\
    b'\x03\xc0\xe0\x0f\x01\xff\xfe\x03\xff\xf8\x07\xff\xc0\x0e\x0f\x00'\
    b'\x1c\x0f\x00\x38\x0f\x00\x70\x0e\x00\xe0\x1e\x01\xc0\x1e\x03\x80'\
    b'\x1c\x07\x00\x3c\x0e\x00\x38\x1c\x00\x78\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x1f\xc0\x03\xff\x80\x3f\xfe\x01\xe0\x78\x1e\x01\xe0\xe0\x07'\
    b'\x07\x00\x38\x38\x00\x00\xe0\x00\x07\xf0\x00\x1f\xf8\x00\x3f\xf0'\
    b'\x00\x1f\xc0\x00\x1f\x00\x00\x3c\x70\x00\xe3\x80\x07\x1e\x00\x38'\
    b'\x70\x03\xc3\xe0\x7c\x0f\xff\xc0\x3f\xfc\x00\x3f\x80\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x03\xff\xff\xff\xff\xff\xff\xfe\x01\xc0\x00\x38\x00\x07\x00'\
    b'\x00\xe0\x00\x1c\x00\x03\x80\x00\x70\x00\x0e\x00\x01\xc0\x00\x38'\
    b'\x00\x07\x00\x00\xe0\x00\x1c\x00\x03\x80\x00\x70\x00\x0e\x00\x01'\
    b'\xc0\x00\x38\x00\x07\x00\x00\xe0\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x38\x00\xe0\x70'\
    b'\x01\xc0\xe0\x03\x81\xc0\x07\x03\x80\x0e\x07\x00\x1c\x0e\x00\x38'\
    b'\x1c\x00\x70\x38\x00\xe0\x70\x01\xc0\xe0\x03\x81\xc0\x07\x03\x80'\
    b'\x0e\x07\x00\x1c\x0e\x00\x38\x1c\x00\x70\x38\x00\xe0\x78\x03\xc0'\
    b'\x70\x07\x00\xf8\x3e\x00\xff\xf8\x00\xff\xe0\x00\x7f\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x03\x80\x00\xfe\x00\x0f\x70\x00\x73\x80\x03\x8e'\
    b'\x00\x38\x70\x01\xc3\x80\x0e\x0e\x00\xe0\x70\x07\x03\xc0\x78\x0e'\
    b'\x03\x80\x70\x1c\x01\xc1\xc0\x0e\x0e\x00\x70\x70\x01\xc7\x00\x0e'\
    b'\x38\x00\x7b\xc0\x01\xdc\x00\x0e\xe0\x00\x7f\x00\x01\xf0\x00\x0f'\
    b'\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x0e\x00\x7c\x00\xee\x00\x7c\x00\xe7'\
    b'\x00\x7c\x01\xc7\x00\xee\x01\xc7\x00\xee\x01\xc7\x00\xee\x01\xc7'\
    b'\x01\xc7\x03\xc3\x81\xc7\x03\x83\x81\xc7\x03\x83\x81\xc7\x03\x83'\
    b'\x83\x83\x83\x81\xc3\x83\x87\x01\xc3\x83\x87\x01\xc7\x01\xc7\x01'\
    b'\xc7\x01\xc7\x00\xe7\x01\xcf\x00\xee\x00\xee\x00\xee\x00\xee\x00'\
    b'\xee\x00\xee\x00\xee\x00\xee\x00\x7c\x00\x7c\x00\x7c\x00\x7c\x00'\
    b'\x7c\x00\x7c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x3c\x00\x78\xf0\x07\x83\x80\x38\x0e\x03\x80\x78\x3c\x01'\
    b'\xe3\xc0\x07\x1c\x00\x1d\xc0\x00\xee\x00\x03\xe0\x00\x0e\x00\x00'\
    b'\xf8\x00\x07\xc0\x00\x77\x00\x07\xbc\x00\x38\xe0\x03\x83\x80\x3c'\
    b'\x1e\x03\xc0\x78\x1c\x01\xc1\xc0\x07\x1e\x00\x3d\xe0\x00\xf0\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x0e\x00\x07\xb8\x00\x78\xe0\x03\x87\x80\x3c\x1c\x03'\
    b'\xc0\x70\x1c\x03\xc1\xe0\x0f\x1e\x00\x38\xe0\x01\xef\x00\x07\x70'\
    b'\x00\x1f\x00\x00\xf8\x00\x03\x80\x00\x1c\x00\x00\xe0\x00\x07\x00'\
    b'\x00\x38\x00\x01\xc0\x00\x0e\x00\x00\x70\x00\x03\x80\x00\x1c\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x01\xff\xff\x1f\xff\xf1\xff\xff\x00\x00\xf0\x00'\
    b'\x1e\x00\x03\xc0\x00\x78\x00\x07\x00\x00\xe0\x00\x1c\x00\x03\xc0'\
    b'\x00\x78\x00\x0f\x00\x01\xe0\x00\x1c\x00\x03\x80\x00\x78\x00\x0f'\
    b'\x00\x01\xe0\x00\x3c\x00\x03\xff\xff\xbf\xff\xfb\xff\xff\x80\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x7e\x3f\x1f\x8e\x07\x03\x81\xc0\xe0\x70\x38\x1c\x0e\x07\x03'\
    b'\x81\xc0\xe0\x70\x38\x1c\x0e\x07\x03\x81\xc0\xe0\x70\x38\x1f\x8f'\
    b'\xc7\xe0\x00\x00\xc0\x30\x06\x01\x80\x60\x0c\x03\x00\xc0\x18\x06'\
    b'\x01\x80\x70\x0c\x03\x00\xc0\x18\x06\x01\x80\x30\x0c\x03\x00\xe0'\
    b'\x18\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\xe3\xf1\xf8\x1c\x0e'\
    b'\x07\x03\x81\xc0\xe0\x70\x38\x1c\x0e\x07\x03\x81\xc0\xe0\x70\x38'\
    b'\x1c\x0e\x07\x03\x81\xc0\xe0\x71\xf8\xfc\x7e\x00\x00\x00\x03\x00'\
    b'\x1e\x00\x78\x01\xe0\x0f\xc0\x33\x01\xce\x07\x38\x38\x70\xe1\xc3'\
    b'\x87\x1c\x0e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\xff\xff\xff\xff'\
    b'\xff\xff\xf8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x80\x78'\
    b'\x07\x00\x70\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x3f\x80\x7f\xf0\x7f\xf8\x78\x1e\x38\x07'\
    b'\x00\x03\x80\x07\xc0\x7f\xe0\xff\xf0\xff\x38\xf0\x1c\x70\x0e\x38'\
    b'\x0f\x1e\x1f\x87\xff\xc3\xfe\xe0\x7e\x38\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xe0\x00\x70\x00\x38'\
    b'\x00\x1c\x00\x0e\x00\x07\x00\x03\x9f\x01\xdf\xc0\xff\xf0\x7c\x3c'\
    b'\x3c\x0e\x1e\x03\x8e\x01\xc7\x00\xe3\x80\x71\xc0\x38\xe0\x1c\x70'\
    b'\x1e\x3c\x0e\x1f\x0f\x0f\xff\x07\x7f\x03\x9f\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x3c\x00\xff\x01\xff\x83\xc3'\
    b'\xc3\x81\xc7\x00\xe7\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00'\
    b'\xe3\x81\xe3\xc3\xc1\xff\xc0\xff\x80\x7e\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x70\x00\x38\x00'\
    b'\x1c\x00\x0e\x00\x07\x00\x03\x80\xf9\xc0\xfe\xe0\xff\xf0\xf0\xf8'\
    b'\x70\x3c\x70\x1e\x38\x07\x1c\x03\x8e\x01\xc7\x00\xe3\x80\x71\xe0'\
    b'\x38\x70\x3c\x3c\x3e\x0f\xff\x03\xfb\x80\xf9\xc0\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf8\x01\xff\x01\xff\xc1'\
    b'\xe0\xf0\xe0\x38\xe0\x0e\x70\x07\x3f\xff\x9f\xff\xce\x00\x07\x00'\
    b'\x03\xc0\x00\xe0\x1c\x7c\x3c\x1f\xfe\x07\xfe\x00\xfc\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x7c\x3f'\
    b'\x1f\xc7\x01\xc0\x70\x7f\x9f\xe7\xf8\x70\x1c\x07\x01\xc0\x70\x1c'\
    b'\x07\x01\xc0\x70\x1c\x07\x01\xc0\x70\x1c\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x0f\x9c\x0f\xfe\x0f\xff\x0f\x0f\x87\x03\xc7\x01\xe3\x80'\
    b'\x71\xc0\x38\xe0\x1c\x70\x0e\x38\x07\x1c\x07\x87\x03\xc3\xc3\xe0'\
    b'\xff\xf0\x3f\xf8\x0f\x9c\x00\x0e\x38\x0f\x1e\x0f\x07\xff\x83\xff'\
    b'\x80\x7f\x00\x00\x00\x00\x00\x1c\x00\x07\x00\x01\xc0\x00\x70\x00'\
    b'\x1c\x00\x07\x00\x01\xc7\xc0\x77\xfc\x1f\xff\x07\xc3\xe1\xe0\x78'\
    b'\x70\x0e\x1c\x03\x87\x00\xe1\xc0\x38\x70\x0e\x1c\x03\x87\x00\xe1'\
    b'\xc0\x38\x70\x0e\x1c\x03\x87\x00\xe1\xc0\x38\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x87\x0e\x00\x00'\
    b'\x00\xe1\xc3\x87\x0e\x1c\x38\x70\xe1\xc3\x87\x0e\x1c\x38\x70\xe0'\
    b'\x00\x00\x00\x00\x00\x00\x00\x70\x70\x70\x00\x00\x00\x70\x70\x70'\
    b'\x70\x70\x70\x70\x70\x70\x70\x70\x70\x70\x70\x70\x70\x70\x70\x70'\
    b'\x73\xf3\xe3\xc0\x00\x00\x00\xe0\x00\xe0\x00\xe0\x00\xe0\x00\xe0'\
    b'\x00\xe0\x00\xe0\x3c\xe0\x78\xe0\xf0\xe1\xe0\xe3\xc0\xe7\x80\xef'\
    b'\x00\xff\x00\xff\x80\xf3\x80\xe3\xc0\xe1\xe0\xe0\xe0\xe0\xf0\xe0'\
    b'\x70\xe0\x38\xe0\x3c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x01\xc3\x87\x0e\x1c\x38\x70\xe1\xc3\x87\x0e\x1c\x38'\
    b'\x70\xe1\xc3\x87\x0e\x1c\x38\x70\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x03\x8f\x03\xc0\x77\xf9\xfe\x0f\xff\x7f\xc1'\
    b'\xf0\xfc\x3c\x3c\x0f\x03\x87\x01\xc0\x70\xe0\x38\x0e\x1c\x07\x01'\
    b'\xc3\x80\xe0\x38\x70\x1c\x07\x0e\x03\x80\xe1\xc0\x70\x1c\x38\x0e'\
    b'\x03\x87\x01\xc0\x70\xe0\x38\x0e\x1c\x07\x01\xc3\x80\xe0\x38\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x0e\x7e\x03\xbf\xe0\xff\xf8\x3e\x0f\x0f'\
    b'\x01\xc3\x80\x70\xe0\x1c\x38\x07\x0e\x01\xc3\x80\x70\xe0\x1c\x38'\
    b'\x07\x0e\x01\xc3\x80\x70\xe0\x1c\x38\x07\x0e\x01\xc0\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\xf0\x03\xfe\x03'\
    b'\xff\x83\xc1\xe1\xc0\x71\xe0\x3c\xe0\x0e\x70\x07\x38\x03\x9c\x01'\
    b'\xce\x00\xe7\x80\xf1\xc0\x70\xf0\x78\x3f\xf8\x0f\xf8\x01\xf0\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x39\xf0\x1d'\
    b'\xfc\x0f\xff\x07\xc3\xc3\xc0\xe1\xe0\x78\xe0\x1c\x70\x0e\x38\x07'\
    b'\x1c\x03\x8e\x01\xc7\x01\xe3\xc0\xe1\xf0\xf0\xff\xf0\x77\xf0\x39'\
    b'\xf0\x1c\x00\x0e\x00\x07\x00\x03\x80\x01\xc0\x00\xe0\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f'\
    b'\x9c\x1f\xee\x0f\xff\x0f\x0f\x87\x03\xc7\x01\xe3\x80\x71\xc0\x38'\
    b'\xe0\x1c\x70\x0e\x38\x07\x1e\x03\x87\x03\xc3\xc3\xe0\xff\xf0\x3f'\
    b'\xb8\x0f\x9c\x00\x0e\x00\x07\x00\x03\x80\x01\xc0\x00\xe0\x00\x70'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x9e\x77\xcf\xf1'\
    b'\xf0\x3c\x07\x00\xe0\x1c\x03\x80\x70\x0e\x01\xc0\x38\x07\x00\xe0'\
    b'\x1c\x03\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfc\x01\xff\x03\xff'\
    b'\x87\x83\xc7\x01\xc7\x80\x07\xf0\x03\xfe\x01\xff\x80\x3f\xc0\x03'\
    b'\xe7\x00\xe7\x80\xe3\xc1\xe3\xff\xc1\xff\x80\x7e\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x40\x60\x70\x38'\
    b'\x1c\x0e\x1f\xef\xf7\xf8\xe0\x70\x38\x1c\x0e\x07\x03\x81\xc0\xe0'\
    b'\x70\x38\x1f\x8f\xc3\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1c\x03\x87'\
    b'\x00\xe1\xc0\x38\x70\x0e\x1c\x03\x87\x00\xe1\xc0\x38\x70\x0e\x1c'\
    b'\x03\x87\x00\xe1\xc0\x38\x70\x0e\x1e\x07\x87\xc3\xe0\xff\xb8\x3f'\
    b'\xee\x03\xe3\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x38\x03\xb8\x0e\x70\x1c\xe0\x38\xe0\xe1\xc1\xc3\x83\x83\x8e\x07'\
    b'\x1c\x0e\x38\x0e\xe0\x1d\xc0\x1b\x00\x36\x00\x7c\x00\x70\x00\xe0'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x38\x0e\x03\x9c\x07\x01\xce\x07\xc0\xe3\x83\xe0\xe1'\
    b'\xc1\xb0\x70\xe0\xd8\x38\x38\xee\x38\x1c\x63\x1c\x0e\x31\x8e\x03'\
    b'\x18\xce\x01\xdc\x77\x00\xec\x1b\x80\x36\x0d\x80\x1f\x07\xc0\x0f'\
    b'\x83\xe0\x03\x80\xe0\x01\xc0\x70\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1c\x03\xb8\x1c\x70\xe1'\
    b'\xc3\x83\x9c\x07\xe0\x1f\x80\x3c\x00\xf0\x03\xc0\x1f\x80\x7e\x03'\
    b'\x9c\x1c\x38\x70\xe3\x81\xdc\x03\x80\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x0e\x00\xee\x03\xdc\x07\x38\x0e\x38\x38\x70\x70\xe0\xe0\xe3'\
    b'\x81\xc7\x01\x8e\x03\xb8\x07\x70\x06\xe0\x0f\x80\x1f\x00\x1e\x00'\
    b'\x38\x00\x70\x01\xc0\x03\x80\x3f\x00\x7c\x00\xf0\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\xff\xe7\xff\xcf'\
    b'\xff\x80\x0f\x00\x3c\x00\xf0\x03\xc0\x0f\x00\x3c\x00\xf0\x03\xc0'\
    b'\x0f\x00\x3c\x00\xf0\x01\xff\xfb\xff\xf7\xff\xe0\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00'

WIDTHS = memoryview(_WIDTHS)
OFFSETS = memoryview(_OFFSETS)
BITMAPS = memoryview(_BITMAPS)