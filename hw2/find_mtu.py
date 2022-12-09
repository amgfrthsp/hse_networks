import ipaddress
import platform
import socket
import subprocess
import sys 

def check_mtu(mtu, host):
    print("searching...")
    cur_os = platform.system().lower()
    command = ""
    if cur_os == "darwin": #macos
        command = f"ping -D -s {mtu} -c 1 {host}"
    elif cur_os == "linux":
        command = f"ping -M do -s {mtu} -c 1 {host}"
    elif cur_os == "windows":
        command = f"ping -M do -s {mtu} -n 1 {host}"

    try:
        out = subprocess.Popen(command,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT,
                                shell=True)
    except Exception:
        raise Exception("Host you provided is invalid or does not exist")

    for line in iter(out.stdout.readline, b''):
        l = line.decode(encoding='utf-8').lower()
        if "message too long" in l or "100.0% packet loss" in l or 'packet size too large' in l:
            return False
    return True

def find_mtu(host):
    # check for existance and availability
    try:
        ipaddress.IPv4Address(socket.gethostbyname(host))
    except Exception:
        raise Exception("Host you provided is invalid or does not exist")
    
    l = 1200
    r = 10000
    while (r - l - 1 > 0):
        mtu_to_check = int((l + r) / 2)
        if check_mtu(mtu_to_check, host):
            l = mtu_to_check
        else:
            r = mtu_to_check
    return l + 28

if __name__ == '__main__':
    args = sys.argv[1:]
    if len(args) != 1:
        raise Exception("Wrong number of arguments. Provide one hostname")
    print(f"The maximum MTU size for this IP including header size: {find_mtu(args[0])}")