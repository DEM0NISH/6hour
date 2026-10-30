"""Calculate incident exercise deadlines from a local noticed time."""

from __future__ import annotations

import argparse
from datetime import datetime, timedelta
from typing import Iterable


def deadlines(noticed: datetime, contract_hours: float = 24) -> list[tuple[str, datetime]]:
    """Return the exercise deadlines, preserving the input's local-time basis."""
    return [
        ("CERT-In report / decision (6 hours)", noticed + timedelta(hours=6)),
        (f"Contract notice ({contract_hours:g} hours)", noticed + timedelta(hours=contract_hours)),
        ("DPDP detailed report target (72 hours)", noticed + timedelta(hours=72)),
        ("Affected individual notice: without delay (decision target)", noticed + timedelta(hours=24)),
        ("Post-incident review (7 days)", noticed + timedelta(days=7)),
    ]


def format_table(rows: Iterable[tuple[str, datetime]], now: datetime) -> str:
    """Render a plain-text deadline table and flag past targets."""
    lines = [f"{'Deadline':58} {'Local deadline':20} Status", "-" * 91]
    for label, due in rows:
        status = "PAST — review immediately" if due < now else "upcoming"
        lines.append(f"{label:58} {due.strftime('%Y-%m-%d %H:%M %Z').strip():20} {status}")
    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--noticed", required=True, help='Local date and time, for example "2026-11-07 02:40"')
    parser.add_argument("--contract-hours", type=float, default=24, help="Example contract notice period in hours (default: 24)")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    try:
        noticed = datetime.strptime(args.noticed, "%Y-%m-%d %H:%M")
    except ValueError as exc:
        raise SystemExit("--noticed must use YYYY-MM-DD HH:MM in local time") from exc
    if args.contract_hours <= 0:
        raise SystemExit("--contract-hours must be greater than zero")
    print(f"Incident noticed: {noticed:%Y-%m-%d %H:%M} local time")
    print(format_table(deadlines(noticed, args.contract_hours), datetime.now()))
    print("Note: individual notice has no fixed hour count here; +24h is a decision checkpoint only.")
    print("Legal deadlines are simplified exercise prompts. Verify against current official text.")


if __name__ == "__main__":
    main()
