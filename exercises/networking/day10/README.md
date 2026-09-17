# Day 10 - Python Connectivity Check

## Objective

Build a Python program that checks DNS resolution and HTTPS connectivity, reports clear results, and returns an exit status for automation.

## Concepts Practised

- Resolve a domain name to an IPv4 address with `socket.gethostbyname()`.
- Make an HTTPS request with `urllib.request.urlopen()`.
- Limit the HTTPS request with a 10-second timeout.
- Handle network errors with `try` and `except`.
- Read a target domain from `sys.argv`.
- Return a machine-readable exit status with `sys.exit()`.

## Usage

Use the default target, `example.com`:

```bash
python3 exercises/networking/day10/connectivity_check.py
```

Check a specified target:

```bash
python3 exercises/networking/day10/connectivity_check.py example.com
```

Check the exit status immediately after running the program:

```bash
echo $?
```

## Verified Results

| Target | DNS | HTTPS | Exit status |
|---|---|---|---:|
| `example.com` | PASS | PASS, HTTP 200 | 0 |
| `does-not-exist.invalid` | FAIL | SKIPPED | 1 |

An exit status of `0` means the complete check succeeded. A non-zero exit status means that at least one required check failed.

## Troubleshooting

A `TabError` occurred because tabs and spaces were mixed in one Python indentation block. The affected line was corrected to use spaces consistently.

Entering `example.com` as a separate shell command returned exit status `127`, which means the shell could not find such a command. The domain must be supplied on the same line as the Python command.

## Security Relevance

Connectivity checks help distinguish DNS failures from HTTPS failures. Clear output and meaningful exit statuses allow monitoring tools and scripts to detect and report network problems automatically.

This exercise only tested a normal HTTPS connection to a designated example domain. It did not scan external systems.
