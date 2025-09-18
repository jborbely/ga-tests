import subprocess

def test() -> None:
    ps = subprocess.Popen("ifconfig", stdout=subprocess.PIPE)  # noqa: S607
    output = subprocess.check_output(("grep", "inet "), stdin=ps.stdout)
    _ = ps.wait()
    addresses = {line.split()[1] for line in output.decode().splitlines()}
    assert addresses == {"127.0.0.1"}
