import socket
import urllib.error
import urllib.request
import sys


target = sys.argv[1] if len(sys.argv) > 1 else "example.com"
url = f"https://{target}"
dns_passed = False
https_passed = False

print("=== Connectivity Check ===")

try:
    ip_address = socket.gethostbyname(target)
    dns_passed = True
    print("[PASS] DNS resolution succeeded")
    print("Target:", target)
    print("IPv4 address:", ip_address)
except socket.gaierror as error:
    print("[FAIL] DNS resolution failed")
    print("Reason:", error)

if dns_passed:
    try:
        with urllib.request.urlopen(url, timeout=10) as response:
            status_code = response.status

        if 200 <= status_code < 400:
            https_passed = True
            print("[PASS] HTTPS connection succeeded")
            print("HTTP status:", status_code)
        else:
            print("[WARN] HTTPS returned an unexpected status")
            print("HTTP status:", status_code)
    except (urllib.error.URLError, TimeoutError) as error:
        print("[FAIL] HTTPS connection failed")
        print("Reason:", error)
else:
    print("[SKIP] HTTPS check skipped because DNS failed")

sys.exit(0 if dns_passed and https_passed else 1)
