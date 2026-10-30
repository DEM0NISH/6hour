# The 6-Hour Clock: AI Agent Breach Tabletop Exercise

A complete, fictional tabletop exercise and offline web simulator for practicing a data breach response when an autonomous AI agent sends customer records outside an approved workflow. It combines a facilitator-ready documentation pack, timed decisions and injects, mock evidence, and a standard-library Python deadline calculator.

## Why it matters

AI agents can hold standing credentials, use tools, and act while a team is offline. A prompt injection can turn that access into an incident before people see an alert. Teams need to practice containment, evidence preservation, contractual communication, and overlapping reporting clocks with clear human ownership.

**Byline:** [Your name]
**All organisations, people, email addresses, events, and evidence are fictional.** This is an educational rehearsal, not legal advice. Legal statements should be verified against current official text before use.

## Screenshots

Capture the landing page, live exercise dashboard, and final score screen after running `app/index.html`. Store approved screenshots in `assets/` and replace this sentence with Markdown image links.

## Quick start

1. Open `app/index.html` directly in a modern browser. The app works offline and saves no data to a server.
2. Choose a role, select a clock speed, and select **Start incident**.
3. Set up the Python environment on Windows with `powershell -ExecutionPolicy Bypass -File tools/setup.ps1` (or follow the manual setup in [`tools/README.md`](tools/README.md)).
4. For deadlines, run `python tools/clock_simulator.py --noticed "2026-11-07 02:40" --contract-hours 24`.
5. Run checks with `python -m unittest discover -s tools -p "test_*.py"`.

## Repository map

| Path | Contents |
|---|---|
| `docs/` | Complete exercise package, split sections, diagrams, and combined document |
| `app/index.html` | Single-file, vanilla HTML/CSS/JS interactive exercise |
| `tools/clock_simulator.py` | Local deadline calculator |
| `tools/test_clock_simulator.py` | Three standard-library unit tests |
| `evidence/` | Invented sample alert, permissions, audit trail, and decision log |
| `assets/` | Mermaid source diagrams |

## The clocks

| Clock | Exercise target | Owner / note |
|---|---|---|
| CERT-In | 6 hours from noticing a qualifying incident | Confirm applicability and report available facts; the official direction lists data breaches and data leaks. |
| Contract | 24 hours (example only) | Meridian AI informs Northwind Retail under the fictional contract. |
| DPDP Board | Initial intimation without delay; detailed report within 72 hours under Rule 7 | Northwind Retail, as Data Fiduciary, owns the statutory duty; Meridian supports. |
| Affected people | Without delay, clear and useful information | No fixed number of hours stated in this exercise. |
| Logs | 180 days under CERT-In directions, subject to scope | Preserve and validate applicability and jurisdiction. |

## Framework mapping

| Failure or practice | ISO/IEC 27001:2022 Annex A controls |
|---|---|
| Access, permissions, agent identity | 5.15, 5.16, 5.18, 8.2, 8.3 |
| Egress and data loss prevention | 8.12 |
| Secure agent design and instruction handling | 8.26, 8.28 |
| Monitoring and detection | 8.15, 8.16 |
| Incident readiness and evidence | 5.24, 5.28 |
| Supplier and contract relationships | 5.19, 5.20 |
| Continuity and ICT readiness | 5.29, 5.30 |

## Assumptions and limitations

The organisations and evidence are fictional. The 24-hour contract notice and downtime values are exercise assumptions, not universal requirements. The scenario is discussion-based, the legal clocks are simplified prompts, and the team must confirm current official text, applicable scope, contract language, and professional advice before relying on any decision.

## What I would do next

Create a one-page on-call checklist, run the exercise with a real team, repeat it every six months, and govern agent access with named owners, expiry, least privilege, and access recertification.

## Publish on GitHub Pages

With GitHub CLI (`gh`) authenticated, run these commands from this project directory:

```powershell
gh repo create <OWNER>/<REPO> --public --source . --remote origin --push
gh api repos/<OWNER>/<REPO>/pages -X POST -F 'source[branch]=main' -F 'source[path]=/'
```

The second command enables Pages from the repository root. The app is at `https://<OWNER>.github.io/<REPO>/app/` (a user site uses `https://<OWNER>.github.io/app/`). No build step is needed. Alternatively, copy `app/index.html` to `/docs/index.html`, then set `source[path]` to `/docs` in the Pages API command. Pages availability and repository visibility depend on GitHub account settings.

## Licence

MIT. See [LICENSE](LICENSE).

