import socket
import subprocess
import sys


def ipv4_addresses():
    """Get the IPv4 addresses of the computer.

    Returns
    -------
    :class:`set` of :class:`str`
        All IPv4 addresses on all network interfaces.
    """
    if sys.platform.startswith('linux'):
        p = subprocess.Popen(['hostname', '--all-ip-addresses'], stdout=subprocess.PIPE)
        stdout, _ = p.communicate()
        addresses = set(stdout.decode().split())
    else:
        interfaces = socket.getaddrinfo(socket.gethostname(), None, socket.AF_INET)
        addresses = set(ip[-1][0] for ip in interfaces)
    addresses.discard('127.0.0.1')
    return addresses


def test_ipv4_addresses():
    addresses = ipv4_addresses()
    for a in addresses:
        print(a)
    assert addresses
