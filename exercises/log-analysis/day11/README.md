# Day 11 - Structured Security Log Analysis

## Objective

Build a Python program that reads structured authentication logs, summarizes login activity, detects repeated failures, handles malformed data, and writes a machine-readable JSON report.

## Files

- `sample_auth.jsonl` - synthetic authentication events in JSON Lines format
- `log_analyzer.py` - Python log analysis program
- `analysis_report.json` - structured analysis result

## Log Format

Each line in `sample_auth.jsonl` represents one independent event:

```json
{"timestamp":"2026-09-17T09:01:05+10:00","event":"login_failed","username":"admin","source_ip":"198.51.100.23"}
```

The fields are:

- `timestamp` - when the event occurred
- `event` - whether the login succeeded or failed
- `username` - the account used in the attempt
- `source_ip` - the source address of the request

The final line is intentionally malformed so that error handling can be tested.

## Usage

Run the analyzer with the default alert threshold of 3:

```bash
python3 exercises/log-analysis/day11/log_analyzer.py
```

Run it with a custom threshold:

```bash
python3 exercises/log-analysis/day11/log_analyzer.py 5
```

The threshold must be a positive integer.

## Verified Results

The synthetic dataset produced:

- 8 valid authentication events
- 3 successful logins
- 5 failed logins
- 1 malformed line skipped
- 4 failures from `198.51.100.23`
- 1 failure from `203.0.113.44`

With the default threshold of 3, `198.51.100.23` generated an alert.

## Error Handling

- Non-integer thresholds return exit status 2.
- Thresholds below 1 return exit status 2.
- Malformed JSON lines produce a warning and are skipped.
- Valid events continue to be processed after a malformed line.

## Structured Report

The program writes its results to:

```text
exercises/log-analysis/day11/analysis_report.json
```

The report contains totals, failed-login counts by source IP, the selected threshold, and generated alerts.

The report can be validated with:

```bash
python3 -m json.tool exercises/log-analysis/day11/analysis_report.json
```

## Security Interpretation

Repeated login failures are a signal for investigation, not proof of an attack. Possible explanations include:

- incorrect passwords
- outdated saved credentials
- automated scanners
- password spraying
- brute-force attempts

An analyst would need additional context before classifying the activity as an incident.

## Security Scope

All events and IP addresses in this exercise are synthetic. No real accounts, devices, networks, or external systems were accessed or scanned.
