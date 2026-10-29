# S01: Leaked API key in a public repository

**Time box:** 45 minutes  |  **Role:** Junior security analyst  |  **Skills:** secrets, containment, rotation, evidence

## Context
Brightside Plumbing Supplies is a 40 person UK business. Their web shop uses a payments provider and an email service. A freelance developer maintains the code in a repository.

## Event
On Tuesday at 09:12 an automated email from the code host says: "A secret that looks like an email service API key was found in a public repository." The repository was made public three days ago so the freelancer could share it with a new client.

## Evidence
```
Repo setting change:   Sat 08:40  visibility private -> public (by freelancer)
Commit f3a9c1e:        Thu 16:05  "add config"  adds file config.js
config.js line 12:     EMAIL_API_KEY = "re_live_xxxxxxxxxxxxxxxx"   (key value redacted here)
Email provider log:
  Sat 11:30  120 emails sent   from IP 203.0.113.50   (normal volume ~20 per day)
  Sun 02:14  4,300 emails sent from IP 198.51.100.9   subject "Urgent invoice attached"
  Mon 13:02  provider flags domain reputation as "poor"
Customer service inbox: 6 customers reported suspicious invoice emails since Sunday.
```

## Your tasks
1. **Triage:** is this a real incident? What does the evidence tell you, and what don't you know yet?
2. **Contain:** what do you do in the first 15 minutes, in what order, and why?
3. **Investigate:** write a timeline. What is the root cause (technical and process)?
4. **Fix:** what changes stop this recurring?
5. **Detect:** what alert would have caught this earlier?
6. **Report:** who must be told (customers, the email provider, a regulator?), and what do you write?

## Deliverable
One page, saved as `practice/responses/s01-aaron.md`. Commit it.
