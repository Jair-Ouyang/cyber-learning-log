import subprocess


def run_command(command):
    result = subprocess.run(
        command,
        capture_output=True,
        text=True,
        check=True,
    )
    return result.stdout.strip()


print("=== Network Interfaces ===")
print(run_command(["ip", "-brief", "address"]))

print("\n=== Routes ===")
print(run_command(["ip", "route"]))

print("\n=== Listening Ports ===")
print(run_command(["ss", "-tuln"]))
