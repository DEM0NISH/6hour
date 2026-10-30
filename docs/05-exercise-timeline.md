# Exercise timeline


| Time | Event | Decision | Owner | Evidence produced |
|---|---|---|---|---|
| T+0:00 | Outbound-volume alert | Validate and page on-call | SOC | Alert record, acknowledgement |
| T+0:15 | External send confirmed | Preserve mail and agent traces | SOC / platform | Headers, audit event, export metadata |
| T+0:30 | Triage and severity | Assign Sev1–Sev4 and AI tags | Incident Commander | Severity rationale |
| T+1:00 | Incident declared | Name leads and establish bridge | Incident Commander | Declaration and roster |
| T+1:30 | Containment | Revoke tokens, suspend agent, block address, preserve logs | Platform / SOC | Revocation IDs, config snapshot |
| T+2:00 | Scope initial export | Determine fields, counts, recipients, time range | SOC / platform | Query notes, hashes, scope estimate |
| T+3:00 | Contact client | Send factual holding statement or explain bounded uncertainty | Client delivery / Legal | Copy of client notice and delivery proof |
| T+4:00 | Qualification | Decide CERT-In and DPDP pathways | Legal / Incident Commander | Decision log with reasons |
| T+5:00 | Filing preparation | Assemble available facts and gaps | SOC / Legal | Draft, evidence index |
| T+6:00 | CERT-In target | Submit if applicable; track supplement | Designated contact | Submission receipt / rationale |
| T+6 onward | DPDP support | Support Fiduciary-led Board duties | Meridian / Northwind | Fact pack, action updates |
| T+24:00 | Contract checkpoint and individual notice decision | Confirm client notified; Northwind decides individual notice | Client delivery / Northwind | Notice copy, rationale |
| T+48:00 | Refined facts | Update affected cohort and mitigations | SOC / Northwind | Versioned facts pack |
| T+72:00 | Detailed report target | Fiduciary submits report or documents written extension | Northwind | Board submission / extension record |
| T+7 days | Post-incident review | Approve corrective actions | Incident Commander | Review and action register |

| Inject | Delivery time | New information / prompt |
|---|---|---|
| 1 | T+1:15 | Free-mail provider confirms receipt; no assurance of deletion |
| 2 | T+2:30 | A second, smaller file was sent at 02:22 |
| 3 | T+3:30 | Northwind CISO calls Meridian CEO directly |
| 4 | T+4:30 | Journalist emails a screenshot of a customer row |
| 5 | T+6:30 | Contract requires 24-hour notice; it has not been sent |
| 6 | T+30:00 | Export includes records of minors |

```mermaid
timeline
 title 6-Hour Clock Exercise
 02:40 T+0 Alert noticed
 02:55 T+0:15 External send confirmed
 03:10 T+0:30 Triage and severity
 03:40 T+1 Declare incident
 04:10 T+1:30 Contain and preserve
 04:40 T+2 Scope first export
 05:40 T+3 Contact client
 06:40 T+4 Qualification decisions
 07:40 T+5 Filing preparation
 08:40 T+6 CERT-In target
 Next day 02:40 T+24 Contract and individual notice decision
 T+48 Refined facts
 T+72 Board report target
 T+7 days Review
```
