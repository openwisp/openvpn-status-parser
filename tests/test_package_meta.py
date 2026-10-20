from pytest import raises

import openvpn_status


def test_version():
    assert openvpn_status.__version__ == "0.3.0"


def test_shortcut():
    with raises(openvpn_status.ParsingError):
        openvpn_status.parse_status("")
    with raises(openvpn_status.ParsingError):
        openvpn_status.parse_status(b"")
