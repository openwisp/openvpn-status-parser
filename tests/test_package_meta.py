from pytest import raises

import openvpn_status
from openvpn_status.version import VERSION


def test_version():
    assert VERSION == (0, 3, 0, "final")
    assert openvpn_status.__version__ == "0.3.0"


def test_shortcut():
    with raises(openvpn_status.ParsingError):
        openvpn_status.parse_status("")
    with raises(openvpn_status.ParsingError):
        openvpn_status.parse_status(b"")
