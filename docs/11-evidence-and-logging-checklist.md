# Evidence and logging checklist


| Evidence | Handling notes | ISO mapping |
|---|---|---|
| Alert record | Preserve original event, rule, delivery and acknowledgement times | 5.28 |
| Agent config / permission manifest | Snapshot tool scopes, model/config version, owner and policy | 5.28 |
| Mailbox audit logs and headers | Preserve originals and message IDs; restrict access | 5.28 |
| CRM access logs | Record query, object count, principal and timestamp | 5.28 |
| Token issue / revocation records | Preserve IDs, time, actor, outcome; avoid logging secrets | 5.28 |
| Screenshots | Include capture time and source; retain original files | 5.28 |
| Decision log | Keep decisions, rationale, approvers and time | 5.28 |
| Messages sent | Keep exact copies, recipients, channel and delivery status | 5.28 |

Retain logs under applicable policy and legal requirements; the CERT-In Directions specify a rolling 180-day requirement for covered entities. Preserve chain of custody and do not alter originals.
