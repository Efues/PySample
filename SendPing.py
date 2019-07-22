import subprocess

def is_connectable(host):
    ping = subprocess.Popen(
        ["ping", "-c", "1", host],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE)
    ping.communicate()
    return ping.returncode == 0

result = is_connectable('192.168.1.20')
print(result)