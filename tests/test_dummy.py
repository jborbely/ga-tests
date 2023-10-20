import socket
import subprocess
import sys

#from msl.equipment import utils


def ipv4_addresses_2():
    """Get the IPv4 addresses of the computer.

    Returns
    -------
    :class:`set` of :class:`str`
        All IPv4 addresses on all network interfaces.
    """
    if sys.platform == 'linux':
        out = subprocess.check_output(['hostname', '--all-ip-addresses'])
        addresses = set(out.decode().split())
    else:
        interfaces = socket.getaddrinfo(socket.gethostname(), None, socket.AF_INET)
        addresses = set(ip[-1][0] for ip in interfaces)
    addresses.discard('127.0.0.1')
    return addresses


def test_ipv4_addresses_2():
    addresses = ipv4_addresses_2()
    print()
    for a in addresses:
        print(a)
    assert addresses


# def test_ipv4_addresses():
#     addresses = utils.ipv4_addresses()
#     print()
#     for a in addresses:
#         print(a)
#     assert addresses
