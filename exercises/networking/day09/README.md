# Day 09 - Linux Network Baseline

## Objective

Inspect the Ubuntu WSL network configuration, routes, connectivity, and listening ports. Automate the collection with Python.

## Commands Practised

- `ip -brief address`
- `ip route`
- `ping -c 4`
- `getent hosts`
- `curl -I`
- `ss -tuln`
- `sudo ss -tulnp`

## Observations

- Ubuntu WSL uses the `eth0` virtual network interface.
- The observed private IPv4 address was `172.17.12.118/20`.
- The observed default gateway was `172.17.0.1`.
- Port 53 belonged to `systemd-resolved` and provided DNS services.
- Port 323 belonged to `chronyd` and supported time synchronization.
- No obviously unexpected public listening service was observed.

## Troubleshooting

The WSL gateway did not reply to ICMP ping requests. However, DNS resolution succeeded and an HTTPS request returned HTTP status 200.

This demonstrates that a failed ping does not always mean the network is unavailable.

## Python Automation

Run the network checker with:

`python3 exercises/networking/day09/network_check.py`

The script uses Python's `subprocess` module to collect network interfaces, routes, and listening ports.

## Security Relevance

A network baseline helps identify unexpected interfaces, routes, and listening services. Observed IP addresses and process IDs may change after restarting the system.
