import base64

# CONVERSION FUNCTIONS

def _chunks(string, chunk_size):
    for i in range(0, len(string), chunk_size):
        yield string[i:i+chunk_size]

def _hex(x):
    return format(x, '02x')

def hex_2_bin(data):
    return ''.join(f'{int(x, 16):08b}' for x in _chunks(data, 2))

def str_2_bin(data):
    return ''.join(f'{ord(c):08b}' for c in data)

def bin_2_hex(data):
    return ''.join(f'{int(b, 2):02x}' for b in _chunks(data, 8))

def str_2_hex(data):
    return ''.join(f'{ord(c):02x}' for c in data)

def bin_2_str(data):
    return ''.join(chr(int(b, 2)) for b in _chunks(data, 8))

def hex_2_str(data):
    return ''.join(chr(int(x, 16)) for x in _chunks(data, 2))

# XOR FUNCTIONS

def strxor(a, b):  # xor two strings, trims the longer input
    return ''.join(chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b))

def bitxor(a, b):  # xor two bit-strings, trims the longer input
    return ''.join(str(int(x) ^ int(y)) for (x, y) in zip(a, b))

def hexxor(a, b):  # xor two hex-strings, trims the longer input
    return ''.join(_hex(int(x, 16) ^ int(y, 16)) for (x, y) in zip(_chunks(a, 2), _chunks(b, 2)))

# BASE64 FUNCTIONS

def b64decode(data):
    return bytes_to_string(base64.b64decode(string_to_bytes(data)))

def b64encode(data):
    return bytes_to_string(base64.b64encode(string_to_bytes(data)))

# PYTHON3 'BYTES' FUNCTIONS

def bytes_to_string(bytes_data):
    return bytes_data.decode()  # default utf-8

def string_to_bytes(string_data):
    return string_data.encode()  # default utf-8