# Evidence Ledger

Rule: an item goes on the CV only when the **Own it** column is done. Status: ⬜ not owned, 🟨 rebuilt, ✅ public + explainable.

## What we can honestly use from FORGE

FORGE is a real production system that takes real payments and processes personal data. That is genuine security context. **Most of the code was written with Claude.** That is fine and normal in 2026, but say "designed, directed and shipped", and be able to explain every fix without notes.

| # | Real FORGE work | Security concept it proves | OWASP / framework | Own it (task) | Status |
|---|---|---|---|---|---|
| F1 | `lib/webhook-auth.js`: replaced 4 `!==` secret checks with constant time compare, fails closed | Timing attacks, fail closed design | OWASP A07 Auth failures | Write a timing attack demo in Python against `==` vs `hmac.compare_digest` | ⬜ |
| F2 | `lib/rate-limit.js`: per instance Map limiter reset on every cold start, moved to KV | Why in memory rate limits fail on serverless | OWASP API4 Resource consumption | Blog post: "Your serverless rate limiter is decorative" | ⬜ |
| F3 | Tavus video agent + logo AI endpoints rate limited (every call costs money) | **Denial of wallet** on LLM / AI APIs | OWASP LLM10 Unbounded consumption | Cost model: what would 10k scripted calls have cost | ⬜ |
| F4 | `upload-logo`: SVG blocked from a public bucket | Stored XSS via SVG | OWASP A03 Injection | Build a vulnerable SVG upload lab and exploit it | ⬜ |
| F5 | `ledger invoice-create` had no auth; anyone could send invoice emails from FORGE's domain | Phishing relay via unauthenticated endpoint | OWASP API2 Broken auth | Write the incident as a finding report (impact, PoC, fix) | ⬜ |
| F6 | Security headers enforced by a build gate (`audit-site.mjs` SITE-HEADERS) not a checklist | Shift left, security as code | CSP, HSTS | Explain each header and what attack it stops | ⬜ |
| F7 | PayPal webhook idempotency (KV dedup on orderId) | Replay attacks | OWASP API6 Business flows | Diagram the replay and the fix | ⬜ |
| F8 | Shared Resend / Klaviyo keys flagged as security debt | Blast radius, secret isolation | NIST least privilege | Write a remediation plan | ⬜ |
| F9 | `brief-crit.mjs`: deterministic checks override the model (uncited claims fail) | **Not trusting LLM output**; hallucination controls | OWASP LLM09 Misinformation, LLM05 Output handling | Talk track: why the gate cannot be an LLM alone | ⬜ |
| F10 | MARK pipeline: vision gate + deterministic D13 check before the paid model call | Layered LLM output validation | OWASP LLM05 | Same as F9 | ⬜ |
| F11 | Hard Rule 10: the voice agent may never deny being an AI | AI policy, deception risk | NIST AI RMF Govern | One paragraph on AI disclosure policy | ⬜ |
| F12 | SCOUT scrapes third party websites and feeds text to an LLM | **Indirect prompt injection** attack surface (real, not yet tested) | OWASP LLM01 | **Phase 4 Project #2**: red team it in a sandbox, report, fix | ⬜ |
| F13 | RELAY (planned WhatsApp AI agent that books jobs and drafts quotes) | Agent threat model: excessive agency, human approval gate | OWASP LLM06 Excessive agency | STRIDE + OWASP Agentic threat model before it is built | ⬜ |
| F14 | ICO registration ZC176397, DPA required before go live | Data protection compliance (UK GDPR) | Governance | CV line, no task needed | ✅ |

**Do not claim:** that you wrote this code unaided, pentested FORGE, or have "security engineering experience". Claim: "Founder of an AI agent platform in production; identified and remediated X security issues; threat modelled the agent stack."

**Keep secrets out.** FORGE's repo holds internal details (IPs, IDs). Evidence goes into a **separate public repo** with sanitised writeups, never the FORGE repo itself.

## New evidence (fill as you go)

| Date | Artefact | Link | LinkedIn post | CV bullet |
|---|---|---|---|---|
