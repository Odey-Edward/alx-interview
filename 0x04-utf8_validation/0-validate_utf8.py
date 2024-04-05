#!/usr/bin/python3
"""validUTF8 method module"""


def validUTF8(data):
    """method that determines if a given data set
    represents a valid UTF-8 encoding."""
    remaining_bytes = 0

    for byte in data:
        byte_value = byte & 0xFF

        if remaining_bytes:
            if byte_value >> 6 != 0b10:
                return False
            remaining_bytes -= 1
        else:
            if byte_value >> 3 == 0b11110:
                remaining_bytes = 3
            elif byte_value >> 4 == 0b1110:
                remaining_bytes = 2
            elif byte_value >> 5 == 0b110:
                remaining_bytes = 1
            elif byte_value >> 7 != 0:
                return False

    if remaining_bytes:
        return False

    return True
