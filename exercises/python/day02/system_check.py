import getpass
import os
import platform

user = getpass.getuser()
hostname = platform.node()
operating_system = platform.system()
python_version = platform.python_version()
architecture = platform.machine()
current_directory = os.getcwd()

print("=== System Check ===")
print("User:", user)
print("Hostname:", hostname)
print("Operating system:", operating_system)
print("Python version:", python_version)
print("Architecture:",architecture)
print("Current directory:", current_directory)
