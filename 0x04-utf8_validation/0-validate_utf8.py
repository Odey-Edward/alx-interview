#!/usr/bin/python3
"""validUTF8 method module"""


def validUTF8(data):
    """method that determines if a given data set
    represents a valid UTF-8 encoding."""

    # Variable to keep track of the number of remaining
    # bytes to read for a character
    remaining_bytes = 0

    # Iterate through each byte in the data
    for byte in data:
        # Check if this byte is a continuation byte
        if remaining_bytes:
            # If it's not of the form 10xxxxxx, then it's an
            # invalid continuation byte
            if byte >> 6 != 0b10:
                return False
            remaining_bytes -= 1
        else:
            # If the byte starts with 0, it's a single-byte character
            if byte >> 7 == 0:
                continue
            # Count the number of leading 1s to determine the
            # number of bytes in this character
            elif byte >> 3 == 0b11110:
                remaining_bytes = 3
            elif byte >> 4 == 0b1110:
                remaining_bytes = 2
            elif byte >> 5 == 0b110:
                remaining_bytes = 1
            else:
                # Invalid starting byte
                return False

    # If there are remaining bytes to be read after iterating through
    # all data, it's invalid
    if remaining_bytes:
        return False

    if not data:
        return False

    # If everything passes, it's a valid UTF-8 encoding
    return True
