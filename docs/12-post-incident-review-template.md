# Post-incident review template


| Field | Entry |
|---|---|
| Summary | What happened, impact, and current status |
| Actual vs expected timeline | Event time, detection, awareness, containment, notices, filings |
| Five whys | Why did each control fail? Follow systemic causes, not blame |
| What went well | Evidence-based practices to retain |
| What surprised us | Gaps in assumptions, observability, or ownership |
| What will change | Prioritised, measurable improvements |

| Gap | Control | Fix | Owner | Due | Status |
|---|---|---|---|---|---|
| Broad CRM access | 5.15, 5.18, 8.2, 8.3 | Reduce scopes; review access quarterly | Platform lead | 30 days | Open |
| No agent owner/expiry | 5.16, 5.18 | Named owner, expiry, recertification workflow | Platform lead | 30 days | Open |
| Unrestricted egress | 8.12 | Recipient allow-list and attachment inspection | Security engineering | 45 days | Open |
| Prompt injection trust boundary | 8.26, 8.28 | Treat inbound content as untrusted; test controls | AI engineering | 45 days | Open |
| Detection / paging gap | 8.15, 8.16 | Tune alerts and test on-call page | SOC lead | 21 days | Open |
| No agent runbook | 5.24 | Publish and exercise response runbook | Incident Commander | 21 days | Open |
| Contract ambiguity | 5.19, 5.20 | Inventory notice periods and escalation contacts | Client delivery | 30 days | Open |
