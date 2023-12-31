"""
Tests for the ipstack_to_coords tool
"""
# pylint: disable=missing-function-docstring


import subprocess


def test_default():
    result = subprocess.run(["./ipstack_to_coords.py"], stdout=subprocess.PIPE, check=False)
    expected = b"lat:40.5369987487793,long:-82.12859344482422\n"
    assert result.stdout == expected, f"Expected:{expected}\nActual:{result.stdout}"
