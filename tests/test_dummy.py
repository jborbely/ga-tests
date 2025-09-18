import socket
import subprocess

MDNS_ADDR = "224.0.0.251"
MDNS_PORT = 5353


def test() -> None:
    ps = subprocess.Popen("ifconfig", stdout=subprocess.PIPE)  # noqa: S607
    output = subprocess.check_output(("grep", "inet "), stdin=ps.stdout)
    _ = ps.wait()

    addresses = {line.split()[1] for line in output.decode().splitlines()}
    addresses.discard("127.0.0.1")
    assert len(addresses) == 1
    for address in addresses:
        assert address.startswith("192")

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_LOOP, 1)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 255)
    sock.bind((addresses.pop(), 0))
    _ = sock.sendto(b"hi", (MDNS_ADDR, MDNS_PORT))
    sock.close()
