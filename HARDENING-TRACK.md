# FORGE hardening track

**What it is:** I read, test and fix the security of a real production codebase (FORGE, an AI agent platform that takes live payments and handles personal data), by hand, and publish what I learn.
**Why it counts:** it is real code with real consequences, and every fix has a commit, a test and a writeup.
**Time:** 4 hours every Friday from Week 3. Counted inside the 40.

## The rules
1. **I write the fixes myself.** AI explains and reviews. It does not write the patch. If I cannot explain a line, it does not ship.
2. **One ticket = one branch = one reviewed PR = one writeup.**
3. **Own code only.** Local or preview deployments. No third party systems. No client data.
4. **Unfixed issues stay private.** Details publish only after the fix is deployed. Sanitised: no secrets, IDs, internal hosts.

## Workflow per ticket
1. **Trace** the code path from input to impact.
2. **Reproduce** locally with a minimal proof of concept.
3. **Fix** by hand. Smallest change that closes the class of bug.
4. **Test** that the exploit now fails and normal behaviour still works.
5. **Write** a finding report (`case-studies/TEMPLATE.md`).
6. **Map** to OWASP / CWE and log in `EVIDENCE.md`.

## Schedule
| Weeks | Friday block | Output |
|---|---|---|
| 3 to 6 | JavaScript reading fluency (javascript.info, free) + **attack surface map**: every endpoint, who can call it, what it accepts, what secret it holds, what it costs when abused | `forge-attack-surface-map` |
| 7 to 14 | First fixes, paired with the PortSwigger topic that week (timing and auth, CORS, DOM XSS, weak randomness) | 4 case studies, each with PoC, fix and test |
| 15 to 20 | Tooling: secret scan, semgrep, dependency audit, input validation tests | Triage log with every finding judged |
| 21 to 30 | LLM attack surface review: where untrusted text reaches a model, then indirect prompt injection tests in a sandbox | Flagship research writeup |
| 31 to 40 | Publish: sanitised case study site, one blog post per fixed class | Public portfolio |
| Ongoing | Cleanup tickets, lint, tests, docs reconciliation | Cleaner repo, fewer false claims |

## Tooling (all free)
`npm audit`, gitleaks, semgrep, ESLint (with a security plugin), OWASP ZAP baseline scan against my own preview deployment, Node's built in test runner.

## Portfolio output
- `case-studies/`: one report per fixed issue, before and after diff, test, lesson.
- A summary table on the CV: *"Found and fixed N issues across M classes in a production AI platform; every fix tested and documented."* Only claim the number that is true.
- Interview material: each case study is a 5 minute story with a concrete bug, a proof, a fix and a lesson.

## Honest limits
This proves I can find and fix issues in a real system I know well. It is not an independent pentest. I describe it that way.
