import socket
from datetime import datetime

print("=" * 50)
print("        SIMPLE PORT SCANNER")
print("=" * 50)

# Take target input
target = input("Enter Target IP or Website: ")

# Convert website name to IP
try:
    target_ip = socket.gethostbyname(target)
except socket.gaierror:
    print("[-] Invalid target")
    exit()

# Port range input
start_port = int(input("Enter Start Port: "))
end_port = int(input("Enter End Port: "))

print(f"\n[+] Scanning Target: {target_ip}")
print(f"[+] Scanning Ports: {start_port} to {end_port}")
print(f"[+] Scan Started At: {datetime.now()}\n")

# Timeout setting
socket.setdefaulttimeout(1)

try:
    # Loop through ports
    for port in range(start_port, end_port + 1):

        scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        result = scanner.connect_ex((target_ip, port))

        if result == 0:
            print(f"[OPEN] Port {port}")
    
        scanner.close()

except KeyboardInterrupt:
    print("\n[-] Scan interrupted by user")

except socket.error:
    print("\n[-] Server not responding")

print(f"\n[+] Scan Completed At: {datetime.now()}")