# AI Security Career Program

**Owner:** Aaron F. ([FORGE](https://forgeisagentic.tech)) | **Started:** 23 Oct 2026 | **Target:** remote AI Security Engineer / AI Red Teamer, £80k to £130k+ (UK) or $150k+ (US remote)
**Commitment:** 40 hrs/week | **Horizon:** 12 months to first offer, reviewed every 4 weeks

## The verdict on the Google Doc plan

Direction is right. Three things are wrong.

1. **It skips classic security.** Almost every AI security hire comes from AppSec or pentesting. Interviewers ask about OAuth, SSRF, IAM and threat models before they ask about jailbreaks. Prompt injection is just injection with a new parser. Phase 2 below fixes this.
2. **30 days is a sprint, not a career.** "Memorise the OWASP LLM Top 10" is recall, not skill. Hiring managers test whether you can *find* LLM01 in a real system. The plan below runs 48 weeks with hard gates.
3. **Data annotation work is optional, not Step 1.** Take it only if you need income. It is weak evidence for a security CV unless it is red teaming work (some platforms run adversarial projects; those count).

What to keep: Python first, build in public, the input sanitiser gateway as project #1, evals as the differentiator.

## How this program works

| Rule | What it means |
|---|---|
| Results first | Every week ends with a shipped artefact: a repo commit, a writeup, a lab flag, a cert. No artefact = the week failed. |
| Gates, not dates | You do not enter a phase until you pass the previous gate test (80%+). |
| Tested constantly | Monday recall quiz (from last week), Friday practical, monthly mock interview. See `tests/`. |
| Evidence everywhere | Every artefact is logged in `EVIDENCE.md` with its GitHub link, LinkedIn post and CV bullet. |
| Own every line | If AI wrote it, you rebuild it by hand before it goes on your CV. Interviewers will make you explain it. |
| Free first | Paid courses only where nothing free exists, and only after a gate is passed. |

## Files

| File | Purpose |
|---|---|
| `ROADMAP.md` | 6 phases, 48 weeks, gates, free courses and certs |
| `EVIDENCE.md` | Evidence ledger: what is real today (including FORGE), what it proves, and how to own it |
| `WEEK-01.md` | This week. Exact tasks. |
| `tests/` | Question banks and the testing cadence |
| `log/` | Weekly logs: hours, artefacts, quiz score, blockers |
| `BRAND.md` | GitHub, LinkedIn and CV structure |
| `SETUP-WINDOWS.md` | Workstation setup (WSL2 Ubuntu, VS Code, Git) |
