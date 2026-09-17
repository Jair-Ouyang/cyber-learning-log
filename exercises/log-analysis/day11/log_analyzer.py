import json
import sys


log_file = "exercises/log-analysis/day11/sample_auth.jsonl"
try:
    alert_threshold = int(sys.argv[1]) if len(sys.argv) > 1 else 3
except ValueError:
    print("[ERROR] Alert threshold must be an integer")
    sys.exit(2)

if alert_threshold < 1:
    print("[ERROR] Alert threshold must be at least 1")
    sys.exit(2)

total_events = 0
successful_logins = 0
failed_logins = 0
failed_by_ip = {}
invalid_lines = 0

with open(log_file, "r", encoding="utf-8") as file:
    for line_number, line in enumerate(file, start=1):
        try:
            event_data = json.loads(line)
        except json.JSONDecodeError as error:
            invalid_lines += 1
            print(f"[WARN] Line {line_number} skipped: {error.msg}")
            continue

        total_events += 1

        if event_data["event"] == "login_success":
            successful_logins += 1

        elif event_data["event"] == "login_failed":
            failed_logins += 1
            source_ip = event_data["source_ip"]
            failed_by_ip[source_ip] = failed_by_ip.get(source_ip, 0) + 1

print("=== Authentication Log Summary ===")
print("Total events:", total_events)
print("Successful logins:", successful_logins)
print("Failed logins:", failed_logins)
print("Invalid lines skipped:", invalid_lines)

print("\n=== Failed Logins by Source IP ===")

for source_ip, count in failed_by_ip.items():
    print(source_ip, ":", count)

print("\n=== Alerts ===")

alerts = []

for source_ip, count in failed_by_ip.items():
    if count >= alert_threshold:
        alerts.append(
            {
                "source_ip": source_ip,
                "failed_logins": count,
            }
        )
        print(f"[ALERT] {source_ip} generated {count} failed login attempts")

if not alerts:
    print("[OK] No source IP reached the alert threshold")

report = {
    "total_events": total_events,
    "successful_logins": successful_logins,
    "failed_logins": failed_logins,
    "invalid_lines_skipped": invalid_lines,
    "failed_by_ip": failed_by_ip,
    "alert_threshold": alert_threshold,
    "alerts": alerts,
}

report_file = "exercises/log-analysis/day11/analysis_report.json"

with open(report_file, "w", encoding="utf-8") as file:
    json.dump(report, file, indent=2)

print("\nReport written to:", report_file)
